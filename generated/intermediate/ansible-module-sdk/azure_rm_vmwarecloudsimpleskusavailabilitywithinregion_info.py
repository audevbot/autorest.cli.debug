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
module: azure_rm_vmwarecloudsimpleskusavailabilitywithinregion_info
version_added: '2.9'
short_description: Get SkusAvailabilityWithinRegion info.
description:
  - Get info of SkusAvailabilityWithinRegion.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  sku_id:
    description:
      - 'sku id, if no sku is passed availability for all skus will be returned'
    required: true
    type: str
  next_link:
    description:
      - Link for next list of DedicatedCloudNode
    type: str
  value:
    description:
      - Results of the DedicatedPlacementGroupSkuAvailability list
    type: list
    suboptions:
      dedicated_availability_zone_id:
        description:
          - CloudSimple Availability Zone id
        type: str
      dedicated_availability_zone_name:
        description:
          - CloudSimple Availability Zone Name
        type: str
      dedicated_placement_group_id:
        description:
          - CloudSimple Placement Group Id
        type: str
      dedicated_placement_group_name:
        description:
          - CloudSimple Placement Group name
        type: str
      limit:
        description:
          - indicates how many resources of a given SKU is available in a AZ->PG
        required: true
        type: number
      resource_type:
        description:
          - resource type e.g. DedicatedCloudNodes
        type: str
      sku_id:
        description:
          - sku id
        type: str
      sku_name:
        description:
          - sku name
        type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListAvailabilities
  azure_rm_vmwarecloudsimpleskusavailabilitywithinregion_info:
    region_id: myLocation

'''

RETURN = '''
skus_availability_within_region:
  description: >-
    A list of dict results where the key is the name of the
    SkusAvailabilityWithinRegion and the values are the facts for that
    SkusAvailabilityWithinRegion.
  returned: always
  type: complex
  contains:
    skusavailabilitywithinregion_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - Link for next list of DedicatedCloudNode
          returned: always
          type: str
          sample: null
        value:
          description:
            - Results of the DedicatedPlacementGroupSkuAvailability list
          returned: always
          type: dict
          sample: null
          contains:
            dedicated_availability_zone_id:
              description:
                - CloudSimple Availability Zone id
              returned: always
              type: str
              sample: null
            dedicated_availability_zone_name:
              description:
                - CloudSimple Availability Zone Name
              returned: always
              type: str
              sample: null
            dedicated_placement_group_id:
              description:
                - CloudSimple Placement Group Id
              returned: always
              type: str
              sample: null
            dedicated_placement_group_name:
              description:
                - CloudSimple Placement Group name
              returned: always
              type: str
              sample: null
            limit:
              description:
                - >-
                  indicates how many resources of a given SKU is available in a
                  AZ->PG
              returned: always
              type: number
              sample: null
            resource_type:
              description:
                - resource type e.g. DedicatedCloudNodes
              returned: always
              type: str
              sample: null
            sku_id:
              description:
                - sku id
              returned: always
              type: str
              sample: null
            sku_name:
              description:
                - sku name
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
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSkusAvailabilityWithinRegionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=true
            ),
            sku_id=dict(
                type='str',
                required=true
            )
        )

        self.region_id = None
        self.sku_id = None
        self.next_link = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSkusAvailabilityWithinRegionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None):
            self.results['skus_availability_within_region'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.skus_availability_within_region.list(region_id=self.region_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMSkusAvailabilityWithinRegionInfo()


if __name__ == '__main__':
    main()
