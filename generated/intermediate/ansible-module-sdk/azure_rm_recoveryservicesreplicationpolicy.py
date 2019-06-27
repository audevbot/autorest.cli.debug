#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_recoveryservicesreplicationpolicy
version_added: '2.9'
short_description: Manage Azure ReplicationPolicy instance.
description:
  - 'Create, update and delete instance of Azure ReplicationPolicy.'
options:
  resource_name:
    description:
      - The name of the recovery services vault.
    required: true
  resource_group:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
  name:
    description:
      - Resource Name
  provider_specific_input:
    description:
      - The ReplicationProviderSettings.
  friendly_name:
    description:
      - The FriendlyName.
  provider_specific_details:
    description:
      - The ReplicationChannelSetting.
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource Type
  location:
    description:
      - Resource Location
  state:
    description:
      - Assert the state of the ReplicationPolicy.
      - >-
        Use C(present) to create or update an ReplicationPolicy and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Creates the policy.
  azure_rm_recoveryservicesreplicationpolicy:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationPolicy
    input:
      properties:
        providerSpecificInput:
          instanceType: HyperVReplicaAzure
- name: Updates the policy.
  azure_rm_recoveryservicesreplicationpolicy:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationPolicy
    input:
      properties:
        replicationProviderSettings:
          instanceType: HyperVReplicaAzure
- name: Delete the policy.
  azure_rm_recoveryservicesreplicationpolicy:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationPolicy
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource Name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource Type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource Location
  returned: always
  type: str
  sample: null
properties:
  description:
    - The custom data.
  returned: always
  type: dict
  sample: null
  contains:
    friendly_name:
      description:
        - The FriendlyName.
      returned: always
      type: str
      sample: null
    provider_specific_details:
      description:
        - The ReplicationChannelSetting.
      returned: always
      type: dict
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.recoveryservices import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMReplicationPolicies(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='policy_name',
                required=true
            ),
            provider_specific_input=dict(
                type='dict',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMReplicationPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                         supports_check_mode=True,
                                                         supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServices,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if self.location is None:
            self.location = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.replication_policies.create(resource_name=self.resource_name,
                                                                        resource_group_name=self.resource_group,
                                                                        policy_name=self.name,
                                                                        input=self.input)
            else:
                response = self.mgmt_client.replication_policies.update(resource_name=self.resource_name,
                                                                        resource_group_name=self.resource_group,
                                                                        policy_name=self.name,
                                                                        input=self.input)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ReplicationPolicy instance.')
            self.fail('Error creating the ReplicationPolicy instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ReplicationPolicy instance {0}'.format(self.))
        try:
            response = self.mgmt_client.replication_policies.delete(resource_name=self.resource_name,
                                                                    resource_group_name=self.resource_group,
                                                                    policy_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ReplicationPolicy instance.')
            self.fail('Error deleting the ReplicationPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationPolicy instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.replication_policies.get(resource_name=self.resource_name,
                                                                 resource_group_name=self.resource_group,
                                                                 policy_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMReplicationPolicies()


if __name__ == '__main__':
    main()
