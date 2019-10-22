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
module: azure_rm_alertsmanagementsmartgroup
version_added: '2.9'
short_description: Manage Azure SmartGroup instance.
description:
  - 'Create, update and delete instance of Azure SmartGroup.'
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
  state:
    description:
      - Assert the state of the SmartGroup.
      - >-
        Use C(present) to create or update an SmartGroup and C(absent) to delete
        it.
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
[]

'''

RETURN = '''
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
          Severity of smart group is the highest(Sev0 >... > Sev4) severity of
          all the alerts in the group.
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
        - Last updated time of smart group. Date-Time in ISO-8601 format.
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
          The URI to fetch the next page of alerts. Call ListNext() with this
          URI to fetch the next page alerts.
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


class AzureRMSmartGroups(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            target_resource=dict(
                type='str',
                updatable=False,
                disposition='targetResource'
            ),
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
            monitor_service=dict(
                type='str',
                updatable=False,
                disposition='monitorService'
            ),
            monitor_condition=dict(
                type='str',
                updatable=False,
                disposition='monitorCondition'
            ),
            severity=dict(
                type='str',
                updatable=False
            ),
            smart_group_state=dict(
                type='str',
                updatable=False,
                disposition='smartGroupState'
            ),
            time_range=dict(
                type='str',
                updatable=False,
                disposition='timeRange'
            ),
            page_count=dict(
                type='number',
                updatable=False,
                disposition='pageCount'
            ),
            sort_by=dict(
                type='str',
                updatable=False,
                disposition='sortBy'
            ),
            sort_order=dict(
                type='str',
                updatable=False,
                disposition='sortOrder'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
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

        super(AzureRMSmartGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/smartGroups')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("SmartGroup instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('SmartGroup instance already exists')

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
            self.log('Need to Create / Update the SmartGroup instance')

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
            self.log('SmartGroup instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('SmartGroup instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["next_link"] = response["next_link"]
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the SmartGroup instance {0}'.format(self.))

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
            self.log('Error attempting to create the SmartGroup instance.')
            self.fail('Error creating the SmartGroup instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the SmartGroup instance {0}'.format(self.))
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
            self.log('Error attempting to delete the SmartGroup instance.')
            self.fail('Error deleting the SmartGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the SmartGroup instance {0} is present'.format(self.))
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
            # self.log("SmartGroup instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SmartGroup instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMSmartGroups()


if __name__ == '__main__':
    main()
