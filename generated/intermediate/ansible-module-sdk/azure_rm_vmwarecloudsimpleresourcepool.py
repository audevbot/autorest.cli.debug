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
module: azure_rm_vmwarecloudsimpleresourcepool
version_added: '2.9'
short_description: Manage Azure ResourcePool instance.
description:
  - 'Create, update and delete instance of Azure ResourcePool.'
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  name:
    description:
      - '{ResourcePoolName}'
    type: str
  id:
    description:
      - 'resource pool id (privateCloudId:vsphereId)'
    required: true
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
  state:
    description:
      - Assert the state of the ResourcePool.
      - >-
        Use C(present) to create or update an ResourcePool and C(absent) to
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


class AzureRMResourcePools(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='pc_name',
                required=true
            ),
            full_name=dict(
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
        self.name = None
        self.id = None
        self.location = None
        self.name = None
        self.private_cloud_id = None
        self.properties = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMResourcePools, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["id"] = response["id"]
           self.results["location"] = response["location"]
           self.results["name"] = response["name"]
           self.results["private_cloud_id"] = response["private_cloud_id"]
           self.results["properties"] = response["properties"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.resource_pools.create()
            else:
                response = self.mgmt_client.resource_pools.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ResourcePool instance.')
            self.fail('Error creating the ResourcePool instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ResourcePool instance {0}'.format(self.))
        try:
            response = self.mgmt_client.resource_pools.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ResourcePool instance.')
            self.fail('Error deleting the ResourcePool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ResourcePool instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.resource_pools.get(region_id=self.region_id,
                                                           pc_name=self.name,
                                                           resource_pool_name=self.resourcePoolName)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMResourcePools()


if __name__ == '__main__':
    main()
