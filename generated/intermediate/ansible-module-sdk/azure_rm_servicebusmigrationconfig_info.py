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
module: azure_rm_servicebusmigrationconfig_info
version_added: '2.9'
short_description: Get MigrationConfig info.
description:
  - Get info of MigrationConfig.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: MigrationConfigurationsList
  azure_rm_servicebusmigrationconfig_info:
    resource_group: myResourceGroup
    namespace_name: my
    name: $default
- name: MigrationConfigurationsGet
  azure_rm_servicebusmigrationconfig_info:
    resource_group: myResourceGroup
    namespace_name: my
    name: myMigrationConfiguration

'''

RETURN = '''
migration_configs:
  description: >-
    A list of dict results where the key is the name of the MigrationConfig and
    the values are the facts for that MigrationConfig.
  returned: always
  type: complex
  contains:
    migrationconfig_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMigrationConfigsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            namespace_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMigrationConfigsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.name is not None):
            self.results['migration_configs'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['migration_configs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.migration_configs.get(resource_group_name=self.resource_group,
                                                              namespace_name=self.namespace_name,
                                                              config_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.migration_configs.list(resource_group_name=self.resource_group,
                                                               namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMMigrationConfigsInfo()


if __name__ == '__main__':
    main()
