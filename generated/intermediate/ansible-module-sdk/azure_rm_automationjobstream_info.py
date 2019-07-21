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
module: azure_rm_automationjobstream_info
version_added: '2.9'
short_description: Get JobStream info.
description:
  - Get info of JobStream.
options:
  resource_group:
    description:
      - Name of an Azure Resource group.
    required: true
    type: str
  automation_account_name:
    description:
      - The name of the automation account.
    required: true
    type: str
  job_name:
    description:
      - The job name.
    required: true
    type: str
  client_request_id:
    description:
      - Identifies this specific client request.
    required: true
    type: str
  job_stream_id:
    description:
      - Gets or sets the id of the job stream.
    type: str
  id:
    description:
      - Gets or sets the id of the resource.
    type: str
  time:
    description:
      - Gets or sets the creation time of the job.
    type: datetime
  stream_type:
    description:
      - Gets or sets the stream type.
    type: str
  stream_text:
    description:
      - Gets or sets the stream text.
    type: str
  summary:
    description:
      - Gets or sets the summary.
    type: str
  value:
    description:
      - Gets or sets the values of the job stream.
    type: >-
      unknown[DictionaryType
      {"$id":"46","$type":"DictionaryType","valueType":{"$id":"47","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"48","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"49","fixed":false},"deprecated":false}]
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List job streams by job name
  azure_rm_automationjobstream_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    job_name: myJob
- name: Get job stream
  azure_rm_automationjobstream_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    job_name: myJob
    job_stream_id: myStream

'''

RETURN = '''
job_stream:
  description: >-
    A list of dict results where the key is the name of the JobStream and the
    values are the facts for that JobStream.
  returned: always
  type: complex
  contains:
    jobstream_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Gets or sets the id of the resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Gets or sets the id of the job stream.
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
    from azure.mgmt.automation import AutomationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMJobStreamInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            automation_account_name=dict(
                type='str',
                required=true
            ),
            job_name=dict(
                type='str',
                required=true
            ),
            client_request_id=dict(
                type='str',
                required=true
            ),
            job_stream_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.automation_account_name = None
        self.job_name = None
        self.client_request_id = None
        self.job_stream_id = None
        self.id = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-05-15-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMJobStreamInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AutomationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.automation_account_name is not None and
            self.job_name is not None and
            self.job_stream_id is not None):
            self.results['job_stream'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.automation_account_name is not None and
              self.job_name is not None):
            self.results['job_stream'] = self.format_item(self.listbyjob())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job_stream.get(resource_group_name=self.resource_group,
                                                       automation_account_name=self.automation_account_name,
                                                       job_name=self.job_name,
                                                       job_stream_id=self.job_stream_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyjob(self):
        response = None

        try:
            response = self.mgmt_client.job_stream.list_by_job(resource_group_name=self.resource_group,
                                                               automation_account_name=self.automation_account_name,
                                                               job_name=self.job_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMJobStreamInfo()


if __name__ == '__main__':
    main()
