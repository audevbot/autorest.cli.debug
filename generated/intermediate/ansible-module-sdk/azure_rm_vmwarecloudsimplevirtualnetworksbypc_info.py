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
module: azure_rm_vmwarecloudsimplevirtualnetworksbypc_info
version_added: '2.9'
short_description: Get VirtualNetworksByPC info.
description:
  - Get info of VirtualNetworksByPC.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  name:
    description:
      - >-
        Resource pool used to derive vSphere cluster which contains virtual
        networks
    required: true
    type: str
  next_link:
    description:
      - Link for next list of VirtualNetwork
    type: str
  value:
    description:
      - Results of the VirtualNetwork list
    type: list
    suboptions:
      assignable:
        description:
          - can be used in vm creation/deletion
        type: boolean
      id:
        description:
          - 'virtual network id (privateCloudId:vsphereId)'
        required: true
        type: str
      location:
        description:
          - Azure region
        type: str
      name:
        description:
          - '{VirtualNetworkName}'
        type: str
      private_cloud_id:
        description:
          - The Private Cloud id
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
- name: ListVirtualNetworks
  azure_rm_vmwarecloudsimplevirtualnetworksbypc_info:
    region_id: myLocation
    pc_name: myPrivateCloud
    name: >-
      /subscriptions/{{ subscription_id
      }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name
      }}/privateClouds/{{ private_cloud_name }}/resourcePools/{{
      resource_pool_name }}

'''

RETURN = '''
virtual_networks_by_pc:
  description: >-
    A list of dict results where the key is the name of the VirtualNetworksByPC
    and the values are the facts for that VirtualNetworksByPC.
  returned: always
  type: complex
  contains:
    virtualnetworksbypc_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - Link for next list of VirtualNetwork
          returned: always
          type: str
          sample: null
        value:
          description:
            - Results of the VirtualNetwork list
          returned: always
          type: dict
          sample: null
          contains:
            assignable:
              description:
                - can be used in vm creation/deletion
              returned: always
              type: boolean
              sample: null
            id:
              description:
                - 'virtual network id (privateCloudId:vsphereId)'
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
                - '{VirtualNetworkName}'
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Virtual Network properties
              returned: always
              type: dict
              sample: null
            private_cloud_id:
              description:
                - The Private Cloud id
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


class AzureRMVirtualNetworksByPCInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=true
            ),
            pc_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='raw',
                required=true,
                pattern=('//subscriptions/{{ subscription_id }}/providers'
                         '/Microsoft.VMwareCloudSimple/locations/{{ location_name }}'
                         '/privateClouds/{{ private_cloud_name }}/resourcePools/{{ name }}')
            )
        )

        self.region_id = None
        self.pc_name = None
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
        super(AzureRMVirtualNetworksByPCInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.pc_name is not None and
            self.name is not None):
            self.results['virtual_networks_by_pc'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_networks_by_pc.list(region_id=self.region_id,
                                                                    pc_name=self.pc_name,
                                                                    resource_pool_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMVirtualNetworksByPCInfo()


if __name__ == '__main__':
    main()
