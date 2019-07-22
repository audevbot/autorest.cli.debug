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
module: servicebustopic_info
version_added: '2.9'
short_description: Get Topic info.
description:
  - Get info of Topic.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
  topic_name:
    description:
      - The topic name.
    type: str
  name:
    description:
      - Resource name
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  size_in_bytes:
    description:
      - 'Size of the topic, in bytes.'
    type: number
  created_at:
    description:
      - Exact time the message was created.
    type: datetime
  updated_at:
    description:
      - The exact time the message was updated.
    type: datetime
  accessed_at:
    description:
      - >-
        Last time the message was sent, or a request was received, for this
        topic.
    type: datetime
  subscription_count:
    description:
      - Number of subscriptions.
    type: number
  count_details:
    description:
      - Message count details
    type: dict
    suboptions:
      active_message_count:
        description:
          - 'Number of active messages in the queue, topic, or subscription.'
        type: number
      dead_letter_message_count:
        description:
          - Number of messages that are dead lettered.
        type: number
      scheduled_message_count:
        description:
          - Number of scheduled messages.
        type: number
      transfer_message_count:
        description:
          - >-
            Number of messages transferred to another queue, topic, or
            subscription.
        type: number
      transfer_dead_letter_message_count:
        description:
          - Number of messages transferred into dead letters.
        type: number
  default_message_time_to_live:
    description:
      - >-
        ISO 8601 Default message timespan to live value. This is the duration
        after which the message expires, starting from when the message is sent
        to Service Bus. This is the default value used when TimeToLive is not
        set on a message itself.
    type: 'unknown-primary[timeSpan]'
  max_size_in_megabytes:
    description:
      - >-
        Maximum size of the topic in megabytes, which is the size of the memory
        allocated for the topic. Default is 1024.
    type: number
  requires_duplicate_detection:
    description:
      - Value indicating if this topic requires duplicate detection.
    type: boolean
  duplicate_detection_history_time_window:
    description:
      - >-
        ISO8601 timespan structure that defines the duration of the duplicate
        detection history. The default value is 10 minutes.
    type: 'unknown-primary[timeSpan]'
  enable_batched_operations:
    description:
      - Value that indicates whether server-side batched operations are enabled.
    type: boolean
  status:
    description:
      - Enumerates the possible values for the status of a messaging entity.
    type: str
  support_ordering:
    description:
      - Value that indicates whether the topic supports ordering.
    type: boolean
  auto_delete_on_idle:
    description:
      - >-
        ISO 8601 timespan idle interval after which the topic is automatically
        deleted. The minimum duration is 5 minutes.
    type: 'unknown-primary[timeSpan]'
  enable_partitioning:
    description:
      - >-
        Value that indicates whether the topic to be partitioned across multiple
        message brokers is enabled.
    type: boolean
  enable_express:
    description:
      - >-
        Value that indicates whether Express Entities are enabled. An express
        topic holds a message in memory temporarily before writing it to
        persistent storage.
    type: boolean
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: TopicGet
  azure.rm.servicebustopic.info:
    resource_group: myResourceGroup
    namespace_name: my
- name: TopicGet
  azure.rm.servicebustopic.info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
- name: TopicAuthorizationRuleListAll
  azure.rm.servicebustopic.info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
- name: TopicAuthorizationRuleGet
  azure.rm.servicebustopic.info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    name: myAuthorizationRule

'''

RETURN = '''
topics:
  description: >-
    A list of dict results where the key is the name of the Topic and the values
    are the facts for that Topic.
  returned: always
  type: complex
  contains:
    topic_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of topic resource.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMTopicsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            namespace_name=dict(
                type='str',
                required=true
            ),
            topic_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.topic_name = None
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
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTopicsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.topic_name is not None and
            self.name is not None):
            self.results['topics'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.topic_name is not None):
            self.results['topics'] = self.format_item(self.listauthorizationrules())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.topic_name is not None):
            self.results['topics'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['topics'] = self.format_item(self.listbynamespace())
        return self.results

    def getauthorizationrule(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ServiceBus' +
                    '/namespaces' +
                    '/{{ namespace_name }}' +
                    '/topics' +
                    '/{{ topic_name }}' +
                    '/authorizationRules' +
                    '/{{ authorization_rule_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ topic_name }}', self.topic_name)
        self.url = self.url.replace('{{ authorization_rule_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listauthorizationrules(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ServiceBus' +
                    '/namespaces' +
                    '/{{ namespace_name }}' +
                    '/topics' +
                    '/{{ topic_name }}' +
                    '/authorizationRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ topic_name }}', self.topic_name)
        self.url = self.url.replace('{{ authorization_rule_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ServiceBus' +
                    '/namespaces' +
                    '/{{ namespace_name }}' +
                    '/topics' +
                    '/{{ topic_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ topic_name }}', self.topic_name)
        self.url = self.url.replace('{{ authorization_rule_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbynamespace(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ServiceBus' +
                    '/namespaces' +
                    '/{{ namespace_name }}' +
                    '/topics')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ topic_name }}', self.topic_name)
        self.url = self.url.replace('{{ authorization_rule_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMTopicsInfo()


if __name__ == '__main__':
    main()
