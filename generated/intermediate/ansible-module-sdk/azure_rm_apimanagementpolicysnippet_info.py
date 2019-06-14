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
module: azure_rm_apimanagementpolicysnippet_info
version_added: '2.9'
short_description: Get PolicySnippet info.
description:
  - Get info of PolicySnippet.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - The name of the API Management service.
    required: true
  scope:
    description:
      - Policy scope.
    required: true
  value:
    description:
      - Policy snippet value.
    type: list
    suboptions:
      name:
        description:
          - Snippet name.
      content:
        description:
          - Snippet content.
      tool_tip:
        description:
          - Snippet toolTip.
      scope:
        description:
          - Binary OR value of the Snippet scope.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListPolicySnippets
  azure_rm_apimanagementpolicysnippet_info:
    resource_group: myResourceGroup
    name: myService
    scope: Api

'''

RETURN = '''
policy_snippet:
  description: >-
    A list of dict results where the key is the name of the PolicySnippet and
    the values are the facts for that PolicySnippet.
  returned: always
  type: complex
  contains:
    policysnippet_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPolicySnippetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            ),
            scope=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.scope = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPolicySnippetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['policy_snippet'] = self.format_item(self.listbyservice())
        return self.results

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.policy_snippet.list_by_service(resource_group_name=self.resource_group,
                                                                       service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMPolicySnippetInfo()


if __name__ == '__main__':
    main()
