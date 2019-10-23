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
module: azure_rm_cosmosdbpercentiletarget
version_added: '2.9'
short_description: Manage Azure PercentileTarget instance.
description:
  - 'Create, update and delete instance of Azure PercentileTarget.'
options:
  resource_group:
    description:
      - Name of an Azure resource group.
    required: true
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    required: true
    type: str
  target_region:
    description:
      - >-
        Target region to which data is written. Cosmos DB region, with spaces
        between words and each word capitalized.
    required: true
    type: str
  value:
    description:
      - The list of percentile metrics for the account.
    type: list
    suboptions:
      start_time:
        description:
          - The start time for the metric (ISO-8601 format).
        type: datetime
      end_time:
        description:
          - The end time for the metric (ISO-8601 format).
        type: datetime
      time_grain:
        description:
          - The time grain to be used to summarize the metric values.
        type: str
      unit:
        description:
          - The unit of the metric.
        type: str
      name:
        description:
          - The name information for the metric.
        type: dict
        suboptions:
          value:
            description:
              - The name of the metric.
            type: str
          localized_value:
            description:
              - The friendly name of the metric.
            type: str
      metric_values:
        description:
          - >-
            The percentile metric values for the specified time window and
            timestep.
        type: list
        suboptions:
          _count:
            description:
              - The number of values for the metric.
            type: number
          average:
            description:
              - The average value of the metric.
            type: number
          maximum:
            description:
              - The max value of the metric.
            type: number
          minimum:
            description:
              - The min value of the metric.
            type: number
          timestamp:
            description:
              - The metric timestamp (ISO-8601 format).
            type: datetime
          total:
            description:
              - The total value of the metric.
            type: number
          p10:
            description:
              - The 10th percentile value for the metric.
            type: number
          p25:
            description:
              - The 25th percentile value for the metric.
            type: number
          p50:
            description:
              - The 50th percentile value for the metric.
            type: number
          p75:
            description:
              - The 75th percentile value for the metric.
            type: number
          p90:
            description:
              - The 90th percentile value for the metric.
            type: number
          p95:
            description:
              - The 95th percentile value for the metric.
            type: number
          p99:
            description:
              - The 99th percentile value for the metric.
            type: number
  state:
    description:
      - Assert the state of the PercentileTarget.
      - >-
        Use C(present) to create or update an PercentileTarget and C(absent) to
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
[]

'''

RETURN = '''
value:
  description:
    - The list of percentile metrics for the account.
  returned: always
  type: dict
  sample: null
  contains:
    start_time:
      description:
        - The start time for the metric (ISO-8601 format).
      returned: always
      type: datetime
      sample: null
    end_time:
      description:
        - The end time for the metric (ISO-8601 format).
      returned: always
      type: datetime
      sample: null
    time_grain:
      description:
        - The time grain to be used to summarize the metric values.
      returned: always
      type: str
      sample: null
    unit:
      description:
        - The unit of the metric.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name information for the metric.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - The name of the metric.
          returned: always
          type: str
          sample: null
        localized_value:
          description:
            - The friendly name of the metric.
          returned: always
          type: str
          sample: null
    metric_values:
      description:
        - >-
          The percentile metric values for the specified time window and
          timestep.
      returned: always
      type: dict
      sample: null
      contains:
        _count:
          description:
            - The number of values for the metric.
          returned: always
          type: number
          sample: null
        average:
          description:
            - The average value of the metric.
          returned: always
          type: number
          sample: null
        maximum:
          description:
            - The max value of the metric.
          returned: always
          type: number
          sample: null
        minimum:
          description:
            - The min value of the metric.
          returned: always
          type: number
          sample: null
        timestamp:
          description:
            - The metric timestamp (ISO-8601 format).
          returned: always
          type: datetime
          sample: null
        total:
          description:
            - The total value of the metric.
          returned: always
          type: number
          sample: null
        p10:
          description:
            - The 10th percentile value for the metric.
          returned: always
          type: number
          sample: null
        p25:
          description:
            - The 25th percentile value for the metric.
          returned: always
          type: number
          sample: null
        p50:
          description:
            - The 50th percentile value for the metric.
          returned: always
          type: number
          sample: null
        p75:
          description:
            - The 75th percentile value for the metric.
          returned: always
          type: number
          sample: null
        p90:
          description:
            - The 90th percentile value for the metric.
          returned: always
          type: number
          sample: null
        p95:
          description:
            - The 95th percentile value for the metric.
          returned: always
          type: number
          sample: null
        p99:
          description:
            - The 99th percentile value for the metric.
          returned: always
          type: number
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.cosmosdb import CosmosDBClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPercentileTarget(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            account_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            target_region=dict(
                type='str',
                updatable=False,
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.target_region = None
        self.value = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPercentileTarget, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDB,
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
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.percentile_target.create()
            else:
                response = self.mgmt_client.percentile_target.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PercentileTarget instance.')
            self.fail('Error creating the PercentileTarget instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the PercentileTarget instance {0}'.format(self.))
        try:
            response = self.mgmt_client.percentile_target.delete()
        except CloudError as e:
            self.log('Error attempting to delete the PercentileTarget instance.')
            self.fail('Error deleting the PercentileTarget instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the PercentileTarget instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.percentile_target.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPercentileTarget()


if __name__ == '__main__':
    main()