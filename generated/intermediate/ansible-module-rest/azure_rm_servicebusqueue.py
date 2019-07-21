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
module: azure_rm_servicebusqueue
version_added: '2.9'
short_description: Manage Azure Queue instance.
description:
  - 'Create, update and delete instance of Azure Queue.'
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
  name:
    description:
      - Resource name
    type: str
  lock_duration:
    description:
      - >-
        ISO 8601 timespan duration of a peek-lock; that is, the amount of time
        that the message is locked for other receivers. The maximum value for
        LockDuration is 5 minutes; the default value is 1 minute.
    type: 'unknown-primary[timeSpan]'
  max_size_in_megabytes:
    description:
      - >-
        The maximum size of the queue in megabytes, which is the size of memory
        allocated for the queue. Default is 1024.
    type: number
  requires_duplicate_detection:
    description:
      - A value indicating if this queue requires duplicate detection.
    type: boolean
  requires_session:
    description:
      - >-
        A value that indicates whether the queue supports the concept of
        sessions.
    type: boolean
  default_message_time_to_live:
    description:
      - >-
        ISO 8601 default message timespan to live value. This is the duration
        after which the message expires, starting from when the message is sent
        to Service Bus. This is the default value used when TimeToLive is not
        set on a message itself.
    type: 'unknown-primary[timeSpan]'
  dead_lettering_on_message_expiration:
    description:
      - >-
        A value that indicates whether this queue has dead letter support when a
        message expires.
    type: boolean
  duplicate_detection_history_time_window:
    description:
      - >-
        ISO 8601 timeSpan structure that defines the duration of the duplicate
        detection history. The default value is 10 minutes.
    type: 'unknown-primary[timeSpan]'
  max_delivery_count:
    description:
      - >-
        The maximum delivery count. A message is automatically deadlettered
        after this number of deliveries. default value is 10.
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
        ISO 8061 timeSpan idle interval after which the queue is automatically
        deleted. The minimum duration is 5 minutes.
    type: 'unknown-primary[timeSpan]'
  enable_partitioning:
    description:
      - >-
        A value that indicates whether the queue is to be partitioned across
        multiple message brokers.
    type: boolean
  enable_express:
    description:
      - >-
        A value that indicates whether Express Entities are enabled. An express
        queue holds a message in memory temporarily before writing it to
        persistent storage.
    type: boolean
  forward_to:
    description:
      - Queue/Topic name to forward the messages
    type: str
  forward_dead_lettered_messages_to:
    description:
      - Queue/Topic name to forward the Dead Letter message
    type: str
  count_details:
    description:
      - Message Count Details.
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
  created_at:
    description:
      - The exact time the message was created.
    type: datetime
  updated_at:
    description:
      - The exact time the message was updated.
    type: datetime
  accessed_at:
    description:
      - >-
        Last time a message was sent, or the last time there was a receive
        request to this queue.
    type: datetime
  size_in_bytes:
    description:
      - 'The size of the queue, in bytes.'
    type: number
  message_count:
    description:
      - The number of messages in the queue.
    type: number
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  state:
    description:
      - Assert the state of the Queue.
      - Use C(present) to create or update an Queue and C(absent) to delete it.
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
- name: QueueCreate
  azure_rm_servicebusqueue:
    resource_group: myResourceGroup
    namespace_name: my
    name: myQueue
    enable_partitioning: true
- name: QueueDelete
  azure_rm_servicebusqueue:
    resource_group: myResourceGroup
    namespace_name: my
    name: myQueue
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
    - Queue Properties
  returned: always
  type: dict
  sample: null
  contains:
    count_details:
      description:
        - Message Count Details.
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
    created_at:
      description:
        - The exact time the message was created.
      returned: always
      type: datetime
      sample: null
    updated_at:
      description:
        - The exact time the message was updated.
      returned: always
      type: datetime
      sample: null
    accessed_at:
      description:
        - >-
          Last time a message was sent, or the last time there was a receive
          request to this queue.
      returned: always
      type: datetime
      sample: null
    size_in_bytes:
      description:
        - 'The size of the queue, in bytes.'
      returned: always
      type: number
      sample: null
    message_count:
      description:
        - The number of messages in the queue.
      returned: always
      type: number
      sample: null
    lock_duration:
      description:
        - >-
          ISO 8601 timespan duration of a peek-lock; that is, the amount of time
          that the message is locked for other receivers. The maximum value for
          LockDuration is 5 minutes; the default value is 1 minute.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    max_size_in_megabytes:
      description:
        - >-
          The maximum size of the queue in megabytes, which is the size of
          memory allocated for the queue. Default is 1024.
      returned: always
      type: number
      sample: null
    requires_duplicate_detection:
      description:
        - A value indicating if this queue requires duplicate detection.
      returned: always
      type: boolean
      sample: null
    requires_session:
      description:
        - >-
          A value that indicates whether the queue supports the concept of
          sessions.
      returned: always
      type: boolean
      sample: null
    default_message_time_to_live:
      description:
        - >-
          ISO 8601 default message timespan to live value. This is the duration
          after which the message expires, starting from when the message is
          sent to Service Bus. This is the default value used when TimeToLive is
          not set on a message itself.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    dead_lettering_on_message_expiration:
      description:
        - >-
          A value that indicates whether this queue has dead letter support when
          a message expires.
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
        - >-
          The maximum delivery count. A message is automatically deadlettered
          after this number of deliveries. default value is 10.
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
          ISO 8061 timeSpan idle interval after which the queue is automatically
          deleted. The minimum duration is 5 minutes.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    enable_partitioning:
      description:
        - >-
          A value that indicates whether the queue is to be partitioned across
          multiple message brokers.
      returned: always
      type: boolean
      sample: null
    enable_express:
      description:
        - >-
          A value that indicates whether Express Entities are enabled. An
          express queue holds a message in memory temporarily before writing it
          to persistent storage.
      returned: always
      type: boolean
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMQueues(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            namespace_name=dict(
                type='str',
                updatable=False,
                disposition='namespaceName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='queueName',
                required=true
            ),
            lock_duration=dict(
                type='unknown-primary[timeSpan]',
                disposition='/properties/lockDuration'
            ),
            max_size_in_megabytes=dict(
                type='number',
                disposition='/properties/maxSizeInMegabytes'
            ),
            requires_duplicate_detection=dict(
                type='boolean',
                disposition='/properties/requiresDuplicateDetection'
            ),
            requires_session=dict(
                type='boolean',
                disposition='/properties/requiresSession'
            ),
            default_message_time_to_live=dict(
                type='unknown-primary[timeSpan]',
                disposition='/properties/defaultMessageTimeToLive'
            ),
            dead_lettering_on_message_expiration=dict(
                type='boolean',
                disposition='/properties/deadLetteringOnMessageExpiration'
            ),
            duplicate_detection_history_time_window=dict(
                type='unknown-primary[timeSpan]',
                disposition='/properties/duplicateDetectionHistoryTimeWindow'
            ),
            max_delivery_count=dict(
                type='number',
                disposition='/properties/maxDeliveryCount'
            ),
            status=dict(
                type='str',
                disposition='/properties/*',
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
                disposition='/properties/enableBatchedOperations'
            ),
            auto_delete_on_idle=dict(
                type='unknown-primary[timeSpan]',
                disposition='/properties/autoDeleteOnIdle'
            ),
            enable_partitioning=dict(
                type='boolean',
                disposition='/properties/enablePartitioning'
            ),
            enable_express=dict(
                type='boolean',
                disposition='/properties/enableExpress'
            ),
            forward_to=dict(
                type='str',
                disposition='/properties/forwardTo'
            ),
            forward_dead_lettered_messages_to=dict(
                type='str',
                disposition='/properties/forwardDeadLetteredMessagesTo'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMQueues, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

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
        self.url = self.url.replace('{{ queue_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Queue instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Queue instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the Queue instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('Queue instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Queue instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Queue instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the Queue instance.')
            self.fail('Error creating the Queue instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Queue instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the Queue instance.')
            self.fail('Error deleting the Queue instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Queue instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("Queue instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Queue instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMQueues()


if __name__ == '__main__':
    main()
