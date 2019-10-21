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
module: azure_rm_servicebusmigrationconfig
version_added: '2.9'
short_description: Manage Azure MigrationConfig instance.
description:
  - 'Create, update and delete instance of Azure MigrationConfig.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  name:
    description:
      - Resource name
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  provisioning_state:
    description:
      - 'Provisioning state of Migration Configuration '
    type: str
  pending_replication_operations_count:
    description:
      - Number of entities pending to be replicated.
    type: number
  target_namespace:
    description:
      - >-
        Existing premium Namespace ARM Id name which has no entities, will be
        used for migration
    required: true
    type: str
  post_migration_name:
    description:
      - Name to access Standard Namespace after migration
    required: true
    type: str
  migration_state:
    description:
      - >-
        State in which Standard to Premium Migration is, possible values :
        Unknown, Reverting, Completing, Initiating, Syncing, Active
    type: str
  state:
    description:
      - Assert the state of the MigrationConfig.
      - >-
        Use C(present) to create or update an MigrationConfig and C(absent) to
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
[]

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
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties required to the Create Migration Configuration
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMigrationConfigs(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='namespace_name',
                required=true
            ),
            provisioning_state=dict(
                type='str',
                disposition='/'
            ),
            pending_replication_operations_count=dict(
                type='number',
                disposition='/'
            ),
            target_namespace=dict(
                type='str',
                disposition='/',
                required=true
            ),
            post_migration_name=dict(
                type='str',
                disposition='/',
                required=true
            ),
            migration_state=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMigrationConfigs, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
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
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.migration_configs.create()
            else:
                response = self.mgmt_client.migration_configs.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MigrationConfig instance.')
            self.fail('Error creating the MigrationConfig instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the MigrationConfig instance {0}'.format(self.))
        try:
            response = self.mgmt_client.migration_configs.delete()
        except CloudError as e:
            self.log('Error attempting to delete the MigrationConfig instance.')
            self.fail('Error deleting the MigrationConfig instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the MigrationConfig instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.migration_configs.get(resource_group_name=self.resource_group,
                                                              namespace_name=self.name,
                                                              config_name=self.configName)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMigrationConfigs()


if __name__ == '__main__':
    main()
