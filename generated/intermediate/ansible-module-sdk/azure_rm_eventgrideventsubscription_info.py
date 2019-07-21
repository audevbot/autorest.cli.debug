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
module: azure_rm_eventgrideventsubscription_info
version_added: '2.9'
short_description: Get EventSubscription info.
description:
  - Get info of EventSubscription.
options:
  scope:
    description:
      - >-
        The scope of the event subscription. The scope can be a subscription, or
        a resource group, or a top level resource belonging to a resource
        provider namespace, or an EventGrid topic. For example, use
        '/subscriptions/{subscriptionId}/' for a subscription,
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for
        a resource group, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}'
        for a resource, and
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}'
        for an EventGrid topic.
    type: str
  event_subscription_name:
    description:
      - Name of the event subscription
    type: str
  location:
    description:
      - Name of the location
    type: str
  topic_type_name:
    description:
      - Name of the topic type
    type: str
  resource_group:
    description:
      - The name of the resource group within the user's subscription.
    type: str
  provider_namespace:
    description:
      - Namespace of the provider of the topic
    type: str
  resource_type_name:
    description:
      - Name of the resource type
    type: str
  name:
    description:
      - Name of the resource
    type: str
  id:
    description:
      - Fully qualified identifier of the resource
    type: str
  type:
    description:
      - Type of the resource
    type: str
  topic:
    description:
      - Name of the topic of the event subscription.
    type: str
  provisioning_state:
    description:
      - Provisioning state of the event subscription.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: EventSubscriptions_ListGlobalBySubscription
  azure_rm_eventgrideventsubscription_info: {}
- name: EventSubscriptions_GetForSubscription
  azure_rm_eventgrideventsubscription_info:
    scope: subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4
    event_subscription_name: examplesubscription3
- name: EventSubscriptions_GetForResourceGroup
  azure_rm_eventgrideventsubscription_info:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg
    event_subscription_name: examplesubscription2
- name: EventSubscriptions_GetForResource
  azure_rm_eventgrideventsubscription_info:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventHub/namespaces/examplenamespace1
    event_subscription_name: examplesubscription1
- name: EventSubscriptions_GetForCustomTopic
  azure_rm_eventgrideventsubscription_info:
    scope: >-
      subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourceGroups/examplerg/providers/Microsoft.EventGrid/topics/exampletopic2
    event_subscription_name: examplesubscription1
- name: EventSubscriptions_ListRegionalBySubscription
  azure_rm_eventgrideventsubscription_info:
    location: myLocation
- name: EventSubscriptions_ListGlobalBySubscriptionForTopicType
  azure_rm_eventgrideventsubscription_info:
    topic_type_name: myTopicType
- name: EventSubscriptions_ListGlobalByResourceGroup
  azure_rm_eventgrideventsubscription_info:
    resource_group: myResourceGroup
- name: EventSubscriptions_ListRegionalBySubscriptionForTopicType
  azure_rm_eventgrideventsubscription_info:
    location: myLocation
    topic_type_name: myTopicType
- name: EventSubscriptions_ListRegionalByResourceGroup
  azure_rm_eventgrideventsubscription_info:
    location: myLocation
    resource_group: myResourceGroup
- name: EventSubscriptions_ListGlobalByResourceGroupForTopicType
  azure_rm_eventgrideventsubscription_info:
    topic_type_name: myTopicType
    resource_group: myResourceGroup
- name: EventSubscriptions_ListRegionalByResourceGroupForTopicType
  azure_rm_eventgrideventsubscription_info:
    location: myLocation
    topic_type_name: myTopicType
    resource_group: myResourceGroup
- name: EventSubscriptions_ListByResource
  azure_rm_eventgrideventsubscription_info:
    resource_group: myResourceGroup
    provider_namespace: Microsoft.EventGrid
    resource_type_name: topics
    name: myResourceType

'''

RETURN = '''
event_subscriptions:
  description: >-
    A list of dict results where the key is the name of the EventSubscription
    and the values are the facts for that EventSubscription.
  returned: always
  type: complex
  contains:
    eventsubscription_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.eventgrid import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEventSubscriptionsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str'
            ),
            event_subscription_name=dict(
                type='str'
            ),
            location=dict(
                type='str'
            ),
            topic_type_name=dict(
                type='str'
            ),
            resource_group=dict(
                type='str'
            ),
            provider_namespace=dict(
                type='str'
            ),
            resource_type_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.scope = None
        self.event_subscription_name = None
        self.location = None
        self.topic_type_name = None
        self.resource_group = None
        self.provider_namespace = None
        self.resource_type_name = None
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
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEventSubscriptionsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.provider_namespace is not None and
            self.resource_type_name is not None and
            self.name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listbyresource())
        elif (self.resource_group is not None and
              self.location is not None and
              self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbyresourcegroupfortopictype())
        elif (self.resource_group is not None and
              self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listglobalbyresourcegroupfortopictype())
        elif (self.resource_group is not None and
              self.location is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbyresourcegroup())
        elif (self.location is not None and
              self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbysubscriptionfortopictype())
        elif (self.resource_group is not None):
            self.results['event_subscriptions'] = self.format_item(self.listglobalbyresourcegroup())
        elif (self.topic_type_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.listglobalbysubscriptionfortopictype())
        elif (self.location is not None):
            self.results['event_subscriptions'] = self.format_item(self.listregionalbysubscription())
        elif (self.scope is not None and
              self.event_subscription_name is not None):
            self.results['event_subscriptions'] = self.format_item(self.get())
        else:
            self.results['event_subscriptions'] = [self.format_item(self.listglobalbysubscription())]
        return self.results

    def listbyresource(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_by_resource(resource_group_name=self.resource_group,
                                                                             provider_namespace=self.provider_namespace,
                                                                             resource_type_name=self.resource_type_name,
                                                                             resource_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listregionalbyresourcegroupfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_resource_group_for_topic_type(resource_group_name=self.resource_group,
                                                                                                           location=self.location,
                                                                                                           topic_type_name=self.topic_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listglobalbyresourcegroupfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_resource_group_for_topic_type(resource_group_name=self.resource_group,
                                                                                                         topic_type_name=self.topic_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listregionalbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_resource_group(resource_group_name=self.resource_group,
                                                                                            location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listregionalbysubscriptionfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_subscription_for_topic_type(location=self.location,
                                                                                                         topic_type_name=self.topic_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listglobalbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listglobalbysubscriptionfortopictype(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_subscription_for_topic_type(topic_type_name=self.topic_type_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listregionalbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_regional_by_subscription(location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.get(scope=self.scope,
                                                                event_subscription_name=self.event_subscription_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listglobalbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.event_subscriptions.list_global_by_subscription()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMEventSubscriptionsInfo()


if __name__ == '__main__':
    main()
