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
module: azure_rm_servicebusqueue_info
version_added: '2.9'
short_description: Get Queue info.
description:
  - Get info of Queue.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
  namespace_name:
    description:
      - The namespace name
    required: true
  queue_name:
    description:
      - The queue name.
  name:
    description:
      - Resource name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  count_details:
    description:
      - Message Count Details.
    suboptions:
      active_message_count:
        description:
          - 'Number of active messages in the queue, topic, or subscription.'
      dead_letter_message_count:
        description:
          - Number of messages that are dead lettered.
      scheduled_message_count:
        description:
          - Number of scheduled messages.
      transfer_message_count:
        description:
          - >-
            Number of messages transferred to another queue, topic, or
            subscription.
      transfer_dead_letter_message_count:
        description:
          - Number of messages transferred into dead letters.
  created_at:
    description:
      - The exact time the message was created.
  updated_at:
    description:
      - The exact time the message was updated.
  accessed_at:
    description:
      - >-
        Last time a message was sent, or the last time there was a receive
        request to this queue.
  size_in_bytes:
    description:
      - 'The size of the queue, in bytes.'
  message_count:
    description:
      - The number of messages in the queue.
  lock_duration:
    description:
      - >-
        ISO 8601 timespan duration of a peek-lock; that is, the amount of time
        that the message is locked for other receivers. The maximum value for
        LockDuration is 5 minutes; the default value is 1 minute.
  max_size_in_megabytes:
    description:
      - >-
        The maximum size of the queue in megabytes, which is the size of memory
        allocated for the queue. Default is 1024.
  requires_duplicate_detection:
    description:
      - A value indicating if this queue requires duplicate detection.
  requires_session:
    description:
      - >-
        A value that indicates whether the queue supports the concept of
        sessions.
  default_message_time_to_live:
    description:
      - >-
        ISO 8601 default message timespan to live value. This is the duration
        after which the message expires, starting from when the message is sent
        to Service Bus. This is the default value used when TimeToLive is not
        set on a message itself.
  dead_lettering_on_message_expiration:
    description:
      - >-
        A value that indicates whether this queue has dead letter support when a
        message expires.
  duplicate_detection_history_time_window:
    description:
      - >-
        ISO 8601 timeSpan structure that defines the duration of the duplicate
        detection history. The default value is 10 minutes.
  max_delivery_count:
    description:
      - >-
        The maximum delivery count. A message is automatically deadlettered
        after this number of deliveries. default value is 10.
  status:
    description:
      - Enumerates the possible values for the status of a messaging entity.
  enable_batched_operations:
    description:
      - Value that indicates whether server-side batched operations are enabled.
  auto_delete_on_idle:
    description:
      - >-
        ISO 8061 timeSpan idle interval after which the queue is automatically
        deleted. The minimum duration is 5 minutes.
  enable_partitioning:
    description:
      - >-
        A value that indicates whether the queue is to be partitioned across
        multiple message brokers.
  enable_express:
    description:
      - >-
        A value that indicates whether Express Entities are enabled. An express
        queue holds a message in memory temporarily before writing it to
        persistent storage.
  forward_to:
    description:
      - Queue/Topic name to forward the messages
  forward_dead_lettered_messages_to:
    description:
      - Queue/Topic name to forward the Dead Letter message
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: QueueListByNameSpace
  azure_rm_servicebusqueue_info:
    resource_group: myResourceGroup
    namespace_name: my
- name: QueueGet
  azure_rm_servicebusqueue_info:
    resource_group: myResourceGroup
    namespace_name: my
    queue_name: myQueue
- name: QueueAuthorizationRuleListAll
  azure_rm_servicebusqueue_info:
    resource_group: myResourceGroup
    namespace_name: my
    queue_name: myQueue
- name: QueueAuthorizationRuleGet
  azure_rm_servicebusqueue_info:
    resource_group: myResourceGroup
    namespace_name: my
    queue_name: myQueue
    name: myAuthorizationRule

'''

RETURN = '''
queues:
  description: >-
    A list of dict results where the key is the name of the Queue and the values
    are the facts for that Queue.
  returned: always
  type: complex
  contains:
    queue_name:
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
            - Queue Properties
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


class AzureRMQueuesInfo(AzureRMModuleBase):
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
            queue_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.queue_name = None
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
        super(AzureRMQueuesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.queue_name is not None and
            self.name is not None):
            self.results['queues'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.queue_name is not None):
            self.results['queues'] = self.format_item(self.listauthorizationrules())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.queue_name is not None):
            self.results['queues'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['queues'] = self.format_item(self.listbynamespace())
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
                    '/queues' +
                    '/{{ queue_name }}' +
                    '/authorizationRules' +
                    '/{{ authorization_rule_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ queue_name }}', self.queue_name)
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
                    '/queues' +
                    '/{{ queue_name }}' +
                    '/authorizationRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ queue_name }}', self.queue_name)
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
                    '/queues' +
                    '/{{ queue_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ queue_name }}', self.queue_name)
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
                    '/queues')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ queue_name }}', self.queue_name)
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
    AzureRMQueuesInfo()


if __name__ == '__main__':
    main()
