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
module: azure_rm_apimanagementapiissueattachmen
version_added: '2.9'
short_description: Manage Azure ApiIssueAttachment instance.
description:
  - 'Create, update and delete instance of Azure ApiIssueAttachment.'
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
  attachment_id:
    description:
      - >-
        Attachment identifier within an Issue. Must be unique in the current
        Issue.
    required: true
    type: str
  title:
    description:
      - Filename by which the binary data will be saved.
    required: true
    type: str
  content_format:
    description:
      - >-
        Either 'link' if content is provided via an HTTP link or the MIME type
        of the Base64-encoded binary data provided in the 'content' property.
    required: true
    type: str
  content:
    description:
      - An HTTP link or Base64-encoded binary data.
    required: true
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
  state:
    description:
      - Assert the state of the ApiIssueAttachment.
      - >-
        Use C(present) to create or update an ApiIssueAttachment and C(absent)
        to delete it.
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
- name: ApiManagementCreateApiIssueAttachment
  azure_rm_apimanagementapiissueattachmen:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    issue_id: myIssue
    attachment_id: myAttachment
    title: Issue attachment.
    content_format: image/jpeg
    content: IEJhc2U2NA==
- name: ApiManagementDeleteApiIssueAttachment
  azure_rm_apimanagementapiissueattachmen:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    issue_id: myIssue
    attachment_id: myAttachment
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
    - Properties of the Issue Attachment.
  returned: always
  type: dict
  sample: null
  contains:
    title:
      description:
        - Filename by which the binary data will be saved.
      returned: always
      type: str
      sample: null
    content_format:
      description:
        - >-
          Either 'link' if content is provided via an HTTP link or the MIME type
          of the Base64-encoded binary data provided in the 'content' property.
      returned: always
      type: str
      sample: null
    content:
      description:
        - An HTTP link or Base64-encoded binary data.
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


class AzureRMApiIssueAttachment(AzureRMModuleBaseExt):
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
            issue_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            attachment_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            title=dict(
                type='str',
                disposition='/',
                required=true
            ),
            content_format=dict(
                type='str',
                disposition='/',
                required=true
            ),
            content=dict(
                type='str',
                disposition='/',
                required=true
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
        self.issue_id = None
        self.attachment_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApiIssueAttachment, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.api_issue_attachment.create_or_update(resource_group_name=self.resource_group,
                                                                              service_name=self.service_name,
                                                                              api_id=self.api_id,
                                                                              issue_id=self.issue_id,
                                                                              attachment_id=self.attachment_id,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ApiIssueAttachment instance.')
            self.fail('Error creating the ApiIssueAttachment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ApiIssueAttachment instance {0}'.format(self.))
        try:
            response = self.mgmt_client.api_issue_attachment.delete(resource_group_name=self.resource_group,
                                                                    service_name=self.service_name,
                                                                    api_id=self.api_id,
                                                                    issue_id=self.issue_id,
                                                                    attachment_id=self.attachment_id)
        except CloudError as e:
            self.log('Error attempting to delete the ApiIssueAttachment instance.')
            self.fail('Error deleting the ApiIssueAttachment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiIssueAttachment instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.api_issue_attachment.get(resource_group_name=self.resource_group,
                                                                 service_name=self.service_name,
                                                                 api_id=self.api_id,
                                                                 issue_id=self.issue_id,
                                                                 attachment_id=self.attachment_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApiIssueAttachment()


if __name__ == '__main__':
    main()
