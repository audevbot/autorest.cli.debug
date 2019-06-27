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
module: azure_rm_recoveryservicesrecoverypoint_info
version_added: '2.9'
short_description: Get RecoveryPoint info.
description:
  - Get info of RecoveryPoint.
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
      - The fabric name.
    required: true
  protection_container_name:
    description:
      - The protection container name.
    required: true
  replicated_protected_item_name:
    description:
      - The replication protected item's name.
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
      - 'The recovery point type: ApplicationConsistent, CrashConsistent.'
  provider_specific_details:
    description:
      - The provider specific details for the recovery point.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Get recovery points for a replication protected item.
  azure_rm_recoveryservicesrecoverypoint_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    replicated_protected_item_name: myReplicationProtectedItem
- name: Get a recovery point.
  azure_rm_recoveryservicesrecoverypoint_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    replicated_protected_item_name: myReplicationProtectedItem
    name: myRecoveryPoint

'''

RETURN = '''
recovery_points:
  description: >-
    A list of dict results where the key is the name of the RecoveryPoint and
    the values are the facts for that RecoveryPoint.
  returned: always
  type: complex
  contains:
    recoverypoint_name:
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
            - Recovery point related data.
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


class AzureRMRecoveryPointsInfo(AzureRMModuleBase):
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
            replicated_protected_item_name=dict(
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
        self.replicated_protected_item_name = None
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
        super(AzureRMRecoveryPointsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.protection_container_name is not None and
            self.replicated_protected_item_name is not None and
            self.name is not None):
            self.results['recovery_points'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None and
              self.protection_container_name is not None and
              self.replicated_protected_item_name is not None):
            self.results['recovery_points'] = self.format_item(self.listbyreplicationprotecteditems())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.recovery_points.get(resource_name=self.resource_name,
                                                            resource_group_name=self.resource_group,
                                                            fabric_name=self.fabric_name,
                                                            protection_container_name=self.protection_container_name,
                                                            replicated_protected_item_name=self.replicated_protected_item_name,
                                                            recovery_point_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyreplicationprotecteditems(self):
        response = None

        try:
            response = self.mgmt_client.recovery_points.list_by_replication_protected_items(resource_name=self.resource_name,
                                                                                            resource_group_name=self.resource_group,
                                                                                            fabric_name=self.fabric_name,
                                                                                            protection_container_name=self.protection_container_name,
                                                                                            replicated_protected_item_name=self.replicated_protected_item_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMRecoveryPointsInfo()


if __name__ == '__main__':
    main()
