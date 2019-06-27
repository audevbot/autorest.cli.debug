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
module: azure_rm_recoveryservicesreplicationmigrationitem_info
version_added: '2.9'
short_description: Get ReplicationMigrationItem info.
description:
  - Get info of ReplicationMigrationItem.
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
  skip_token:
    description:
      - The pagination token.
  fabric_name:
    description:
      - Fabric unique name.
  protection_container_name:
    description:
      - Protection container name.
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
  machine_name:
    description:
      - The on-premise virtual machine name.
  policy_id:
    description:
      - The ARM Id of policy governing this item.
  policy_friendly_name:
    description:
      - The name of policy governing this item.
  recovery_services_provider_id:
    description:
      - The recovery services provider ARM Id.
  migration_state:
    description:
      - The migration status.
  migration_state_description:
    description:
      - The migration state description.
  test_migrate_state:
    description:
      - The test migrate state.
  test_migrate_state_description:
    description:
      - The test migrate state description.
  health:
    description:
      - The consolidated health.
  health_errors:
    description:
      - The list of health errors.
    type: list
    suboptions:
      inner_health_errors:
        description:
          - >-
            The inner health errors. HealthError having a list of HealthError as
            child errors is problematic. InnerHealthError is used because this
            will prevent an infinite loop of structures when Hydra tries to
            auto-generate the contract. We are exposing the related health
            errors as inner health errors and all API consumers can utilize this
            in the same fashion as Exception -&gt; InnerException.
        type: list
        suboptions:
          error_source:
            description:
              - Source of error.
          error_type:
            description:
              - Type of error.
          error_level:
            description:
              - Level of error.
          error_category:
            description:
              - Category of error.
          error_code:
            description:
              - Error code.
          summary_message:
            description:
              - Summary message of the entity.
          error_message:
            description:
              - Error message.
          possible_causes:
            description:
              - Possible causes of error.
          recommended_action:
            description:
              - Recommended action to resolve error.
          creation_time_utc:
            description:
              - Error creation time (UTC)
          recovery_provider_error_message:
            description:
              - DRA error message.
          entity_id:
            description:
              - ID of the entity.
      error_source:
        description:
          - Source of error.
      error_type:
        description:
          - Type of error.
      error_level:
        description:
          - Level of error.
      error_category:
        description:
          - Category of error.
      error_code:
        description:
          - Error code.
      summary_message:
        description:
          - Summary message of the entity.
      error_message:
        description:
          - Error message.
      possible_causes:
        description:
          - Possible causes of error.
      recommended_action:
        description:
          - Recommended action to resolve error.
      creation_time_utc:
        description:
          - Error creation time (UTC)
      recovery_provider_error_message:
        description:
          - DRA error message.
      entity_id:
        description:
          - ID of the entity.
      error_id:
        description:
          - The health error unique id.
      customer_resolvability:
        description:
          - Value indicating whether the health error is customer resolvable.
  allowed_operations:
    description:
      - >-
        The allowed operations on the migration item, based on the current
        migration state of the item.
    type: list
  current_job:
    description:
      - The current job details.
    suboptions:
      job_name:
        description:
          - The job name.
      job_id:
        description:
          - The ARM Id of the job being executed.
      start_time:
        description:
          - The start time of the job.
  provider_specific_details:
    description:
      - The migration provider custom settings.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of migration items in the vault.
  azure_rm_recoveryservicesreplicationmigrationitem_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the list of migration items in the protection container.
  azure_rm_recoveryservicesreplicationmigrationitem_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
- name: Gets the details of a migration item.
  azure_rm_recoveryservicesreplicationmigrationitem_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationMigrationItem

'''

RETURN = '''
replication_migration_items:
  description: >-
    A list of dict results where the key is the name of the
    ReplicationMigrationItem and the values are the facts for that
    ReplicationMigrationItem.
  returned: always
  type: complex
  contains:
    replicationmigrationitem_name:
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
            - The migration item properties.
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


class AzureRMReplicationMigrationItemsInfo(AzureRMModuleBase):
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
            skip_token=dict(
                type='str'
            ),
            fabric_name=dict(
                type='str'
            ),
            protection_container_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.skip_token = None
        self.fabric_name = None
        self.protection_container_name = None
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
        super(AzureRMReplicationMigrationItemsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.protection_container_name is not None and
            self.name is not None):
            self.results['replication_migration_items'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None and
              self.protection_container_name is not None):
            self.results['replication_migration_items'] = self.format_item(self.listbyreplicationprotectioncontainers())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_migration_items'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.replication_migration_items.get(resource_name=self.resource_name,
                                                                        resource_group_name=self.resource_group,
                                                                        fabric_name=self.fabric_name,
                                                                        protection_container_name=self.protection_container_name,
                                                                        migration_item_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyreplicationprotectioncontainers(self):
        response = None

        try:
            response = self.mgmt_client.replication_migration_items.list_by_replication_protection_containers(resource_name=self.resource_name,
                                                                                                              resource_group_name=self.resource_group,
                                                                                                              fabric_name=self.fabric_name,
                                                                                                              protection_container_name=self.protection_container_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.replication_migration_items.list(resource_name=self.resource_name,
                                                                         resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMReplicationMigrationItemsInfo()


if __name__ == '__main__':
    main()
