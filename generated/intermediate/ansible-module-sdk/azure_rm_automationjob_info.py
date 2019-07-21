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
module: azure_rm_automationjob_info
version_added: '2.9'
short_description: Get Job info.
description:
  - Get info of Job.
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
  client_request_id:
    description:
      - Identifies this specific client request.
    required: true
    type: str
  name:
    description:
      - The name of the resource
    type: str
  id:
    description:
      - Fully qualified resource Id for the resource
    type: str
  type:
    description:
      - The type of the resource.
    type: str
  runbook:
    description:
      - Gets or sets the runbook.
    type: dict
    suboptions:
      name:
        description:
          - Gets or sets the name of the runbook.
        type: str
  started_by:
    description:
      - Gets or sets the job started by.
    type: str
  run_on:
    description:
      - >-
        Gets or sets the runOn which specifies the group name where the job is
        to be executed.
    type: str
  job_id:
    description:
      - Gets or sets the id of the job.
    type: 'unknown-primary[uuid]'
  creation_time:
    description:
      - Gets or sets the creation time of the job.
    type: datetime
  status:
    description:
      - Gets or sets the status of the job.
    type: str
  status_details:
    description:
      - Gets or sets the status details of the job.
    type: str
  start_time:
    description:
      - Gets or sets the start time of the job.
    type: datetime
  end_time:
    description:
      - Gets or sets the end time of the job.
    type: datetime
  exception:
    description:
      - Gets or sets the exception of the job.
    type: str
  last_modified_time:
    description:
      - Gets or sets the last modified time of the job.
    type: datetime
  last_status_modified_time:
    description:
      - Gets or sets the last status modified time of the job.
    type: datetime
  parameters:
    description:
      - Gets or sets the parameters of the job.
    type: >-
      unknown[DictionaryType
      {"$id":"175","$type":"DictionaryType","valueType":{"$id":"176","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"177","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"178","fixed":false},"deprecated":false}]
  provisioning_state:
    description:
      - The current provisioning state of the job.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List jobs by automation account
  azure_rm_automationjob_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: foo
- name: Get job
  azure_rm_automationjob_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: myJob
- name: Get Job Output
  azure_rm_automationjob_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: myJob
- name: Get Job Runbook Content
  azure_rm_automationjob_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: myJob

'''

RETURN = '''
job:
  description: >-
    A list of dict results where the key is the name of the Job and the values
    are the facts for that Job.
  returned: always
  type: complex
  contains:
    job_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Fully qualified resource Id for the resource
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the resource
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The properties of the job.
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


class AzureRMJobInfo(AzureRMModuleBase):
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
            client_request_id=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.automation_account_name = None
        self.client_request_id = None
        self.name = None
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
        self.query_parameters['api-version'] = '2017-05-15-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMJobInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AutomationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.automation_account_name is not None and
            self.name is not None):
            self.results['job'] = self.format_item(self.getrunbookcontent())
        elif (self.resource_group is not None and
              self.automation_account_name is not None and
              self.name is not None):
            self.results['job'] = self.format_item(self.getoutput())
        elif (self.resource_group is not None and
              self.automation_account_name is not None and
              self.name is not None):
            self.results['job'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.automation_account_name is not None):
            self.results['job'] = self.format_item(self.listbyautomationaccount())
        return self.results

    def getrunbookcontent(self):
        response = None

        try:
            response = self.mgmt_client.job.get_runbook_content(resource_group_name=self.resource_group,
                                                                automation_account_name=self.automation_account_name,
                                                                job_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getoutput(self):
        response = None

        try:
            response = self.mgmt_client.job.get_output(resource_group_name=self.resource_group,
                                                       automation_account_name=self.automation_account_name,
                                                       job_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.job.get(resource_group_name=self.resource_group,
                                                automation_account_name=self.automation_account_name,
                                                job_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyautomationaccount(self):
        response = None

        try:
            response = self.mgmt_client.job.list_by_automation_account(resource_group_name=self.resource_group,
                                                                       automation_account_name=self.automation_account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMJobInfo()


if __name__ == '__main__':
    main()
