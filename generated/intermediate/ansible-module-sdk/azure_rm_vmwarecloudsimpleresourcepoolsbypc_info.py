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
module: azure_rm_vmwarecloudsimpleresourcepoolsbypc_info
version_added: '2.9'
short_description: Get ResourcePoolsByPC info.
description:
  - Get info of ResourcePoolsByPC.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  name:
    description:
      - The private cloud name
    required: true
    type: str
  next_link:
    description:
      - Link for next list of ResourcePoolsList
    type: str
  value:
    description:
      - Results of the Resource pools list
    type: list
    suboptions:
      id:
        description:
          - 'resource pool id (privateCloudId:vsphereId)'
        required: true
        type: str
      location:
        description:
          - Azure region
        type: str
      name:
        description:
          - '{ResourcePoolName}'
        type: str
      private_cloud_id:
        description:
          - The Private Cloud Id
        type: str
      full_name:
        description:
          - Hierarchical resource pool name
        type: str
      type:
        description:
          - '{resourceProviderNamespace}/{resourceType}'
        type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListResourcePools
  azure_rm_vmwarecloudsimpleresourcepoolsbypc_info:
    region_id: myLocation
    name: myPrivateCloud

'''

RETURN = '''
resource_pools_by_pc:
  description: >-
    A list of dict results where the key is the name of the ResourcePoolsByPC
    and the values are the facts for that ResourcePoolsByPC.
  returned: always
  type: complex
  contains:
    resourcepoolsbypc_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - Link for next list of ResourcePoolsList
          returned: always
          type: str
          sample: null
        value:
          description:
            - Results of the Resource pools list
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - 'resource pool id (privateCloudId:vsphereId)'
              returned: always
              type: str
              sample: null
            location:
              description:
                - Azure region
              returned: always
              type: str
              sample: null
            name:
              description:
                - '{ResourcePoolName}'
              returned: always
              type: str
              sample: null
            private_cloud_id:
              description:
                - The Private Cloud Id
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Resource pool properties
              returned: always
              type: dict
              sample: null
            full_name:
              description:
                - Hierarchical resource pool name
              returned: always
              type: str
              sample: null
            type:
              description:
                - '{resourceProviderNamespace}/{resourceType}'
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


class AzureRMResourcePoolsByPCInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.region_id = None
        self.name = None
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
        super(AzureRMResourcePoolsByPCInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.name is not None):
            self.results['resource_pools_by_pc'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.resource_pools_by_pc.list(region_id=self.region_id,
                                                                  pc_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMResourcePoolsByPCInfo()


if __name__ == '__main__':
    main()
