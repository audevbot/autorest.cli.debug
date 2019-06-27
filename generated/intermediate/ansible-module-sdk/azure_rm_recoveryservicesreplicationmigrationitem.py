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
module: azure_rm_recoveryservicesreplicationmigrationitem
version_added: '2.9'
short_description: Manage Azure ReplicationMigrationItem instance.
description:
  - 'Create, update and delete instance of Azure ReplicationMigrationItem.'
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
      - Fabric name.
    required: true
  protection_container_name:
    description:
      - Protection container name.
    required: true
  name:
    description:
      - Resource Name
  policy_id:
    description:
      - The policy Id.
    required: true
  provider_specific_details:
    description:
      - The provider specific details.
    required: true
  machine_name:
    description:
      - The on-premise virtual machine name.
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
      - Assert the state of the ReplicationMigrationItem.
      - >-
        Use C(present) to create or update an ReplicationMigrationItem and
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
- name: Enables migration.
  azure_rm_recoveryservicesreplicationmigrationitem:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationMigrationItem
    input:
      properties:
        policyId: >-
          /Subscriptions/cb53d0c3-bd59-4721-89bc-06916a9147ef/resourceGroups/resourcegroup1/providers/Microsoft.RecoveryServices/vaults/migrationvault/replicationPolicies/vmwarepolicy1
        providerSpecificDetails:
          instanceType: VMwareCbt
- name: Updates migration item.
  azure_rm_recoveryservicesreplicationmigrationitem:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationMigrationItem
    input:
      properties:
        providerSpecificDetails:
          instanceType: VMwareCbt
- name: Delete the migration item.
  azure_rm_recoveryservicesreplicationmigrationitem:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationMigrationItem
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
    - The migration item properties.
  returned: always
  type: dict
  sample: null
  contains:
    machine_name:
      description:
        - The on-premise virtual machine name.
      returned: always
      type: str
      sample: null
    policy_id:
      description:
        - The ARM Id of policy governing this item.
      returned: always
      type: str
      sample: null
    policy_friendly_name:
      description:
        - The name of policy governing this item.
      returned: always
      type: str
      sample: null
    recovery_services_provider_id:
      description:
        - The recovery services provider ARM Id.
      returned: always
      type: str
      sample: null
    migration_state:
      description:
        - The migration status.
      returned: always
      type: str
      sample: null
    migration_state_description:
      description:
        - The migration state description.
      returned: always
      type: str
      sample: null
    test_migrate_state:
      description:
        - The test migrate state.
      returned: always
      type: str
      sample: null
    test_migrate_state_description:
      description:
        - The test migrate state description.
      returned: always
      type: str
      sample: null
    health:
      description:
        - The consolidated health.
      returned: always
      type: str
      sample: null
    health_errors:
      description:
        - The list of health errors.
      returned: always
      type: dict
      sample: null
      contains:
        inner_health_errors:
          description:
            - >-
              The inner health errors. HealthError having a list of HealthError
              as child errors is problematic. InnerHealthError is used because
              this will prevent an infinite loop of structures when Hydra tries
              to auto-generate the contract. We are exposing the related health
              errors as inner health errors and all API consumers can utilize
              this in the same fashion as Exception -&gt; InnerException.
          returned: always
          type: dict
          sample: null
          contains:
            error_source:
              description:
                - Source of error.
              returned: always
              type: str
              sample: null
            error_type:
              description:
                - Type of error.
              returned: always
              type: str
              sample: null
            error_level:
              description:
                - Level of error.
              returned: always
              type: str
              sample: null
            error_category:
              description:
                - Category of error.
              returned: always
              type: str
              sample: null
            error_code:
              description:
                - Error code.
              returned: always
              type: str
              sample: null
            summary_message:
              description:
                - Summary message of the entity.
              returned: always
              type: str
              sample: null
            error_message:
              description:
                - Error message.
              returned: always
              type: str
              sample: null
            possible_causes:
              description:
                - Possible causes of error.
              returned: always
              type: str
              sample: null
            recommended_action:
              description:
                - Recommended action to resolve error.
              returned: always
              type: str
              sample: null
            creation_time_utc:
              description:
                - Error creation time (UTC)
              returned: always
              type: datetime
              sample: null
            recovery_provider_error_message:
              description:
                - DRA error message.
              returned: always
              type: str
              sample: null
            entity_id:
              description:
                - ID of the entity.
              returned: always
              type: str
              sample: null
        error_source:
          description:
            - Source of error.
          returned: always
          type: str
          sample: null
        error_type:
          description:
            - Type of error.
          returned: always
          type: str
          sample: null
        error_level:
          description:
            - Level of error.
          returned: always
          type: str
          sample: null
        error_category:
          description:
            - Category of error.
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - Error code.
          returned: always
          type: str
          sample: null
        summary_message:
          description:
            - Summary message of the entity.
          returned: always
          type: str
          sample: null
        error_message:
          description:
            - Error message.
          returned: always
          type: str
          sample: null
        possible_causes:
          description:
            - Possible causes of error.
          returned: always
          type: str
          sample: null
        recommended_action:
          description:
            - Recommended action to resolve error.
          returned: always
          type: str
          sample: null
        creation_time_utc:
          description:
            - Error creation time (UTC)
          returned: always
          type: datetime
          sample: null
        recovery_provider_error_message:
          description:
            - DRA error message.
          returned: always
          type: str
          sample: null
        entity_id:
          description:
            - ID of the entity.
          returned: always
          type: str
          sample: null
        error_id:
          description:
            - The health error unique id.
          returned: always
          type: str
          sample: null
        customer_resolvability:
          description:
            - Value indicating whether the health error is customer resolvable.
          returned: always
          type: str
          sample: null
    allowed_operations:
      description:
        - >-
          The allowed operations on the migration item, based on the current
          migration state of the item.
      returned: always
      type: str
      sample: null
    current_job:
      description:
        - The current job details.
      returned: always
      type: dict
      sample: null
      contains:
        job_name:
          description:
            - The job name.
          returned: always
          type: str
          sample: null
        job_id:
          description:
            - The ARM Id of the job being executed.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - The start time of the job.
          returned: always
          type: datetime
          sample: null
    provider_specific_details:
      description:
        - The migration provider custom settings.
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


class AzureRMReplicationMigrationItems(AzureRMModuleBaseExt):
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
            protection_container_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='migration_item_name',
                required=true
            ),
            policy_id=dict(
                type='str',
                disposition='/',
                required=true
            ),
            provider_specific_details=dict(
                type='dict',
                disposition='/',
                required=true
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
        self.protection_container_name = None
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

        super(AzureRMReplicationMigrationItems, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.replication_migration_items.create(resource_name=self.resource_name,
                                                                               resource_group_name=self.resource_group,
                                                                               fabric_name=self.fabric_name,
                                                                               protection_container_name=self.protection_container_name,
                                                                               migration_item_name=self.name,
                                                                               input=self.input)
            else:
                response = self.mgmt_client.replication_migration_items.update(resource_name=self.resource_name,
                                                                               resource_group_name=self.resource_group,
                                                                               fabric_name=self.fabric_name,
                                                                               protection_container_name=self.protection_container_name,
                                                                               migration_item_name=self.name,
                                                                               input=self.input)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ReplicationMigrationItem instance.')
            self.fail('Error creating the ReplicationMigrationItem instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ReplicationMigrationItem instance {0}'.format(self.))
        try:
            response = self.mgmt_client.replication_migration_items.delete(resource_name=self.resource_name,
                                                                           resource_group_name=self.resource_group,
                                                                           fabric_name=self.fabric_name,
                                                                           protection_container_name=self.protection_container_name,
                                                                           migration_item_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ReplicationMigrationItem instance.')
            self.fail('Error deleting the ReplicationMigrationItem instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationMigrationItem instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.replication_migration_items.get(resource_name=self.resource_name,
                                                                        resource_group_name=self.resource_group,
                                                                        fabric_name=self.fabric_name,
                                                                        protection_container_name=self.protection_container_name,
                                                                        migration_item_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMReplicationMigrationItems()


if __name__ == '__main__':
    main()
