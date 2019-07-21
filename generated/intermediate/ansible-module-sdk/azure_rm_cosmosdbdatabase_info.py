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
module: azure_rm_cosmosdbdatabase_info
version_added: '2.9'
short_description: Get Database info.
description:
  - Get info of Database.
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
  database_rid:
    description:
      - Cosmos DB database rid.
    required: true
    type: str
  value:
    description:
      - The list of usages for the database. A usage is a point in time metric
    type: list
    suboptions:
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
      quota_period:
        description:
          - The quota period used to summarize the usage values.
        type: str
      limit:
        description:
          - Maximum value for this metric
        type: number
      current_value:
        description:
          - Current value for this metric
        type: number
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: CosmosDBDatabaseGetUsages
  azure_rm_cosmosdbdatabase_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBDatabaseGetMetrics
  azure_rm_cosmosdbdatabase_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBDatabaseGetMetricDefinitions
  azure_rm_cosmosdbdatabase_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_rid: myDatabase

'''

RETURN = '''
database:
  description: >-
    A list of dict results where the key is the name of the Database and the
    values are the facts for that Database.
  returned: always
  type: complex
  contains:
    database_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - >-
              The list of usages for the database. A usage is a point in time
              metric
          returned: always
          type: dict
          sample: null
          contains:
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
            quota_period:
              description:
                - The quota period used to summarize the usage values.
              returned: always
              type: str
              sample: null
            limit:
              description:
                - Maximum value for this metric
              returned: always
              type: number
              sample: null
            current_value:
              description:
                - Current value for this metric
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


class AzureRMDatabaseInfo(AzureRMModuleBase):
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
            database_rid=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.account_name = None
        self.database_rid = None
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
        super(AzureRMDatabaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.database_rid is not None):
            self.results['database'] = self.format_item(self.listmetricdefinitions())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_rid is not None):
            self.results['database'] = self.format_item(self.listmetrics())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_rid is not None):
            self.results['database'] = self.format_item(self.listusages())
        return self.results

    def listmetricdefinitions(self):
        response = None

        try:
            response = self.mgmt_client.database.list_metric_definitions(resource_group_name=self.resource_group,
                                                                         account_name=self.account_name,
                                                                         database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listmetrics(self):
        response = None

        try:
            response = self.mgmt_client.database.list_metrics(resource_group_name=self.resource_group,
                                                              account_name=self.account_name,
                                                              database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listusages(self):
        response = None

        try:
            response = self.mgmt_client.database.list_usages(resource_group_name=self.resource_group,
                                                             account_name=self.account_name,
                                                             database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMDatabaseInfo()


if __name__ == '__main__':
    main()
