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
module: azure_rm_recoveryservicesreplicationprotectioncontainer
version_added: '2.9'
short_description: Manage Azure ReplicationProtectionContainer instance.
description:
  - 'Create, update and delete instance of Azure ReplicationProtectionContainer.'
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
  fabric_name:
    description:
      - Unique fabric ARM name.
    required: true
  name:
    description:
      - Resource Name
  provider_specific_input:
    description:
      - Provider specific inputs for container creation.
    type: list
  fabric_friendly_name:
    description:
      - Fabric friendly name.
  friendly_name:
    description:
      - The name.
  fabric_type:
    description:
      - The fabric type.
  protected_item_count:
    description:
      - Number of protected PEs
  pairing_status:
    description:
      - The pairing status of this cloud.
  role:
    description:
      - The role of this cloud.
  fabric_specific_details:
    description:
      - Fabric specific details.
    suboptions:
      instance_type:
        description:
          - Gets the class type. Overridden in derived classes.
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
      - Assert the state of the ReplicationProtectionContainer.
      - >-
        Use C(present) to create or update an ReplicationProtectionContainer and
        C(absent) to delete it.
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
- name: Create a protection container.
  azure_rm_recoveryservicesreplicationprotectioncontainer:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    name: myReplicationProtectionContainer
    creation_input:
      properties:
        providerSpecificInput:
          - instanceType: ReplicationProviderSpecificContainerCreationInput
- name: Removes a protection container.
  azure_rm_recoveryservicesreplicationprotectioncontainer:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    name: myReplicationProtectionContainer

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
    fabric_friendly_name:
      description:
        - Fabric friendly name.
      returned: always
      type: str
      sample: null
    friendly_name:
      description:
        - The name.
      returned: always
      type: str
      sample: null
    fabric_type:
      description:
        - The fabric type.
      returned: always
      type: str
      sample: null
    protected_item_count:
      description:
        - Number of protected PEs
      returned: always
      type: number
      sample: null
    pairing_status:
      description:
        - The pairing status of this cloud.
      returned: always
      type: str
      sample: null
    role:
      description:
        - The role of this cloud.
      returned: always
      type: str
      sample: null
    fabric_specific_details:
      description:
        - Fabric specific details.
      returned: always
      type: dict
      sample: null
      contains:
        instance_type:
          description:
            - Gets the class type. Overridden in derived classes.
          returned: always
          type: str
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


class AzureRMReplicationProtectionContainers(AzureRMModuleBaseExt):
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
            fabric_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='protection_container_name',
                required=true
            ),
            provider_specific_input=dict(
                type='list',
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
        self.fabric_name = None
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

        super(AzureRMReplicationProtectionContainers, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.replication_protection_containers.create(resource_name=self.resource_name,
                                                                                     resource_group_name=self.resource_group,
                                                                                     fabric_name=self.fabric_name,
                                                                                     protection_container_name=self.name,
                                                                                     creation_input=self.creationInput)
            else:
                response = self.mgmt_client.replication_protection_containers.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ReplicationProtectionContainer instance.')
            self.fail('Error creating the ReplicationProtectionContainer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ReplicationProtectionContainer instance {0}'.format(self.))
        try:
            response = self.mgmt_client.replication_protection_containers.delete(resource_name=self.resource_name,
                                                                                 resource_group_name=self.resource_group,
                                                                                 fabric_name=self.fabric_name,
                                                                                 protection_container_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ReplicationProtectionContainer instance.')
            self.fail('Error deleting the ReplicationProtectionContainer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationProtectionContainer instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.replication_protection_containers.get(resource_name=self.resource_name,
                                                                              resource_group_name=self.resource_group,
                                                                              fabric_name=self.fabric_name,
                                                                              protection_container_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMReplicationProtectionContainers()


if __name__ == '__main__':
    main()
