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
module: azure_rm_eventgridtopic
version_added: '2.9'
short_description: Manage Azure Topic instance.
description:
  - 'Create, update and delete instance of Azure Topic.'
options:
  resource_group:
    description:
      - The name of the resource group within the user's subscription.
    required: true
    type: str
  topic_name:
    description:
      - Name of the topic
    required: true
    type: str
  location:
    description:
      - Location of the resource
    required: true
    type: str
  provisioning_state:
    description:
      - Provisioning state of the topic.
    type: str
  endpoint:
    description:
      - Endpoint for the topic.
    type: str
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
  state:
    description:
      - Assert the state of the Topic.
      - Use C(present) to create or update an Topic and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Topics_CreateOrUpdate
  azure_rm_eventgridtopic:
    resource_group: myResourceGroup
    topic_name: myTopic
    topic_info:
      location: westus2
      tags:
        tag1: value1
        tag2: value2
- name: Topics_Update
  azure_rm_eventgridtopic:
    resource_group: myResourceGroup
    topic_name: myTopic
- name: Topics_Delete
  azure_rm_eventgridtopic:
    resource_group: myResourceGroup
    topic_name: myTopic
    state: absent

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
location:
  description:
    - Location of the resource
  returned: always
  type: str
  sample: null
tags:
  description:
    - Tags of the resource
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"342","$type":"DictionaryType","valueType":{"$id":"343","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"344","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"345","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - Properties of the topic
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_state:
      description:
        - Provisioning state of the topic.
      returned: always
      type: str
      sample: null
    endpoint:
      description:
        - Endpoint for the topic.
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
    from azure.mgmt.eventgrid import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTopics(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            topic_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
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
        self.topic_name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTopics, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

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
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.topics.create_or_update(resource_group_name=self.resource_group,
                                                                topic_name=self.topic_name,
                                                                topic_info=self.topicInfo)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Topic instance.')
            self.fail('Error creating the Topic instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Topic instance {0}'.format(self.))
        try:
            response = self.mgmt_client.topics.delete(resource_group_name=self.resource_group,
                                                      topic_name=self.topic_name)
        except CloudError as e:
            self.log('Error attempting to delete the Topic instance.')
            self.fail('Error deleting the Topic instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Topic instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.topics.get(resource_group_name=self.resource_group,
                                                   topic_name=self.topic_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTopics()


if __name__ == '__main__':
    main()
