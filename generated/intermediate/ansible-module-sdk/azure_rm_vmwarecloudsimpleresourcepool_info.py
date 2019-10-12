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
module: azure_rm_vmwarecloudsimpleresourcepool_info
version_added: '2.9'
short_description: Get ResourcePool info.
description:
  - Get info of ResourcePool.
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
      - '{ResourcePoolName}'
    type: str
  id:
    description:
      - 'resource pool id (privateCloudId:vsphereId)'
    type: str
  location:
    description:
      - Azure region
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
  azure_rm_vmwarecloudsimpleresourcepool_info:
    region_id: myLocation
    pc_name: myPrivateCloud
- name: GetResourcePool
  azure_rm_vmwarecloudsimpleresourcepool_info:
    region_id: myLocation
    pc_name: myPrivateCloud
    name: myResourcePool

'''

RETURN = '''
resource_pools:
  description: >-
    A list of dict results where the key is the name of the ResourcePool and the
    values are the facts for that ResourcePool.
  returned: always
  type: complex
  contains:
    resourcepool_name:
      description: The key is the name of the server that the values relate to.
      type: complex
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


class AzureRMResourcePoolsInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.region_id = None
        self.pc_name = None
        self.name = None
        self.id = None
        self.location = None
        self.name = None
        self.private_cloud_id = None
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
        super(AzureRMResourcePoolsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.pc_name is not None and
            self.name is not None):
            self.results['resource_pools'] = self.format_item(self.get())
        elif (self.region_id is not None and
              self.pc_name is not None):
            self.results['resource_pools'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.resource_pools.get(region_id=self.region_id,
                                                           pc_name=self.pc_name,
                                                           resource_pool_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.resource_pools.list(region_id=self.region_id,
                                                            pc_name=self.pc_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMResourcePoolsInfo()


if __name__ == '__main__':
    main()
