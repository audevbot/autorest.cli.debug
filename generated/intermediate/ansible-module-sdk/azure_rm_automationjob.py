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
module: azure_rm_automationjob
version_added: '2.9'
short_description: Manage Azure Job instance.
description:
  - 'Create, update and delete instance of Azure Job.'
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
  runbook:
    description:
      - Gets or sets the runbook.
    type: dict
    suboptions:
      name:
        description:
          - Gets or sets the name of the runbook.
        type: str
  parameters:
    description:
      - Gets or sets the parameters of the job.
    type: >-
      unknown[DictionaryType
      {"$id":"301","$type":"DictionaryType","valueType":{"$id":"302","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"303","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"304","fixed":false},"deprecated":false}]
  run_on:
    description:
      - >-
        Gets or sets the runOn which specifies the group name where the job is
        to be executed.
    type: str
  started_by:
    description:
      - Gets or sets the job started by.
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
  provisioning_state:
    description:
      - The current provisioning state of the job.
    type: str
  client_request_id:
    description:
      - Identifies this specific client request.
    type: str
  id:
    description:
      - Fully qualified resource Id for the resource
    type: str
  name:
    description:
      - The name of the resource
    type: str
  type:
    description:
      - The type of the resource.
    type: str
  state:
    description:
      - Assert the state of the Job.
      - Use C(present) to create or update an Job and C(absent) to delete it.
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
- name: Create job
  azure_rm_automationjob:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    job_name: myJob
    runbook:
      name: TestRunbook
    run_on: ''

'''

RETURN = '''
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
  contains:
    runbook:
      description:
        - Gets or sets the runbook.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Gets or sets the name of the runbook.
          returned: always
          type: str
          sample: null
    started_by:
      description:
        - Gets or sets the job started by.
      returned: always
      type: str
      sample: null
    run_on:
      description:
        - >-
          Gets or sets the runOn which specifies the group name where the job is
          to be executed.
      returned: always
      type: str
      sample: null
    job_id:
      description:
        - Gets or sets the id of the job.
      returned: always
      type: 'unknown-primary[uuid]'
      sample: null
    creation_time:
      description:
        - Gets or sets the creation time of the job.
      returned: always
      type: datetime
      sample: null
    status:
      description:
        - Gets or sets the status of the job.
      returned: always
      type: str
      sample: null
    status_details:
      description:
        - Gets or sets the status details of the job.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - Gets or sets the start time of the job.
      returned: always
      type: datetime
      sample: null
    end_time:
      description:
        - Gets or sets the end time of the job.
      returned: always
      type: datetime
      sample: null
    exception:
      description:
        - Gets or sets the exception of the job.
      returned: always
      type: str
      sample: null
    last_modified_time:
      description:
        - Gets or sets the last modified time of the job.
      returned: always
      type: datetime
      sample: null
    last_status_modified_time:
      description:
        - Gets or sets the last status modified time of the job.
      returned: always
      type: datetime
      sample: null
    parameters:
      description:
        - Gets or sets the parameters of the job.
      returned: always
      type: >-
        unknown[DictionaryType
        {"$id":"175","$type":"DictionaryType","valueType":{"$id":"176","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"177","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"178","fixed":false},"deprecated":false}]
      sample: null
    provisioning_state:
      description:
        - The current provisioning state of the job.
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
    from azure.mgmt.automation import AutomationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMJob(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            automation_account_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            job_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            runbook=dict(
                type='dict',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str'
                    )
                )
            ),
            parameters=dict(
                type='unknown[DictionaryType {"$id":"301","$type":"DictionaryType","valueType":{"$id":"302","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"303","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"304","fixed":false},"deprecated":false}]',
                disposition='/'
            ),
            run_on=dict(
                type='str',
                disposition='/'
            ),
            client_request_id=dict(
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
        self.automation_account_name = None
        self.job_name = None
        self.client_request_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJob, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AutomationManagement,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.job.create(resource_group_name=self.resource_group,
                                                       automation_account_name=self.automation_account_name,
                                                       job_name=self.job_name,
                                                       parameters=self.body)
            else:
                response = self.mgmt_client.job.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Job instance.')
            self.fail('Error creating the Job instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Job instance {0}'.format(self.))
        try:
            response = self.mgmt_client.job.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Job instance.')
            self.fail('Error deleting the Job instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Job instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.job.get(resource_group_name=self.resource_group,
                                                automation_account_name=self.automation_account_name,
                                                job_name=self.job_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJob()


if __name__ == '__main__':
    main()
