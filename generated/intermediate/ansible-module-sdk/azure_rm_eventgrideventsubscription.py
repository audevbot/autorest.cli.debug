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
module: azure_rm_eventgrideventsubscription
version_added: '2.9'
short_description: Manage Azure EventSubscription instance.
description:
  - 'Create, update and delete instance of Azure EventSubscription.'
options:
  scope:
    description:
      - >-
        The identifier of the resource to which the event subscription needs to
        be created or updated. The scope can be a subscription, or a resource
        group, or a top level resource belonging to a resource provider
        namespace, or an EventGrid topic. For example, use
        '/subscriptions/{subscriptionId}/' for a subscription,
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for
        a resource group, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}'
        for a resource, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}'
        for an EventGrid topic.
    required: true
    type: str
  name:
    description:
      - Name of the resource
    type: str
  destination:
    description:
      - >-
        Information about the destination where events have to be delivered for
        the event subscription.
    type: dict
  filter:
    description:
      - Information about the filter for the event subscription.
    type: dict
    suboptions:
      subject_begins_with:
        description:
          - >-
            An optional string to filter events for an event subscription based
            on a resource path prefix.<br>The format of this depends on the
            publisher of the events. <br>Wildcard characters are not supported
            in this path.
        type: str
      subject_ends_with:
        description:
          - >-
            An optional string to filter events for an event subscription based
            on a resource path suffix.<br>Wildcard characters are not supported
            in this path.
        type: str
      included_event_types:
        description:
          - >-
            A list of applicable event types that need to be part of the event
            subscription. <br>If it is desired to subscribe to all event types,
            the string "all" needs to be specified as an element in this list.
        type: list
      is_subject_case_sensitive:
        description:
          - >-
            Specifies if the SubjectBeginsWith and SubjectEndsWith properties of
            the filter <br>should be compared in a case sensitive manner.
        type: boolean
  labels:
    description:
      - List of user defined labels.
    type: list
  retry_policy:
    description:
      - >-
        The retry policy for events. This can be used to configure maximum
        number of delivery attempts and time to live for events.
    type: dict
    suboptions:
      max_delivery_attempts:
        description:
          - Maximum number of delivery retry attempts for events.
        type: number
      event_time_to_live_in_minutes:
        description:
          - Time To Live (in minutes) for events.
        type: number
  dead_letter_destination:
    description:
      - The DeadLetter destination of the event subscription.
    type: dict
  topic:
    description:
      - Name of the topic of the event subscription.
    type: str
  provisioning_state:
    description:
      - Provisioning state of the event subscription.
    type: str
  id:
    description:
      - Fully qualified identifier of the resource
    type: str
  type:
    description:
      - Type of the resource
    type: str
  state:
    description:
      - Assert the state of the EventSubscription.
      - >-
        Use C(present) to create or update an EventSubscription and C(absent) to
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
- name: EventSubscriptions_CreateOrUpdateForSubscription
  azure_rm_eventgrideventsubscription:
    scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: WebHook
          properties:
            endpointUrl: 'https://requestb.in/15ksip71'
        filter:
          isSubjectCaseSensitive: false
- name: EventSubscriptions_CreateOrUpdateForResourceGroup
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: WebHook
          properties:
            endpointUrl: 'https://requestb.in/15ksip71'
        filter:
          isSubjectCaseSensitive: false
          subjectBeginsWith: ExamplePrefix
          subjectEndsWith: ExampleSuffix
- name: EventSubscriptions_CreateOrUpdateForResource
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: WebHook
          properties:
            endpointUrl: 'https://requestb.in/15ksip71'
        filter:
          isSubjectCaseSensitive: false
          subjectBeginsWith: ExamplePrefix
          subjectEndsWith: ExampleSuffix
- name: EventSubscriptions_CreateOrUpdateForCustomTopic_WebhookDestination
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: WebHook
          properties:
            endpointUrl: >-
              https://contosofunction.azurewebsites.net/api/HttpTriggerCSharp1?code=<HIDDEN>
        filter:
          isSubjectCaseSensitive: false
          subjectBeginsWith: ExamplePrefix
          subjectEndsWith: ExampleSuffix
        deadLetterDestination:
          endpointType: StorageBlob
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Storage/storageAccounts/{{
              storage_account_name }}
            blobContainerName: contosocontainer
- name: EventSubscriptions_CreateOrUpdateForCustomTopic_EventHubDestination
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: EventHub
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.EventHub/namespaces/{{
              namespace_name }}/eventhubs/{{ eventhub_name }}
        filter:
          isSubjectCaseSensitive: false
          subjectBeginsWith: ExamplePrefix
          subjectEndsWith: ExampleSuffix
        deadLetterDestination:
          endpointType: StorageBlob
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Storage/storageAccounts/{{
              storage_account_name }}
            blobContainerName: contosocontainer
- name: EventSubscriptions_CreateOrUpdateForCustomTopic_HybridConnectionDestination
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: HybridConnection
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Relay/namespaces/{{
              namespace_name }}/hybridConnections/{{ hybrid_connection_name }}
        filter:
          isSubjectCaseSensitive: false
          subjectBeginsWith: ExamplePrefix
          subjectEndsWith: ExampleSuffix
        deadLetterDestination:
          endpointType: StorageBlob
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Storage/storageAccounts/{{
              storage_account_name }}
            blobContainerName: contosocontainer
- name: EventSubscriptions_CreateOrUpdateForCustomTopic_StorageQueueDestination
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
    name: myEventSubscription
    event_subscription_info:
      properties:
        destination:
          endpointType: StorageQueue
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Storage/storageAccounts/{{
              storage_account_name }}
            queueName: queue1
        filter:
          isSubjectCaseSensitive: false
          subjectBeginsWith: ExamplePrefix
          subjectEndsWith: ExampleSuffix
        deadLetterDestination:
          endpointType: StorageBlob
          properties:
            resourceId: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Storage/storageAccounts/{{
              storage_account_name }}
            blobContainerName: contosocontainer
- name: EventSubscriptions_UpdateForSubscription
  azure_rm_eventgrideventsubscription:
    scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
    name: myEventSubscription
- name: EventSubscriptions_UpdateForResourceGroup
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
    name: myEventSubscription
- name: EventSubscriptions_UpdateForResource
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
    name: myEventSubscription
- name: EventSubscriptions_UpdateForCustomTopic
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic2
    name: myEventSubscription
- name: EventSubscriptions_DeleteForSubscription
  azure_rm_eventgrideventsubscription:
    scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
    name: myEventSubscription
    state: absent
- name: EventSubscriptions_DeleteForResourceGroup
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
    name: myEventSubscription
    state: absent
- name: EventSubscriptions_DeleteForResource
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
    name: myEventSubscription
    state: absent
- name: EventSubscriptions_DeleteForCustomTopic
  azure_rm_eventgrideventsubscription:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic1
    name: myEventSubscription
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
properties:
  description:
    - Properties of the event subscription
  returned: always
  type: dict
  sample: null
  contains:
    topic:
      description:
        - Name of the topic of the event subscription.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the event subscription.
      returned: always
      type: str
      sample: null
    destination:
      description:
        - >-
          Information about the destination where events have to be delivered
          for the event subscription.
      returned: always
      type: dict
      sample: null
    filter:
      description:
        - Information about the filter for the event subscription.
      returned: always
      type: dict
      sample: null
      contains:
        subject_begins_with:
          description:
            - >-
              An optional string to filter events for an event subscription
              based on a resource path prefix.<br>The format of this depends on
              the publisher of the events. <br>Wildcard characters are not
              supported in this path.
          returned: always
          type: str
          sample: null
        subject_ends_with:
          description:
            - >-
              An optional string to filter events for an event subscription
              based on a resource path suffix.<br>Wildcard characters are not
              supported in this path.
          returned: always
          type: str
          sample: null
        included_event_types:
          description:
            - >-
              A list of applicable event types that need to be part of the event
              subscription. <br>If it is desired to subscribe to all event
              types, the string "all" needs to be specified as an element in
              this list.
          returned: always
          type: str
          sample: null
        is_subject_case_sensitive:
          description:
            - >-
              Specifies if the SubjectBeginsWith and SubjectEndsWith properties
              of the filter <br>should be compared in a case sensitive manner.
          returned: always
          type: boolean
          sample: null
    labels:
      description:
        - List of user defined labels.
      returned: always
      type: str
      sample: null
    retry_policy:
      description:
        - >-
          The retry policy for events. This can be used to configure maximum
          number of delivery attempts and time to live for events.
      returned: always
      type: dict
      sample: null
      contains:
        max_delivery_attempts:
          description:
            - Maximum number of delivery retry attempts for events.
          returned: always
          type: number
          sample: null
        event_time_to_live_in_minutes:
          description:
            - Time To Live (in minutes) for events.
          returned: always
          type: number
          sample: null
    dead_letter_destination:
      description:
        - The DeadLetter destination of the event subscription.
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


class AzureRMEventSubscriptions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='event_subscription_name',
                required=true
            ),
            destination=dict(
                type='dict',
                disposition='/'
            ),
            filter=dict(
                type='dict',
                disposition='/',
                options=dict(
                    subject_begins_with=dict(
                        type='str'
                    ),
                    subject_ends_with=dict(
                        type='str'
                    ),
                    included_event_types=dict(
                        type='list'
                    ),
                    is_subject_case_sensitive=dict(
                        type='boolean'
                    )
                )
            ),
            labels=dict(
                type='list',
                disposition='/'
            ),
            retry_policy=dict(
                type='dict',
                disposition='/',
                options=dict(
                    max_delivery_attempts=dict(
                        type='number'
                    ),
                    event_time_to_live_in_minutes=dict(
                        type='number'
                    )
                )
            ),
            dead_letter_destination=dict(
                type='dict',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEventSubscriptions, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.event_subscriptions.create_or_update(scope=self.scope,
                                                                             event_subscription_name=self.name,
                                                                             event_subscription_info=self.eventSubscriptionInfo)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the EventSubscription instance.')
            self.fail('Error creating the EventSubscription instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the EventSubscription instance {0}'.format(self.))
        try:
            response = self.mgmt_client.event_subscriptions.delete(scope=self.scope,
                                                                   event_subscription_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the EventSubscription instance.')
            self.fail('Error deleting the EventSubscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the EventSubscription instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.event_subscriptions.get(scope=self.scope,
                                                                event_subscription_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEventSubscriptions()


if __name__ == '__main__':
    main()
