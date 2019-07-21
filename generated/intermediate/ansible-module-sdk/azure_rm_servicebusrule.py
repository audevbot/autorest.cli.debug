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
module: azure_rm_servicebusrule
version_added: '2.9'
short_description: Manage Azure Rule instance.
description:
  - 'Create, update and delete instance of Azure Rule.'
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
      requires_preprocessing:
        description:
          - Value that indicates whether the rule action requires preprocessing.
        type: boolean
      compatibility_level:
        description:
          - >-
            This property is reserved for future use. An integer value showing
            the compatibility level, currently hard-coded to 20.
        type: number
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
      - Assert the state of the Rule.
      - Use C(present) to create or update an Rule and C(absent) to delete it.
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
- name: RulesCreateOrUpdate
  azure_rm_servicebusrule:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-8691
    name: myRule
- name: RulesCreateSqlFilter
  azure_rm_servicebusrule:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-8691
    name: myRule
    filter_type: SqlFilter
    sql_filter:
      sql_expression: myproperty=test
- name: RulesCreateCorrelationFilter
  azure_rm_servicebusrule:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-8691
    name: myRule
    filter_type: CorrelationFilter
    correlation_filter: {}
- name: RulesDelete
  azure_rm_servicebusrule:
    resource_group: myResourceGroup
    namespace_name: my
    topic_name: myTopic
    subscription_name: sdk-Subscriptions-8691
    name: myRule
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
    - Properties of Rule resource
  returned: always
  type: dict
  sample: null
  contains:
    action:
      description:
        - >-
          Represents the filter actions which are allowed for the transformation
          of a message that have been matched by a filter expression.
      returned: always
      type: dict
      sample: null
      contains:
        sql_expression:
          description:
            - SQL expression. e.g. MyProperty='ABC'
          returned: always
          type: str
          sample: null
        compatibility_level:
          description:
            - >-
              This property is reserved for future use. An integer value showing
              the compatibility level, currently hard-coded to 20.
          returned: always
          type: number
          sample: null
        requires_preprocessing:
          description:
            - >-
              Value that indicates whether the rule action requires
              preprocessing.
          returned: always
          type: boolean
          sample: null
    filter_type:
      description:
        - Filter type that is evaluated against a BrokeredMessage.
      returned: always
      type: str
      sample: null
    sql_filter:
      description:
        - Properties of sqlFilter
      returned: always
      type: dict
      sample: null
      contains:
        sql_expression:
          description:
            - The SQL expression. e.g. MyProperty='ABC'
          returned: always
          type: str
          sample: null
        compatibility_level:
          description:
            - >-
              This property is reserved for future use. An integer value showing
              the compatibility level, currently hard-coded to 20.
          returned: always
          type: number
          sample: null
        requires_preprocessing:
          description:
            - >-
              Value that indicates whether the rule action requires
              preprocessing.
          returned: always
          type: boolean
          sample: null
    correlation_filter:
      description:
        - Properties of correlationFilter
      returned: always
      type: dict
      sample: null
      contains:
        properties:
          description:
            - dictionary object for custom filters
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"834","$type":"DictionaryType","valueType":{"$id":"835","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"836","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"837","fixed":false},"deprecated":false}]
          sample: null
        correlation_id:
          description:
            - Identifier of the correlation.
          returned: always
          type: str
          sample: null
        message_id:
          description:
            - Identifier of the message.
          returned: always
          type: str
          sample: null
        to:
          description:
            - Address to send to.
          returned: always
          type: str
          sample: null
        reply_to:
          description:
            - Address of the queue to reply to.
          returned: always
          type: str
          sample: null
        label:
          description:
            - Application specific label.
          returned: always
          type: str
          sample: null
        session_id:
          description:
            - Session identifier.
          returned: always
          type: str
          sample: null
        reply_to_session_id:
          description:
            - Session identifier to reply to.
          returned: always
          type: str
          sample: null
        content_type:
          description:
            - Content type of the message.
          returned: always
          type: str
          sample: null
        requires_preprocessing:
          description:
            - >-
              Value that indicates whether the rule action requires
              preprocessing.
          returned: always
          type: boolean
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


class AzureRMRules(AzureRMModuleBaseExt):
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
            name=dict(
                type='str',
                updatable=False,
                disposition='rule_name',
                required=true
            ),
            action=dict(
                type='dict',
                disposition='/',
                options=dict(
                    sql_expression=dict(
                        type='str'
                    ),
                    compatibility_level=dict(
                        type='number'
                    ),
                    requires_preprocessing=dict(
                        type='boolean'
                    )
                )
            ),
            filter_type=dict(
                type='str',
                disposition='/',
                choices=['SqlFilter',
                         'CorrelationFilter']
            ),
            sql_filter=dict(
                type='dict',
                disposition='/',
                options=dict(
                    sql_expression=dict(
                        type='str'
                    ),
                    requires_preprocessing=dict(
                        type='boolean'
                    )
                )
            ),
            correlation_filter=dict(
                type='dict',
                disposition='/',
                options=dict(
                    correlation_id=dict(
                        type='str'
                    ),
                    message_id=dict(
                        type='str'
                    ),
                    to=dict(
                        type='str'
                    ),
                    reply_to=dict(
                        type='str'
                    ),
                    label=dict(
                        type='str'
                    ),
                    session_id=dict(
                        type='str'
                    ),
                    reply_to_session_id=dict(
                        type='str'
                    ),
                    content_type=dict(
                        type='str'
                    ),
                    requires_preprocessing=dict(
                        type='boolean'
                    )
                )
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
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRules, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.rules.create_or_update(resource_group_name=self.resource_group,
                                                               namespace_name=self.namespace_name,
                                                               topic_name=self.topic_name,
                                                               subscription_name=self.subscription_name,
                                                               rule_name=self.name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Rule instance.')
            self.fail('Error creating the Rule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Rule instance {0}'.format(self.))
        try:
            response = self.mgmt_client.rules.delete(resource_group_name=self.resource_group,
                                                     namespace_name=self.namespace_name,
                                                     topic_name=self.topic_name,
                                                     subscription_name=self.subscription_name,
                                                     rule_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Rule instance.')
            self.fail('Error deleting the Rule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Rule instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.rules.get(resource_group_name=self.resource_group,
                                                  namespace_name=self.namespace_name,
                                                  topic_name=self.topic_name,
                                                  subscription_name=self.subscription_name,
                                                  rule_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRules()


if __name__ == '__main__':
    main()
