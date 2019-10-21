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
module: alertsmanagementactionrule
version_added: '2.9'
short_description: Manage Azure ActionRule instance.
description:
  - 'Create, update and delete instance of Azure ActionRule.'
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
      - filter by action rule name
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
  state:
    description:
      - Assert the state of the ActionRule.
      - >-
        Use C(present) to create or update an ActionRule and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
[]

'''

RETURN = '''
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
              list of ARM IDs of the given scope type which will be the target
              of the given action rule.
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
        - Last updated time of action rule. Date-Time in ISO-8601 format.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMActionRules(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            target_resource_group=dict(
                type='str',
                updatable=False,
                disposition='targetResourceGroup'
            ),
            target_resource_type=dict(
                type='str',
                updatable=False,
                disposition='targetResourceType'
            ),
            target_resource=dict(
                type='str',
                updatable=False,
                disposition='targetResource'
            ),
            severity=dict(
                type='str',
                updatable=False
            ),
            monitor_service=dict(
                type='str',
                updatable=False,
                disposition='monitorService'
            ),
            impacted_scope=dict(
                type='str',
                updatable=False,
                disposition='impactedScope'
            ),
            description=dict(
                type='str',
                updatable=False
            ),
            alert_rule_id=dict(
                type='str',
                updatable=False,
                disposition='alertRuleId'
            ),
            action_group=dict(
                type='str',
                updatable=False,
                disposition='actionGroup'
            ),
            name=dict(
                type='str',
                updatable=False
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
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
        self.next_link = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = 'undefined'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMActionRules, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/actionRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("ActionRule instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ActionRule instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ActionRule instance')

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
            self.log('ActionRule instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ActionRule instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["next_link"] = response["next_link"]
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ActionRule instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the ActionRule instance.')
            self.fail('Error creating the ActionRule instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ActionRule instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ActionRule instance.')
            self.fail('Error deleting the ActionRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ActionRule instance {0} is present'.format(self.))
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
            # self.log("ActionRule instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ActionRule instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMActionRules()


if __name__ == '__main__':
    main()
