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
module: alertsmanagementactionrule_info
version_added: '2.9'
short_description: Get ActionRule info.
description:
  - Get info of ActionRule.
options:
  target_resource_group:
    description:
      - Filter by target resource group name. Default value is select all.
    type: str
  target_resource_type:
    description:
      - Filter by target resource type. Default value is select all.
    type: str
  target_resource:
    description:
      - >-
        Filter by target resource( which is full ARM ID) Default value is select
        all.
    type: str
  severity:
    description:
      - Filter by severity.  Default value is select all.
    type: str
  monitor_service:
    description:
      - >-
        Filter by monitor service which generates the alert instance. Default
        value is select all.
    type: str
  impacted_scope:
    description:
      - >-
        filter by impacted/target scope (provide comma separated list for
        multiple scopes). The value should be an well constructed ARM id of the
        scope.
    type: str
  description:
    description:
      - filter by alert rule description
    type: str
  alert_rule_id:
    description:
      - filter by alert rule id
    type: str
  action_group:
    description:
      - filter by action group configured as part of action rule
    type: str
  name:
    description:
      - The name of action rule that needs to be fetched
    type: str
  resource_group:
    description:
      - Resource group name where the resource is created.
    type: str
  next_link:
    description:
      - URL to fetch the next set of action rules
    type: str
  value:
    description:
      - List of action rules
    type: list
    suboptions:
      id:
        description:
          - Azure resource Id
        type: str
      type:
        description:
          - Azure resource type
        type: str
      name:
        description:
          - Azure resource name
        type: str
      location:
        description:
          - Resource location
        required: true
        type: str
      scope:
        description:
          - scope on which action rule will apply
        type: dict
        suboptions:
          scope_type:
            description:
              - type of target scope
            type: str
          values:
            description:
              - >-
                list of ARM IDs of the given scope type which will be the target
                of the given action rule.
            type: list
      conditions:
        description:
          - conditions on which alerts will be filtered
        type: dict
        suboptions:
          severity:
            description:
              - filter alerts by severity
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
          monitor_service:
            description:
              - filter alerts by monitor service
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
          monitor_condition:
            description:
              - filter alerts by monitor condition
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
          target_resource_type:
            description:
              - filter alerts by target resource type
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
          alert_rule_id:
            description:
              - filter alerts by alert rule id
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
          description:
            description:
              - filter alerts by alert rule description
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
          alert_context:
            description:
              - filter alerts by alert context (payload)
            type: dict
            suboptions:
              operator:
                description:
                  - operator for a given condition
                type: str
              values:
                description:
                  - list of values to match for a given condition.
                type: list
      description:
        description:
          - Description of action rule
        type: str
      created_at:
        description:
          - Creation time of action rule. Date-Time in ISO-8601 format.
        type: datetime
      last_modified_at:
        description:
          - Last updated time of action rule. Date-Time in ISO-8601 format.
        type: datetime
      created_by:
        description:
          - Created by user name.
        type: str
      last_modified_by:
        description:
          - Last modified by user name.
        type: str
      status:
        description:
          - Indicates if the given action rule is enabled or disabled
        type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: GetActionRulesSubscriptionWide
  azure.rm.alertsmanagementactionrule.info: {}
- name: GetActionRulesResourceGroupWide
  azure.rm.alertsmanagementactionrule.info:
    resource_group: myResourceGroup
- name: GetActionRuleById
  azure.rm.alertsmanagementactionrule.info:
    resource_group: myResourceGroup
    name: myActionRule

'''

RETURN = '''
action_rules:
  description: >-
    A list of dict results where the key is the name of the ActionRule and the
    values are the facts for that ActionRule.
  returned: always
  type: complex
  contains:
    actionrule_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - URL to fetch the next set of action rules
          returned: always
          type: str
          sample: null
        value:
          description:
            - List of action rules
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Azure resource Id
              returned: always
              type: str
              sample: null
            type:
              description:
                - Azure resource type
              returned: always
              type: str
              sample: null
            name:
              description:
                - Azure resource name
              returned: always
              type: str
              sample: null
            location:
              description:
                - Resource location
              returned: always
              type: str
              sample: null
            tags:
              description:
                - Resource tags
              returned: always
              type: >-
                unknown[DictionaryType
                {"$id":"117","$type":"DictionaryType","valueType":{"$id":"118","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"119","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"120","fixed":false},"deprecated":false}]
              sample: null
            properties:
              description:
                - action rule properties
              returned: always
              type: dict
              sample: null
            scope:
              description:
                - scope on which action rule will apply
              returned: always
              type: dict
              sample: null
              contains:
                scope_type:
                  description:
                    - type of target scope
                  returned: always
                  type: str
                  sample: null
                values:
                  description:
                    - >-
                      list of ARM IDs of the given scope type which will be the
                      target of the given action rule.
                  returned: always
                  type: str
                  sample: null
            conditions:
              description:
                - conditions on which alerts will be filtered
              returned: always
              type: dict
              sample: null
              contains:
                severity:
                  description:
                    - filter alerts by severity
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
                monitor_service:
                  description:
                    - filter alerts by monitor service
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
                monitor_condition:
                  description:
                    - filter alerts by monitor condition
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
                target_resource_type:
                  description:
                    - filter alerts by target resource type
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
                alert_rule_id:
                  description:
                    - filter alerts by alert rule id
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
                description:
                  description:
                    - filter alerts by alert rule description
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
                alert_context:
                  description:
                    - filter alerts by alert context (payload)
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    operator:
                      description:
                        - operator for a given condition
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - list of values to match for a given condition.
                      returned: always
                      type: str
                      sample: null
            description:
              description:
                - Description of action rule
              returned: always
              type: str
              sample: null
            created_at:
              description:
                - Creation time of action rule. Date-Time in ISO-8601 format.
              returned: always
              type: datetime
              sample: null
            last_modified_at:
              description:
                - >-
                  Last updated time of action rule. Date-Time in ISO-8601
                  format.
              returned: always
              type: datetime
              sample: null
            created_by:
              description:
                - Created by user name.
              returned: always
              type: str
              sample: null
            last_modified_by:
              description:
                - Last modified by user name.
              returned: always
              type: str
              sample: null
            status:
              description:
                - Indicates if the given action rule is enabled or disabled
              returned: always
              type: str
              sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMActionRulesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            target_resource_group=dict(
                type='str'
            ),
            target_resource_type=dict(
                type='str'
            ),
            target_resource=dict(
                type='str'
            ),
            severity=dict(
                type='str'
            ),
            monitor_service=dict(
                type='str'
            ),
            impacted_scope=dict(
                type='str'
            ),
            description=dict(
                type='str'
            ),
            alert_rule_id=dict(
                type='str'
            ),
            action_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.target_resource_group = None
        self.target_resource_type = None
        self.target_resource = None
        self.severity = None
        self.monitor_service = None
        self.impacted_scope = None
        self.description = None
        self.alert_rule_id = None
        self.action_group = None
        self.name = None
        self.resource_group = None
        self.name = None
        self.next_link = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = 'undefined'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMActionRulesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['action_rules'] = self.format_item(self.getbyname())
        elif (self.resource_group is not None):
            self.results['action_rules'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['action_rules'] = [self.format_item(self.listbysubscription())]
        return self.results

    def getbyname(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/actionRules' +
                    '/{{ action_rule_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ action_rule_name }}', self.name)

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

    def listbyresourcegroup(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/actionRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ action_rule_name }}', self.name)

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

    def listbysubscription(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/actionRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ action_rule_name }}', self.name)

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
    AzureRMActionRulesInfo()


if __name__ == '__main__':
    main()
