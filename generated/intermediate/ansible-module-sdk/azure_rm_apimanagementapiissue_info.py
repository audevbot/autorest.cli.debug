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
module: azure_rm_apimanagementapiissue_info
version_added: '2.9'
short_description: Get ApiIssue info.
description:
  - Get info of ApiIssue.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  api_id:
    description:
      - A resource identifier for the API the issue was created for.
  expand_comments_attachments:
    description:
      - 'Expand the comment attachments. '
    required: true
  issue_id:
    description:
      - >-
        Issue identifier. Must be unique in the current API Management service
        instance.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  created_date:
    description:
      - Date and time when the issue was created.
  state:
    description:
      - Status of the issue.
  title:
    description:
      - The issue title.
    required: true
  description:
    description:
      - Text describing the issue.
    required: true
  user_id:
    description:
      - A resource identifier for the user created the issue.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiIssues
  azure_rm_apimanagementapiissue_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApi
- name: ApiManagementGetApiIssue
  azure_rm_apimanagementapiissue_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApi
    issue_id: myIssue

'''

RETURN = '''
api_issue:
  description: >-
    A list of dict results where the key is the name of the ApiIssue and the
    values are the facts for that ApiIssue.
  returned: always
  type: complex
  contains:
    apiissue_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
            - Properties of the Issue.
          returned: always
          type: dict
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


class AzureRMApiIssueInfo(AzureRMModuleBase):
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
            api_id=dict(
                type='str',
                required=true
            ),
            expand_comments_attachments=dict(
                type='boolean',
                required=true
            ),
            issue_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.api_id = None
        self.expand_comments_attachments = None
        self.issue_id = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None

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
        super(AzureRMApiIssueInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.api_id is not None and
            self.issue_id is not None):
            self.results['api_issue'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None and
              self.api_id is not None):
            self.results['api_issue'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_issue.get(resource_group_name=self.resource_group,
                                                      service_name=self.name,
                                                      api_id=self.api_id,
                                                      issue_id=self.issue_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.api_issue.list_by_service(resource_group_name=self.resource_group,
                                                                  service_name=self.name,
                                                                  api_id=self.api_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiIssueInfo()


if __name__ == '__main__':
    main()
