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
module: azure_rm_apimanagementapirelease
version_added: '2.9'
short_description: Manage Azure ApiRelease instance.
description:
  - 'Create, update and delete instance of Azure ApiRelease.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  api_id:
    description:
      - Identifier of the API the release belongs to.
    type: str
  release_id:
    description:
      - >-
        Release identifier within an API. Must be unique in the current API
        Management service instance.
    required: true
    type: str
  notes:
    description:
      - Release Notes
    type: str
  created_date_time:
    description:
      - >-
        The time the API was released. The date conforms to the following
        format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard.
    type: datetime
  updated_date_time:
    description:
      - The time the API release was updated.
    type: datetime
  id:
    description:
      - Resource ID.
    type: str
  name:
    description:
      - Resource name.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the ApiRelease.
      - >-
        Use C(present) to create or update an ApiRelease and C(absent) to delete
        it.
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
- name: ApiManagementCreateApiRelease
  azure_rm_apimanagementapirelease:
    resource_group: myResourceGroup
    service_name: myService
    api_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{
      api_name }}
    release_id: myRelease
    notes: yahooagain
- name: ApiManagementUpdateApiRelease
  azure_rm_apimanagementapirelease:
    resource_group: myResourceGroup
    service_name: myService
    api_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{
      api_name }}
    release_id: myRelease
    notes: yahooagain
- name: ApiManagementDeleteApiRelease
  azure_rm_apimanagementapirelease:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    release_id: myRelease
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
    - ApiRelease entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    api_id:
      description:
        - Identifier of the API the release belongs to.
      returned: always
      type: str
      sample: null
    created_date_time:
      description:
        - >-
          The time the API was released. The date conforms to the following
          format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard.
      returned: always
      type: datetime
      sample: null
    updated_date_time:
      description:
        - The time the API release was updated.
      returned: always
      type: datetime
      sample: null
    notes:
      description:
        - Release Notes
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


class AzureRMApiRelease(AzureRMModuleBaseExt):
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
            api_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            release_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            api_id=dict(
                type='raw',
                disposition='/',
                pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                         '/{{ resource_group }}/providers/Microsoft.ApiManagement/service'
                         '/{{ service_name }}/apis/{{ name }}')
            ),
            notes=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.release_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApiRelease, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.api_release.create_or_update(resource_group_name=self.resource_group,
                                                                     service_name=self.service_name,
                                                                     api_id=self.api_id,
                                                                     release_id=self.release_id,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ApiRelease instance.')
            self.fail('Error creating the ApiRelease instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ApiRelease instance {0}'.format(self.))
        try:
            response = self.mgmt_client.api_release.delete(resource_group_name=self.resource_group,
                                                           service_name=self.service_name,
                                                           api_id=self.api_id,
                                                           release_id=self.release_id)
        except CloudError as e:
            self.log('Error attempting to delete the ApiRelease instance.')
            self.fail('Error deleting the ApiRelease instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiRelease instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.api_release.get(resource_group_name=self.resource_group,
                                                        service_name=self.service_name,
                                                        api_id=self.api_id,
                                                        release_id=self.release_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApiRelease()


if __name__ == '__main__':
    main()
