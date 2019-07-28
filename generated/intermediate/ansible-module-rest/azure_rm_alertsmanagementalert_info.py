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
module: azure_rm_alertsmanagementalert_info
version_added: '2.9'
short_description: Get Alert info.
description:
  - Get info of Alert.
options:
  identifier:
    description:
      - Identification of the information to be retrieved by API call.
    type: str
  target_resource:
    description:
      - >-
        Filter by target resource( which is full ARM ID) Default value is select
        all.
    type: str
  target_resource_type:
    description:
      - Filter by target resource type. Default value is select all.
    type: str
  target_resource_group:
    description:
      - Filter by target resource group name. Default value is select all.
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
  alert_state:
    description:
      - Filter by state of the alert instance. Default value is to select all.
    type: str
  alert_rule:
    description:
      - Filter by specific alert rule.  Default value is to select all.
    type: str
  smart_group_id:
    description:
      - Filter the alerts list by the Smart Group Id. Default value is none.
    type: str
  include_context:
    description:
      - >-
        Include context which has contextual data specific to the monitor
        service. Default value is false'
    type: boolean
  include_egress_config:
    description:
      - >-
        Include egress config which would be used for displaying the content in
        portal.  Default value is 'false'.
    type: boolean
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
        Sort the query results by input field,  Default value is
        'lastModifiedDateTime'.
    type: str
  sort_order:
    description:
      - >-
        Sort the query results order in either ascending or descending.  Default
        value is 'desc' for time fields and 'asc' for others.
    type: str
  select:
    description:
      - >-
        This filter allows to selection of the fields(comma separated) which
        would  be part of the essential section. This would allow to project
        only the  required fields rather than getting entire content.  Default
        is to fetch all the fields in the essentials section.
    type: str
  time_range:
    description:
      - Filter by time range by below listed values. Default value is 1 day.
    type: str
  custom_time_range:
    description:
      - >-
        Filter by custom time range in the format <start-time>/<end-time>  where
        time is in (ISO-8601 format)'. Permissible values is within 30 days
        from  query time. Either timeRange or customTimeRange could be used but
        not both. Default is none.
    type: str
  groupby:
    description:
      - >-
        This parameter allows the result set to be grouped by input fields
        (Maximum 2 comma separated fields supported). For example,
        groupby=severity or groupby=severity,alertstate.
    type: str
  include_smart_groups_count:
    description:
      - >-
        Include count of the SmartGroups as part of the summary. Default value
        is 'false'.
    type: boolean
  alert_id:
    description:
      - Unique ID of an alert instance.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: MonService
  azure_rm_alertsmanagementalert_info:
    identifier: MonitorServiceList
- name: ListAlerts
  azure_rm_alertsmanagementalert_info: {}
- name: Summary
  azure_rm_alertsmanagementalert_info:
    groupby: 'severity,alertState'
- name: GetById
  azure_rm_alertsmanagementalert_info:
    alert_id: myAlert
- name: Resolve
  azure_rm_alertsmanagementalert_info:
    alert_id: myAlert

'''

RETURN = '''
alerts:
  description: >-
    A list of dict results where the key is the name of the Alert and the values
    are the facts for that Alert.
  returned: always
  type: complex
  contains:
    alert_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMAlertsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            identifier=dict(
                type='str'
            ),
            target_resource=dict(
                type='str'
            ),
            target_resource_type=dict(
                type='str'
            ),
            target_resource_group=dict(
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
            alert_state=dict(
                type='str'
            ),
            alert_rule=dict(
                type='str'
            ),
            smart_group_id=dict(
                type='str'
            ),
            include_context=dict(
                type='boolean'
            ),
            include_egress_config=dict(
                type='boolean'
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
            select=dict(
                type='str'
            ),
            time_range=dict(
                type='str'
            ),
            custom_time_range=dict(
                type='str'
            ),
            groupby=dict(
                type='str'
            ),
            include_smart_groups_count=dict(
                type='boolean'
            ),
            alert_id=dict(
                type='str'
            )
        )

        self.identifier = None
        self.target_resource = None
        self.target_resource_type = None
        self.target_resource_group = None
        self.monitor_service = None
        self.monitor_condition = None
        self.severity = None
        self.alert_state = None
        self.alert_rule = None
        self.smart_group_id = None
        self.include_context = None
        self.include_egress_config = None
        self.page_count = None
        self.sort_by = None
        self.sort_order = None
        self.select = None
        self.time_range = None
        self.custom_time_range = None
        self.groupby = None
        self.include_smart_groups_count = None
        self.alert_id = None
        self.properties = None

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
        super(AzureRMAlertsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.alert_id is not None):
            self.results['alerts'] = self.format_item(self.gethistory())
        elif (self.alert_id is not None):
            self.results['alerts'] = self.format_item(self.getbyid())
        elif (self.groupby is not None):
            self.results['alerts'] = self.format_item(self.getsummary())
        else:
            self.results['alerts'] = [self.format_item(self.getall())]
        elif (self.identifier is not None):
            self.results['alerts'] = self.format_item(self.metadata())
        return self.results

    def gethistory(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/alerts' +
                    '/{{ alert_name }}' +
                    '/history')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ alert_name }}', self.name)

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
                    '/alerts' +
                    '/{{ alert_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ alert_name }}', self.name)

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

    def getsummary(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/alertsSummary')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ alert_name }}', self.name)

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
                    '/alerts')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ alert_name }}', self.name)

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

    def metadata(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/providers' +
                    '/Microsoft.AlertsManagement' +
                    '/alertsMetaData')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ alert_name }}', self.name)

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
    AzureRMAlertsInfo()


if __name__ == '__main__':
    main()
