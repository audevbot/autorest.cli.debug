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
module: azure_rm_servicebusrule_info
version_added: '2.9'
short_description: Get Rule info.
description:
  - Get info of Rule.
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
  action:
    description:
      - >-
        Represents the filter actions which are allowed for the transformation
        of a message that have been matched by a filter expression.
    type: dict
    suboptions:
      sql_expression:
        description:
          - SQL expression. e.g. MyProperty='ABC'
        type: str
      compatibility_level:
        description:
          - >-
            This property is reserved for future use. An integer value showing
            the compatibility level, currently hard-coded to 20.
        type: number
      requires_preprocessing:
        description:
          - Value that indicates whether the rule action requires preprocessing.
        type: boolean
  filter_type:
    description:
      - Filter type that is evaluated against a BrokeredMessage.
    type: str
  sql_filter:
    description:
      - Properties of sqlFilter
    type: dict
    suboptions:
      sql_expression:
        description:
          - The SQL expression. e.g. MyProperty='ABC'
        type: str
      compatibility_level:
        description:
          - >-
            This property is reserved for future use. An integer value showing
            the compatibility level, currently hard-coded to 20.
        type: number
      requires_preprocessing:
        description:
          - Value that indicates whether the rule action requires preprocessing.
        type: boolean
  correlation_filter:
    description:
      - Properties of correlationFilter
    type: dict
    suboptions:
      correlation_id:
        description:
          - Identifier of the correlation.
        type: str
      message_id:
        description:
          - Identifier of the message.
        type: str
      to:
        description:
          - Address to send to.
        type: str
      reply_to:
        description:
          - Address of the queue to reply to.
        type: str
      label:
        description:
          - Application specific label.
        type: str
      session_id:
        description:
          - Session identifier.
        type: str
      reply_to_session_id:
        description:
          - Session identifier to reply to.
        type: str
      content_type:
        description:
          - Content type of the message.
        type: str
      requires_preprocessing:
        description:
          - Value that indicates whether the rule action requires preprocessing.
        type: boolean
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: RulesListBySubscriptions
  azure_rm_servicebusrule_info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-8691
- name: RulesGet
  azure_rm_servicebusrule_info:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-8691
    name: myRule

'''

RETURN = '''
rules:
  description: >-
    A list of dict results where the key is the name of the Rule and the values
    are the facts for that Rule.
  returned: always
  type: complex
  contains:
    rule_name:
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
            - Properties of Rule resource
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


class AzureRMRulesInfo(AzureRMModuleBase):
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
            subscription_name=dict(
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
        self.subscription_name = None
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
        super(AzureRMRulesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.topic_name is not None and
            self.subscription_name is not None and
            self.name is not None):
            self.results['rules'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.topic_name is not None and
              self.subscription_name is not None):
            self.results['rules'] = self.format_item(self.listbysubscriptions())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.rules.get(resource_group_name=self.resource_group,
                                                  namespace_name=self.namespace_name,
                                                  topic_name=self.topic_name,
                                                  subscription_name=self.subscription_name,
                                                  rule_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbysubscriptions(self):
        response = None

        try:
            response = self.mgmt_client.rules.list_by_subscriptions(resource_group_name=self.resource_group,
                                                                    namespace_name=self.namespace_name,
                                                                    topic_name=self.topic_name,
                                                                    subscription_name=self.subscription_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMRulesInfo()


if __name__ == '__main__':
    main()
