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
module: azure_rm_recoveryservicestargetcomputesize_info
version_added: '2.9'
short_description: Get TargetComputeSize info.
description:
  - Get info of TargetComputeSize.
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
      - protection container name.
    required: true
  name:
    description:
      - Replication protected item name.
    required: true
  value:
    description:
      - The list of target compute sizes.
    type: list
    suboptions:
      id:
        description:
          - The Id.
      name:
        description:
          - Target compute size name.
      type:
        description:
          - The Type of the object.
      friendly_name:
        description:
          - Target compute size display name.
      cpu_cores_count:
        description:
          - The maximum cpu cores count supported by target compute size.
      memory_in_gb:
        description:
          - The maximum memory in GB supported by target compute size.
      max_data_disk_count:
        description:
          - The maximum data disks count supported by target compute size.
      max_nics_count:
        description:
          - The maximum Nics count supported by target compute size.
      errors:
        description:
          - >-
            The reasons why the target compute size is not applicable for the
            protected item.
        type: list
        suboptions:
          message:
            description:
              - The error message.
          severity:
            description:
              - The severity of the error.
      high_iops_supported:
        description:
          - >-
            The value indicating whether the target compute size supports high
            Iops.
  next_link:
    description:
      - The value of next link.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of target compute sizes for the replication protected item.
  azure_rm_recoveryservicestargetcomputesize_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationProtectedItem

'''

RETURN = '''
target_compute_sizes:
  description: >-
    A list of dict results where the key is the name of the TargetComputeSize
    and the values are the facts for that TargetComputeSize.
  returned: always
  type: complex
  contains:
    targetcomputesize_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - The list of target compute sizes.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - The Id.
              returned: always
              type: str
              sample: null
            name:
              description:
                - Target compute size name.
              returned: always
              type: str
              sample: null
            type:
              description:
                - The Type of the object.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - The custom data.
              returned: always
              type: dict
              sample: null
            friendly_name:
              description:
                - Target compute size display name.
              returned: always
              type: str
              sample: null
            cpu_cores_count:
              description:
                - The maximum cpu cores count supported by target compute size.
              returned: always
              type: number
              sample: null
            memory_in_gb:
              description:
                - The maximum memory in GB supported by target compute size.
              returned: always
              type: number
              sample: null
            max_data_disk_count:
              description:
                - The maximum data disks count supported by target compute size.
              returned: always
              type: number
              sample: null
            max_nics_count:
              description:
                - The maximum Nics count supported by target compute size.
              returned: always
              type: number
              sample: null
            errors:
              description:
                - >-
                  The reasons why the target compute size is not applicable for
                  the protected item.
              returned: always
              type: dict
              sample: null
              contains:
                message:
                  description:
                    - The error message.
                  returned: always
                  type: str
                  sample: null
                severity:
                  description:
                    - The severity of the error.
                  returned: always
                  type: str
                  sample: null
            high_iops_supported:
              description:
                - >-
                  The value indicating whether the target compute size supports
                  high Iops.
              returned: always
              type: str
              sample: null
        next_link:
          description:
            - The value of next link.
          returned: always
          type: str
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


class AzureRMTargetComputeSizesInfo(AzureRMModuleBase):
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
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.fabric_name = None
        self.protection_container_name = None
        self.name = None
        self.value = None
        self.next_link = None

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
        super(AzureRMTargetComputeSizesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

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
            self.results['target_compute_sizes'] = self.format_item(self.listbyreplicationprotecteditems())
        return self.results

    def listbyreplicationprotecteditems(self):
        response = None

        try:
            response = self.mgmt_client.target_compute_sizes.list_by_replication_protected_items(resource_name=self.resource_name,
                                                                                                 resource_group_name=self.resource_group,
                                                                                                 fabric_name=self.fabric_name,
                                                                                                 protection_container_name=self.protection_container_name,
                                                                                                 replicated_protected_item_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMTargetComputeSizesInfo()


if __name__ == '__main__':
    main()
