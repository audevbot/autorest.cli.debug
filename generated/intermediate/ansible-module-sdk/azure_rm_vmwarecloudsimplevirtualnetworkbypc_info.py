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
module: azure_rm_vmwarecloudsimplevirtualnetworkbypc_info
version_added: '2.9'
short_description: Get VirtualNetworkByPC info.
description:
  - Get info of VirtualNetworkByPC.
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
      - '{VirtualNetworkName}'
    type: str
  assignable:
    description:
      - can be used in vm creation/deletion
    type: boolean
  id:
    description:
      - 'virtual network id (privateCloudId:vsphereId)'
    type: str
  location:
    description:
      - Azure region
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
- name: GetVirtualNetwork
  azure_rm_vmwarecloudsimplevirtualnetworkbypc_info:
    region_id: myLocation
    pc_name: myPrivateCloud
    name: myVirtualNetwork

'''

RETURN = '''
virtual_network_by_pc:
  description: >-
    A list of dict results where the key is the name of the VirtualNetworkByPC
    and the values are the facts for that VirtualNetworkByPC.
  returned: always
  type: complex
  contains:
    virtualnetworkbypc_name:
      description: The key is the name of the server that the values relate to.
      type: complex
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


class AzureRMVirtualNetworkByPCInfo(AzureRMModuleBase):
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
                type='str',
                required=true
            )
        )

        self.region_id = None
        self.pc_name = None
        self.name = None
        self.assignable = None
        self.id = None
        self.location = None
        self.name = None
        self.properties = None
        self.type = None

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
        super(AzureRMVirtualNetworkByPCInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.pc_name is not None and
            self.name is not None):
            self.results['virtual_network_by_pc'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_network_by_pc.get(region_id=self.region_id,
                                                                  pc_name=self.pc_name,
                                                                  virtual_network_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMVirtualNetworkByPCInfo()


if __name__ == '__main__':
    main()
