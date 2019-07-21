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
module: azure_rm_servicebussubscription_info
version_added: '2.9'
short_description: Get Subscription info.
description:
  - Get info of Subscription.
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
    required: true
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
  message_count:
    description:
      - Number of messages.
    type: number
  created_at:
    description:
      - Exact time the message was created.
    type: datetime
  accessed_at:
    description:
      - Last time there was a receive request to this subscription.
    type: datetime
  updated_at:
    description:
      - The exact time the message was updated.
    type: datetime
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
  lock_duration:
    description:
      - >-
        ISO 8061 lock duration timespan for the subscription. The default value
        is 1 minute.
    type: 'unknown-primary[timeSpan]'
  requires_session:
    description:
      - Value indicating if a subscription supports the concept of sessions.
    type: boolean
  default_message_time_to_live:
    description:
      - >-
        ISO 8061 Default message timespan to live value. This is the duration
        after which the message expires, starting from when the message is sent
        to Service Bus. This is the default value used when TimeToLive is not
        set on a message itself.
    type: 'unknown-primary[timeSpan]'
  dead_lettering_on_filter_evaluation_exceptions:
    description:
      - >-
        Value that indicates whether a subscription has dead letter support on
        filter evaluation exceptions.
    type: boolean
  dead_lettering_on_message_expiration:
    description:
      - >-
        Value that indicates whether a subscription has dead letter support when
        a message expires.
    type: boolean
  duplicate_detection_history_time_window:
    description:
      - >-
        ISO 8601 timeSpan structure that defines the duration of the duplicate
        detection history. The default value is 10 minutes.
    type: 'unknown-primary[timeSpan]'
  max_delivery_count:
    description:
      - Number of maximum deliveries.
    type: number
  status:
    description:
      - Enumerates the possible values for the status of a messaging entity.
    type: str
  enable_batched_operations:
    description:
      - Value that indicates whether server-side batched operations are enabled.
    type: boolean
  auto_delete_on_idle:
    description:
      - >-
        ISO 8061 timeSpan idle interval after which the topic is automatically
        deleted. The minimum duration is 5 minutes.
    type: 'unknown-primary[timeSpan]'
  forward_to:
    description:
      - Queue/Topic name to forward the messages
    type: str
  forward_dead_lettered_messages_to:
    description:
      - Queue/Topic name to forward the Dead Letter message
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: SubscriptionListByTopic
  azure_rm_servicebussubscription_info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
- name: SubscriptionGet
  azure_rm_servicebussubscription_info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    name: sdk-Subscriptions-2178

'''

RETURN = '''
subscriptions:
  description: >-
    A list of dict results where the key is the name of the Subscription and the
    values are the facts for that Subscription.
  returned: always
  type: complex
  contains:
    subscription_name:
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
            - Properties of subscriptions resource.
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSubscriptionsInfo(AzureRMModuleBase):
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
                type='str',
                required=true
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
        super(AzureRMSubscriptionsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.topic_name is not None and
            self.name is not None):
            self.results['subscriptions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.topic_name is not None):
            self.results['subscriptions'] = self.format_item(self.listbytopic())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.subscriptions.get(resource_group_name=self.resource_group,
                                                          namespace_name=self.namespace_name,
                                                          topic_name=self.topic_name,
                                                          subscription_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbytopic(self):
        response = None

        try:
            response = self.mgmt_client.subscriptions.list_by_topic(resource_group_name=self.resource_group,
                                                                    namespace_name=self.namespace_name,
                                                                    topic_name=self.topic_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMSubscriptionsInfo()


if __name__ == '__main__':
    main()
