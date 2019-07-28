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
module: alertsmanagementsmartgroup_info
version_added: '2.9'
short_description: Get SmartGroup info.
description:
  - Get info of SmartGroup.
options:
  target_resource:
    description:
      - >-
        Filter by target resource( which is full ARM ID) Default value is select
        all.
    type: str
  target_resource_group:
    description:
      - Filter by target resource group name. Default value is select all.
    type: str
  target_resource_type:
    description:
      - Filter by target resource type. Default value is select all.
    type: str
  monitor_service:
    description:
      - >-
        Filter by monitor service which generates the alert instance. Default
        value is select all.
    type: str
  monitor_condition:
    description:
      - >-
        Filter by monitor condition which is either 'Fired' or 'Resolved'.
        Default value is to select all.
    type: str
  severity:
    description:
      - Filter by severity.  Default value is select all.
    type: str
  smart_group_state:
    description:
      - Filter by state of the smart group. Default value is to select all.
    type: str
  time_range:
    description:
      - Filter by time range by below listed values. Default value is 1 day.
    type: str
  page_count:
    description:
      - >-
        Determines number of alerts returned per page in response. Permissible
        value is between 1 to 250. When the "includeContent"  filter is
        selected, maximum value allowed is 25. Default value is 25.
    type: number
  sort_by:
    description:
      - >-
        Sort the query results by input field. Default value is sort by
        'lastModifiedDateTime'.
    type: str
  sort_order:
    description:
      - >-
        Sort the query results order in either ascending or descending.  Default
        value is 'desc' for time fields and 'asc' for others.
    type: str
  smart_group_id:
    description:
      - 'Smart group unique id. '
    type: str
  next_link:
    description:
      - URL to fetch the next set of alerts.
    type: str
  value:
    description:
      - List of alerts
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
      alerts_count:
        description:
          - Total number of alerts in smart group
        type: number
      smart_group_state:
        description:
          - Smart group state
        type: str
      severity:
        description:
          - >-
            Severity of smart group is the highest(Sev0 >... > Sev4) severity of
            all the alerts in the group.
        type: str
      start_date_time:
        description:
          - Creation time of smart group. Date-Time in ISO-8601 format.
        type: datetime
      last_modified_date_time:
        description:
          - Last updated time of smart group. Date-Time in ISO-8601 format.
        type: datetime
      last_modified_user_name:
        description:
          - Last modified by user name.
        type: str
      resources:
        description:
          - Summary of target resources in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      resource_types:
        description:
          - Summary of target resource types in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      resource_groups:
        description:
          - Summary of target resource groups in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      monitor_services:
        description:
          - Summary of monitorServices in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      monitor_conditions:
        description:
          - Summary of monitorConditions in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      alert_states:
        description:
          - Summary of alertStates in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      alert_severities:
        description:
          - Summary of alertSeverities in the smart group
        type: list
        suboptions:
          name:
            description:
              - Name of the type.
            type: str
          count:
            description:
              - Total number of items of type.
            type: number
      next_link:
        description:
          - >-
            The URI to fetch the next page of alerts. Call ListNext() with this
            URI to fetch the next page alerts.
        type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List
  azure.rm.alertsmanagementsmartgroup.info: {}
- name: Get
  azure.rm.alertsmanagementsmartgroup.info:
    smart_group_id: mySmartGroup
- name: Resolve
  azure.rm.alertsmanagementsmartgroup.info:
    smart_group_id: mySmartGroup

'''

RETURN = '''
smart_groups:
  description: >-
    A list of dict results where the key is the name of the SmartGroup and the
    values are the facts for that SmartGroup.
  returned: always
  type: complex
  contains:
    smartgroup_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - URL to fetch the next set of alerts.
          returned: always
          type: str
          sample: null
        value:
          description:
            - List of alerts
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
            properties:
              description:
                - ''
              returned: always
              type: dict
              sample: null
            alerts_count:
              description:
                - Total number of alerts in smart group
              returned: always
              type: number
              sample: null
            smart_group_state:
              description:
                - Smart group state
              returned: always
              type: str
              sample: null
            severity:
              description:
                - >-
                  Severity of smart group is the highest(Sev0 >... > Sev4)
                  severity of all the alerts in the group.
              returned: always
              type: str
              sample: null
            start_date_time:
              description:
                - Creation time of smart group. Date-Time in ISO-8601 format.
              returned: always
              type: datetime
              sample: null
            last_modified_date_time:
              description:
                - >-
                  Last updated time of smart group. Date-Time in ISO-8601
                  format.
              returned: always
              type: datetime
              sample: null
            last_modified_user_name:
              description:
                - Last modified by user name.
              returned: always
              type: str
              sample: null
            resources:
              description:
                - Summary of target resources in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            resource_types:
              description:
                - Summary of target resource types in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            resource_groups:
              description:
                - Summary of target resource groups in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            monitor_services:
              description:
                - Summary of monitorServices in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            monitor_conditions:
              description:
                - Summary of monitorConditions in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            alert_states:
              description:
                - Summary of alertStates in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            alert_severities:
              description:
                - Summary of alertSeverities in the smart group
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the type.
                  returned: always
                  type: str
                  sample: null
                count:
                  description:
                    - Total number of items of type.
                  returned: always
                  type: number
                  sample: null
            next_link:
              description:
                - >-
                  The URI to fetch the next page of alerts. Call ListNext() with
                  this URI to fetch the next page alerts.
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


class AzureRMSmartGroupsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            target_resource=dict(
                type='str'
            ),
            target_resource_group=dict(
                type='str'
            ),
            target_resource_type=dict(
                type='str'
            ),
            monitor_service=dict(
                type='str'
            ),
            monitor_condition=dict(
                type='str'
            ),
            severity=dict(
                type='str'
            ),
            smart_group_state=dict(
                type='str'
            ),
            time_range=dict(
                type='str'
            ),
            page_count=dict(
                type='number'
            ),
            sort_by=dict(
                type='str'
            ),
            sort_order=dict(
                type='str'
            ),
            smart_group_id=dict(
                type='str'
            )
        )

        self.target_resource = None
        self.target_resource_group = None
        self.target_resource_type = None
        self.monitor_service = None
        self.monitor_condition = None
        self.severity = None
        self.smart_group_state = None
        self.time_range = None
        self.page_count = None
        self.sort_by = None
        self.sort_order = None
        self.smart_group_id = None
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
        super(AzureRMSmartGroupsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.smart_group_id is not None):
            self.results['smart_groups'] = self.format_item(self.gethistory())
        elif (self.smart_group_id is not None):
            self.results['smart_groups'] = self.format_item(self.getbyid())
        else:
            self.results['smart_groups'] = [self.format_item(self.getall())]
        return self.results

    def gethistory(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/smartGroups' +
                    '/{{ smart_group_name }}' +
                    '/history')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ smart_group_name }}', self.name)

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

    def getbyid(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/smartGroups' +
                    '/{{ smart_group_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ smart_group_name }}', self.name)

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

    def getall(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/smartGroups')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ smart_group_name }}', self.name)

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
    AzureRMSmartGroupsInfo()


if __name__ == '__main__':
    main()
