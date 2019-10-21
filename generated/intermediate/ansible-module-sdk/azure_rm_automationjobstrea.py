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
module: azure_rm_automationjobstrea
version_added: '2.9'
short_description: Manage Azure JobStream instance.
description:
  - 'Create, update and delete instance of Azure JobStream.'
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
  name:
    description:
      - The job name.
    required: true
    type: str
  client_request_id:
    description:
      - Identifies this specific client request.
    type: str
  id:
    description:
      - Gets or sets the id of the resource.
    type: str
  job_stream_id:
    description:
      - Gets or sets the id of the job stream.
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
  state:
    description:
      - Assert the state of the JobStream.
      - >-
        Use C(present) to create or update an JobStream and C(absent) to delete
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
[]

'''

RETURN = '''
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


class AzureRMJobStream(AzureRMModuleBaseExt):
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
            name=dict(
                type='str',
                updatable=False,
                disposition='job_name',
                required=true
            ),
            client_request_id=dict(
                type='str',
                updatable=False
            ),
            job_stream_id=dict(
                type='str',
                disposition='/'
            ),
            time=dict(
                type='datetime',
                disposition='/'
            ),
            stream_type=dict(
                type='str',
                disposition='/',
                choices=['Progress',
                         'Output',
                         'Warning',
                         'Error',
                         'Debug',
                         'Verbose',
                         'Any']
            ),
            stream_text=dict(
                type='str',
                disposition='/'
            ),
            summary=dict(
                type='str',
                disposition='/'
            ),
            value=dict(
                type='unknown[DictionaryType {"$id":"46","$type":"DictionaryType","valueType":{"$id":"47","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"48","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"49","fixed":false},"deprecated":false}]',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.automation_account_name = None
        self.name = None
        self.client_request_id = None
        self.id = None
        self.properties = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMJobStream, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.job_stream.create()
            else:
                response = self.mgmt_client.job_stream.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the JobStream instance.')
            self.fail('Error creating the JobStream instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the JobStream instance {0}'.format(self.))
        try:
            response = self.mgmt_client.job_stream.delete()
        except CloudError as e:
            self.log('Error attempting to delete the JobStream instance.')
            self.fail('Error deleting the JobStream instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the JobStream instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.job_stream.get(resource_group_name=self.resource_group,
                                                       automation_account_name=self.automation_account_name,
                                                       job_name=self.name,
                                                       job_stream_id=self.job_stream_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMJobStream()


if __name__ == '__main__':
    main()
