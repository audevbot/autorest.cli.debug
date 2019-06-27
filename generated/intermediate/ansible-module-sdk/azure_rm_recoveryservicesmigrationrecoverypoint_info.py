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
module: azure_rm_recoveryservicesmigrationrecoverypoint_info
version_added: '2.9'
short_description: Get MigrationRecoveryPoint info.
description:
  - Get info of MigrationRecoveryPoint.
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
      - Fabric unique name.
    required: true
  protection_container_name:
    description:
      - Protection container name.
    required: true
  migration_item_name:
    description:
      - Migration item name.
    required: true
  name:
    description:
      - Resource Name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource Type
  location:
    description:
      - Resource Location
  recovery_point_time:
    description:
      - The recovery point time.
  recovery_point_type:
    description:
      - The recovery point type.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the recovery points for a migration item.
  azure_rm_recoveryservicesmigrationrecoverypoint_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    migration_item_name: myReplicationMigrationItem
- name: Gets a recovery point for a migration item.
  azure_rm_recoveryservicesmigrationrecoverypoint_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    migration_item_name: myReplicationMigrationItem
    name: myMigrationRecoveryPoint

'''

RETURN = '''
migration_recovery_points:
  description: >-
    A list of dict results where the key is the name of the
    MigrationRecoveryPoint and the values are the facts for that
    MigrationRecoveryPoint.
  returned: always
  type: complex
  contains:
    migrationrecoverypoint_name:
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
            - Recovery point properties.
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
    from azure.mgmt.recoveryservices import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMigrationRecoveryPointsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                required=true
            ),
            resource_group=dict(
                type='str',
                required=true
            ),
            fabric_name=dict(
                type='str',
                required=true
            ),
            protection_container_name=dict(
                type='str',
                required=true
            ),
            migration_item_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.fabric_name = None
        self.protection_container_name = None
        self.migration_item_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-10'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMigrationRecoveryPointsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.protection_container_name is not None and
            self.migration_item_name is not None and
            self.name is not None):
            self.results['migration_recovery_points'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None and
              self.protection_container_name is not None and
              self.migration_item_name is not None):
            self.results['migration_recovery_points'] = self.format_item(self.listbyreplicationmigrationitems())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.migration_recovery_points.get(resource_name=self.resource_name,
                                                                      resource_group_name=self.resource_group,
                                                                      fabric_name=self.fabric_name,
                                                                      protection_container_name=self.protection_container_name,
                                                                      migration_item_name=self.migration_item_name,
                                                                      migration_recovery_point_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyreplicationmigrationitems(self):
        response = None

        try:
            response = self.mgmt_client.migration_recovery_points.list_by_replication_migration_items(resource_name=self.resource_name,
                                                                                                      resource_group_name=self.resource_group,
                                                                                                      fabric_name=self.fabric_name,
                                                                                                      protection_container_name=self.protection_container_name,
                                                                                                      migration_item_name=self.migration_item_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMMigrationRecoveryPointsInfo()


if __name__ == '__main__':
    main()
