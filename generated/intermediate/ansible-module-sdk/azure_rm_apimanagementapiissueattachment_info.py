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
module: azure_rm_apimanagementapiissueattachment_info
version_added: '2.9'
short_description: Get ApiIssueAttachment info.
description:
  - Get info of ApiIssueAttachment.
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
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
    required: true
  issue_id:
    description:
      - >-
        Issue identifier. Must be unique in the current API Management service
        instance.
    required: true
  attachment_id:
    description:
      - >-
        Attachment identifier within an Issue. Must be unique in the current
        Issue.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  title:
    description:
      - Filename by which the binary data will be saved.
    required: true
  content_format:
    description:
      - >-
        Either 'link' if content is provided via an HTTP link or the MIME type
        of the Base64-encoded binary data provided in the 'content' property.
    required: true
  content:
    description:
      - An HTTP link or Base64-encoded binary data.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiIssueAttachments
  azure_rm_apimanagementapiissueattachment_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    issue_id: myIssue
- name: ApiManagementGetApiIssueAttachment
  azure_rm_apimanagementapiissueattachment_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    issue_id: myIssue
    attachment_id: myAttachment

'''

RETURN = '''
api_issue_attachment:
  description: >-
    A list of dict results where the key is the name of the ApiIssueAttachment
    and the values are the facts for that ApiIssueAttachment.
  returned: always
  type: complex
  contains:
    apiissueattachment_name:
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
            - Properties of the Issue Attachment.
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


class AzureRMApiIssueAttachmentInfo(AzureRMModuleBase):
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
            issue_id=dict(
                type='str',
                required=true
            ),
            attachment_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.api_id = None
        self.issue_id = None
        self.attachment_id = None
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
        super(AzureRMApiIssueAttachmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.api_id is not None and
            self.issue_id is not None and
            self.attachment_id is not None):
            self.results['api_issue_attachment'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None and
              self.api_id is not None and
              self.issue_id is not None):
            self.results['api_issue_attachment'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_issue_attachment.get(resource_group_name=self.resource_group,
                                                                 service_name=self.name,
                                                                 api_id=self.api_id,
                                                                 issue_id=self.issue_id,
                                                                 attachment_id=self.attachment_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.api_issue_attachment.list_by_service(resource_group_name=self.resource_group,
                                                                             service_name=self.name,
                                                                             api_id=self.api_id,
                                                                             issue_id=self.issue_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiIssueAttachmentInfo()


if __name__ == '__main__':
    main()
