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
module: azure_rm_apimanagementpolicysnippet
version_added: '2.9'
short_description: Manage Azure PolicySnippet instance.
description:
  - 'Create, update and delete instance of Azure PolicySnippet.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  scope:
    description:
      - Policy scope.
    type: str
  value:
    description:
      - Policy snippet value.
    type: list
    suboptions:
      name:
        description:
          - Snippet name.
        type: str
      content:
        description:
          - Snippet content.
        type: str
      tool_tip:
        description:
          - Snippet toolTip.
        type: str
      scope:
        description:
          - Binary OR value of the Snippet scope.
        type: number
  state:
    description:
      - Assert the state of the PolicySnippet.
      - >-
        Use C(present) to create or update an PolicySnippet and C(absent) to
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
value:
  description:
    - Policy snippet value.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Snippet name.
      returned: always
      type: str
      sample: null
    content:
      description:
        - Snippet content.
      returned: always
      type: str
      sample: null
    tool_tip:
      description:
        - Snippet toolTip.
      returned: always
      type: str
      sample: null
    scope:
      description:
        - Binary OR value of the Snippet scope.
      returned: always
      type: number
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


class AzureRMPolicySnippet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='service_name',
                required=true
            ),
            scope=dict(
                type='str',
                updatable=False
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.scope = None
        self.value = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPolicySnippet, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.policy_snippet.create()
            else:
                response = self.mgmt_client.policy_snippet.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PolicySnippet instance.')
            self.fail('Error creating the PolicySnippet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the PolicySnippet instance {0}'.format(self.))
        try:
            response = self.mgmt_client.policy_snippet.delete()
        except CloudError as e:
            self.log('Error attempting to delete the PolicySnippet instance.')
            self.fail('Error deleting the PolicySnippet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the PolicySnippet instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.policy_snippet.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPolicySnippet()


if __name__ == '__main__':
    main()
