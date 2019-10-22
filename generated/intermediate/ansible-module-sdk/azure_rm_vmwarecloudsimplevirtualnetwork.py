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
module: azure_rm_vmwarecloudsimplevirtualnetwork
version_added: '2.9'
short_description: Manage Azure VirtualNetwork instance.
description:
  - 'Create, update and delete instance of Azure VirtualNetwork.'
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
    required: true
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
  state:
    description:
      - Assert the state of the VirtualNetwork.
      - >-
        Use C(present) to create or update an VirtualNetwork and C(absent) to
        delete it.
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
[]

'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualNetworks(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            pc_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='resource_pool_name',
                required=true
            ),
            private_cloud_id=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualNetworks, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

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
           self.results["assignable"] = response["assignable"]
           self.results["id"] = response["id"]
           self.results["location"] = response["location"]
           self.results["name"] = response["name"]
           self.results["properties"] = response["properties"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.virtual_networks.create()
            else:
                response = self.mgmt_client.virtual_networks.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualNetwork instance.')
            self.fail('Error creating the VirtualNetwork instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the VirtualNetwork instance {0}'.format(self.))
        try:
            response = self.mgmt_client.virtual_networks.delete()
        except CloudError as e:
            self.log('Error attempting to delete the VirtualNetwork instance.')
            self.fail('Error deleting the VirtualNetwork instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the VirtualNetwork instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.virtual_networks.get(region_id=self.region_id,
                                                             pc_name=self.pc_name,
                                                             virtual_network_name=self.virtualNetworkName)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualNetworks()


if __name__ == '__main__':
    main()
