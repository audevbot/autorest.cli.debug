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
module: azure_rm_servicebustopic
version_added: '2.9'
short_description: Manage Azure Topic instance.
description:
  - 'Create, update and delete instance of Azure Topic.'
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
      - Assert the state of the Topic.
      - Use C(present) to create or update an Topic and C(absent) to delete it.
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
- name: TopicCreate
  azure_rm_servicebustopic:
    resource_group: myResourceGroup
    namespace_name: my
    name: myTopic
    enable_express: true
- name: TopicDelete
  azure_rm_servicebustopic:
    resource_group: myResourceGroup
    namespace_name: my
    name: myTopic
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
    - Properties of topic resource.
  returned: always
  type: dict
  sample: null
  contains:
    size_in_bytes:
      description:
        - 'Size of the topic, in bytes.'
      returned: always
      type: number
      sample: null
    created_at:
      description:
        - Exact time the message was created.
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
          Last time the message was sent, or a request was received, for this
          topic.
      returned: always
      type: datetime
      sample: null
    subscription_count:
      description:
        - Number of subscriptions.
      returned: always
      type: number
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
    default_message_time_to_live:
      description:
        - >-
          ISO 8601 Default message timespan to live value. This is the duration
          after which the message expires, starting from when the message is
          sent to Service Bus. This is the default value used when TimeToLive is
          not set on a message itself.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    max_size_in_megabytes:
      description:
        - >-
          Maximum size of the topic in megabytes, which is the size of the
          memory allocated for the topic. Default is 1024.
      returned: always
      type: number
      sample: null
    requires_duplicate_detection:
      description:
        - Value indicating if this topic requires duplicate detection.
      returned: always
      type: boolean
      sample: null
    duplicate_detection_history_time_window:
      description:
        - >-
          ISO8601 timespan structure that defines the duration of the duplicate
          detection history. The default value is 10 minutes.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    enable_batched_operations:
      description:
        - >-
          Value that indicates whether server-side batched operations are
          enabled.
      returned: always
      type: boolean
      sample: null
    status:
      description:
        - Enumerates the possible values for the status of a messaging entity.
      returned: always
      type: str
      sample: null
    support_ordering:
      description:
        - Value that indicates whether the topic supports ordering.
      returned: always
      type: boolean
      sample: null
    auto_delete_on_idle:
      description:
        - >-
          ISO 8601 timespan idle interval after which the topic is automatically
          deleted. The minimum duration is 5 minutes.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    enable_partitioning:
      description:
        - >-
          Value that indicates whether the topic to be partitioned across
          multiple message brokers is enabled.
      returned: always
      type: boolean
      sample: null
    enable_express:
      description:
        - >-
          Value that indicates whether Express Entities are enabled. An express
          topic holds a message in memory temporarily before writing it to
          persistent storage.
      returned: always
      type: boolean
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


class AzureRMTopics(AzureRMModuleBaseExt):
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
                disposition='topicName',
                required=true
            ),
            default_message_time_to_live=dict(
                type='unknown-primary[timeSpan]',
                disposition='/properties/defaultMessageTimeToLive'
            ),
            max_size_in_megabytes=dict(
                type='number',
                disposition='/properties/maxSizeInMegabytes'
            ),
            requires_duplicate_detection=dict(
                type='boolean',
                disposition='/properties/requiresDuplicateDetection'
            ),
            duplicate_detection_history_time_window=dict(
                type='unknown-primary[timeSpan]',
                disposition='/properties/duplicateDetectionHistoryTimeWindow'
            ),
            enable_batched_operations=dict(
                type='boolean',
                disposition='/properties/enableBatchedOperations'
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
            support_ordering=dict(
                type='boolean',
                disposition='/properties/supportOrdering'
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
                    '/topics' +
                    '/{{ topic_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ topic_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Topic instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Topic instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the Topic instance')

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
            self.log('Topic instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Topic instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Topic instance {0}'.format(self.))

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
            self.log('Error attempting to create the Topic instance.')
            self.fail('Error creating the Topic instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Topic instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Topic instance.')
            self.fail('Error deleting the Topic instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Topic instance {0} is present'.format(self.))
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
            # self.log("Topic instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Topic instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMTopics()


if __name__ == '__main__':
    main()
