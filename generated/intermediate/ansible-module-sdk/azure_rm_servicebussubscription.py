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
module: azure_rm_servicebussubscription
version_added: '2.9'
short_description: Manage Azure Subscription instance.
description:
  - 'Create, update and delete instance of Azure Subscription.'
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
  subscription_name:
    description:
      - The subscription name.
    required: true
    type: str
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
  id:
    description:
      - Resource Id
    type: str
  name:
    description:
      - Resource name
    type: str
  type:
    description:
      - Resource type
    type: str
  state:
    description:
      - Assert the state of the Subscription.
      - >-
        Use C(present) to create or update an Subscription and C(absent) to
        delete it.
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
- name: SubscriptionCreate
  azure_rm_servicebussubscription:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-2178
    enable_batched_operations: true
- name: SubscriptionDelete
  azure_rm_servicebussubscription:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-3670
    state: absent

'''

RETURN = '''
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
  contains:
    message_count:
      description:
        - Number of messages.
      returned: always
      type: number
      sample: null
    created_at:
      description:
        - Exact time the message was created.
      returned: always
      type: datetime
      sample: null
    accessed_at:
      description:
        - Last time there was a receive request to this subscription.
      returned: always
      type: datetime
      sample: null
    updated_at:
      description:
        - The exact time the message was updated.
      returned: always
      type: datetime
      sample: null
    count_details:
      description:
        - Message count details
      returned: always
      type: dict
      sample: null
      contains:
        active_message_count:
          description:
            - 'Number of active messages in the queue, topic, or subscription.'
          returned: always
          type: number
          sample: null
        dead_letter_message_count:
          description:
            - Number of messages that are dead lettered.
          returned: always
          type: number
          sample: null
        scheduled_message_count:
          description:
            - Number of scheduled messages.
          returned: always
          type: number
          sample: null
        transfer_message_count:
          description:
            - >-
              Number of messages transferred to another queue, topic, or
              subscription.
          returned: always
          type: number
          sample: null
        transfer_dead_letter_message_count:
          description:
            - Number of messages transferred into dead letters.
          returned: always
          type: number
          sample: null
    lock_duration:
      description:
        - >-
          ISO 8061 lock duration timespan for the subscription. The default
          value is 1 minute.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    requires_session:
      description:
        - Value indicating if a subscription supports the concept of sessions.
      returned: always
      type: boolean
      sample: null
    default_message_time_to_live:
      description:
        - >-
          ISO 8061 Default message timespan to live value. This is the duration
          after which the message expires, starting from when the message is
          sent to Service Bus. This is the default value used when TimeToLive is
          not set on a message itself.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    dead_lettering_on_filter_evaluation_exceptions:
      description:
        - >-
          Value that indicates whether a subscription has dead letter support on
          filter evaluation exceptions.
      returned: always
      type: boolean
      sample: null
    dead_lettering_on_message_expiration:
      description:
        - >-
          Value that indicates whether a subscription has dead letter support
          when a message expires.
      returned: always
      type: boolean
      sample: null
    duplicate_detection_history_time_window:
      description:
        - >-
          ISO 8601 timeSpan structure that defines the duration of the duplicate
          detection history. The default value is 10 minutes.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    max_delivery_count:
      description:
        - Number of maximum deliveries.
      returned: always
      type: number
      sample: null
    status:
      description:
        - Enumerates the possible values for the status of a messaging entity.
      returned: always
      type: str
      sample: null
    enable_batched_operations:
      description:
        - >-
          Value that indicates whether server-side batched operations are
          enabled.
      returned: always
      type: boolean
      sample: null
    auto_delete_on_idle:
      description:
        - >-
          ISO 8061 timeSpan idle interval after which the topic is automatically
          deleted. The minimum duration is 5 minutes.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    forward_to:
      description:
        - Queue/Topic name to forward the messages
      returned: always
      type: str
      sample: null
    forward_dead_lettered_messages_to:
      description:
        - Queue/Topic name to forward the Dead Letter message
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSubscriptions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            namespace_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            topic_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            subscription_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            lock_duration=dict(
                type='unknown-primary[timeSpan]',
                disposition='/'
            ),
            requires_session=dict(
                type='boolean',
                disposition='/'
            ),
            default_message_time_to_live=dict(
                type='unknown-primary[timeSpan]',
                disposition='/'
            ),
            dead_lettering_on_filter_evaluation_exceptions=dict(
                type='boolean',
                disposition='/'
            ),
            dead_lettering_on_message_expiration=dict(
                type='boolean',
                disposition='/'
            ),
            duplicate_detection_history_time_window=dict(
                type='unknown-primary[timeSpan]',
                disposition='/'
            ),
            max_delivery_count=dict(
                type='number',
                disposition='/'
            ),
            status=dict(
                type='str',
                disposition='/',
                choices=['Active',
                         'Disabled',
                         'Restoring',
                         'SendDisabled',
                         'ReceiveDisabled',
                         'Creating',
                         'Deleting',
                         'Renaming',
                         'Unknown']
            ),
            enable_batched_operations=dict(
                type='boolean',
                disposition='/'
            ),
            auto_delete_on_idle=dict(
                type='unknown-primary[timeSpan]',
                disposition='/'
            ),
            forward_to=dict(
                type='str',
                disposition='/'
            ),
            forward_dead_lettered_messages_to=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.topic_name = None
        self.subscription_name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSubscriptions, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
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
            response = self.mgmt_client.subscriptions.create_or_update(resource_group_name=self.resource_group,
                                                                       namespace_name=self.namespace_name,
                                                                       topic_name=self.topic_name,
                                                                       subscription_name=self.subscription_name,
                                                                       parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Subscription instance.')
            self.fail('Error creating the Subscription instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Subscription instance {0}'.format(self.))
        try:
            response = self.mgmt_client.subscriptions.delete(resource_group_name=self.resource_group,
                                                             namespace_name=self.namespace_name,
                                                             topic_name=self.topic_name,
                                                             subscription_name=self.subscription_name)
        except CloudError as e:
            self.log('Error attempting to delete the Subscription instance.')
            self.fail('Error deleting the Subscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Subscription instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.subscriptions.get(resource_group_name=self.resource_group,
                                                          namespace_name=self.namespace_name,
                                                          topic_name=self.topic_name,
                                                          subscription_name=self.subscription_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSubscriptions()


if __name__ == '__main__':
    main()
