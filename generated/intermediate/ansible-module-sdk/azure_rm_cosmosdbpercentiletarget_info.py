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
module: azure_rm_cosmosdbpercentiletarget_info
version_added: '2.9'
short_description: Get PercentileTarget info.
description:
  - Get info of PercentileTarget.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: CosmosDBDatabaseAccountRegionGetMetrics
  azure_rm_cosmosdbpercentiletarget_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    target_region: myTargetRegion

'''

RETURN = '''
percentile_target:
  description: >-
    A list of dict results where the key is the name of the PercentileTarget and
    the values are the facts for that PercentileTarget.
  returned: always
  type: complex
  contains:
    percentiletarget_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.cosmosdb import CosmosDBClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPercentileTargetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            account_name=dict(
                type='str',
                required=true
            ),
            target_region=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.account_name = None
        self.target_region = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-04-08'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPercentileTargetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.target_region is not None):
            self.results['percentile_target'] = self.format_item(self.listmetrics())
        return self.results

    def listmetrics(self):
        response = None

        try:
            response = self.mgmt_client.percentile_target.list_metrics(resource_group_name=self.resource_group,
                                                                       account_name=self.account_name,
                                                                       target_region=self.target_region)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMPercentileTargetInfo()


if __name__ == '__main__':
    main()
