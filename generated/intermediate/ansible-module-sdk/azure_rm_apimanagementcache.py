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
module: azure_rm_apimanagementcache
version_added: '2.9'
short_description: Manage Azure Cache instance.
description:
  - 'Create, update and delete instance of Azure Cache.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  cache_id:
    description:
      - >-
        Identifier of the Cache entity. Cache identifier (should be either
        'default' or valid Azure region identifier).
    required: true
  description:
    description:
      - Cache description
  connection_string:
    description:
      - Runtime connection string to cache
    required: true
  resource_id:
    description:
      - Original uri of entity in external system cache points to
  id:
    description:
      - Resource ID.
  name:
    description:
      - Resource name.
  type:
    description:
      - Resource type for API Management resource.
  state:
    description:
      - Assert the state of the Cache.
      - Use C(present) to create or update an Cache and C(absent) to delete it.
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
- name: ApiManagementCreateCache
  azure_rm_apimanagementcache:
    resource_group: myResourceGroup
    service_name: myService
    cache_id: myCache
    description: Redis cache instances in West India
    connection_string: 'contoso5.redis.cache.windows.net,ssl=true,password=...'
    resource_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.Cache/Redis/{{ redis_name }}
- name: ApiManagementUpdateCache
  azure_rm_apimanagementcache:
    resource_group: myResourceGroup
    service_name: myService
    cache_id: myCache
    description: Update Cache in west India
- name: ApiManagementDeleteCache
  azure_rm_apimanagementcache:
    resource_group: myResourceGroup
    service_name: myService
    cache_id: myCache
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Cache properties details.
  returned: always
  type: dict
  sample: null
  contains:
    description:
      description:
        - Cache description
      returned: always
      type: str
      sample: null
    connection_string:
      description:
        - Runtime connection string to cache
      returned: always
      type: str
      sample: null
    resource_id:
      description:
        - Original uri of entity in external system cache points to
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMCache(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            cache_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            connection_string=dict(
                type='str',
                disposition='/',
                required=true
            ),
            resource_id=dict(
                type='raw',
                disposition='/',
                pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                         '/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ name }}')
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.cache_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMCache, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClient,
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
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.cache.create_or_update(resource_group_name=self.resource_group,
                                                               service_name=self.service_name,
                                                               cache_id=self.cache_id,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Cache instance.')
            self.fail('Error creating the Cache instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Cache instance {0}'.format(self.))
        try:
            response = self.mgmt_client.cache.delete(resource_group_name=self.resource_group,
                                                     service_name=self.service_name,
                                                     cache_id=self.cache_id)
        except CloudError as e:
            self.log('Error attempting to delete the Cache instance.')
            self.fail('Error deleting the Cache instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Cache instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.cache.get(resource_group_name=self.resource_group,
                                                  service_name=self.service_name,
                                                  cache_id=self.cache_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMCache()


if __name__ == '__main__':
    main()
