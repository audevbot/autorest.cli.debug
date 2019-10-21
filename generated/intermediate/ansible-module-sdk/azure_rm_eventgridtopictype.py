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
module: azure_rm_eventgridtopictype
version_added: '2.9'
short_description: Manage Azure TopicType instance.
description:
  - 'Create, update and delete instance of Azure TopicType.'
options:
  id:
    description:
      - Fully qualified identifier of the resource
    type: str
  name:
    description:
      - Name of the resource
    type: str
  type:
    description:
      - Type of the resource
    type: str
  provider:
    description:
      - Namespace of the provider of the topic type.
    type: str
  display_name:
    description:
      - Display Name for the topic type.
    type: str
  description:
    description:
      - Description of the topic type.
    type: str
  resource_region_type:
    description:
      - Region type of the resource.
    type: str
  provisioning_state:
    description:
      - Provisioning state of the topic type
    type: str
  supported_locations:
    description:
      - List of locations supported by this topic type.
    type: list
  state:
    description:
      - Assert the state of the TopicType.
      - >-
        Use C(present) to create or update an TopicType and C(absent) to delete
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
    - Fully qualified identifier of the resource
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of the resource
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties of the topic type info
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
    from azure.mgmt.eventgrid import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTopicTypes(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            provider=dict(
                type='str',
                disposition='/'
            ),
            display_name=dict(
                type='str',
                disposition='/'
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            resource_region_type=dict(
                type='str',
                disposition='/',
                choices=['RegionalResource',
                         'GlobalResource']
            ),
            provisioning_state=dict(
                type='str',
                disposition='/',
                choices=['Creating',
                         'Updating',
                         'Deleting',
                         'Succeeded',
                         'Canceled',
                         'Failed']
            ),
            supported_locations=dict(
                type='list',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.id = None
        self.name = None
        self.type = None
        self.properties = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTopicTypes, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

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
                response = self.mgmt_client.topic_types.create()
            else:
                response = self.mgmt_client.topic_types.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the TopicType instance.')
            self.fail('Error creating the TopicType instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the TopicType instance {0}'.format(self.))
        try:
            response = self.mgmt_client.topic_types.delete()
        except CloudError as e:
            self.log('Error attempting to delete the TopicType instance.')
            self.fail('Error deleting the TopicType instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the TopicType instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.topic_types.get(topic_type_name=self.topicTypeName)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTopicTypes()


if __name__ == '__main__':
    main()
