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
module: azure_rm_apimanagementapiissuecomment_info
version_added: '2.9'
short_description: Get ApiIssueComment info.
description:
  - Get info of ApiIssueComment.
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
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  issue_id:
    description:
      - >-
        Issue identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  comment_id:
    description:
      - Comment identifier within an Issue. Must be unique in the current Issue.
    type: str
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
  text:
    description:
      - Comment text.
    required: true
    type: str
  created_date:
    description:
      - Date and time when the comment was created.
    type: datetime
  user_id:
    description:
      - A resource identifier for the user who left the comment.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiIssueComments
  azure_rm_apimanagementapiissuecomment_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    issue_id: myIssue
- name: ApiManagementGetApiIssueComment
  azure_rm_apimanagementapiissuecomment_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    issue_id: myIssue
    comment_id: myComment

'''

RETURN = '''
api_issue_comment:
  description: >-
    A list of dict results where the key is the name of the ApiIssueComment and
    the values are the facts for that ApiIssueComment.
  returned: always
  type: complex
  contains:
    apiissuecomment_name:
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
            - Properties of the Issue Comment.
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


class AzureRMApiIssueCommentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            service_name=dict(
                type='str',
                required=true
            ),
            api_id=dict(
                type='str',
                required=true
            ),
            issue_id=dict(
                type='str',
                required=true
            ),
            comment_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.issue_id = None
        self.comment_id = None
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
        super(AzureRMApiIssueCommentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None and
            self.issue_id is not None and
            self.comment_id is not None):
            self.results['api_issue_comment'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None and
              self.issue_id is not None):
            self.results['api_issue_comment'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_issue_comment.get(resource_group_name=self.resource_group,
                                                              service_name=self.service_name,
                                                              api_id=self.api_id,
                                                              issue_id=self.issue_id,
                                                              comment_id=self.comment_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.api_issue_comment.list_by_service(resource_group_name=self.resource_group,
                                                                          service_name=self.service_name,
                                                                          api_id=self.api_id,
                                                                          issue_id=self.issue_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiIssueCommentInfo()


if __name__ == '__main__':
    main()
