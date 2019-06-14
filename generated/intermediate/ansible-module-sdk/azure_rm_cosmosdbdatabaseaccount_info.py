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
module: azure_rm_cosmosdbdatabaseaccount_info
version_added: '2.9'
short_description: Get DatabaseAccount info.
description:
  - Get info of DatabaseAccount.
options:
  resource_group:
    description:
      - Name of an Azure resource group.
  name:
    description:
      - The name of the database account.
  table_rid:
    description:
      - Cosmos DB table rid.
  database_rid:
    description:
      - Cosmos DB database rid.
  keyspace_rid:
    description:
      - Cosmos DB keyspace rid.
  container_rid:
    description:
      - Cosmos DB container rid.
  collection_rid:
    description:
      - Cosmos DB collection rid.
  id:
    description:
      - The unique resource identifier of the database account.
  type:
    description:
      - The type of Azure resource.
  location:
    description:
      - The location of the resource group to which the resource belongs.
  kind:
    description:
      - >-
        Indicates the type of database account. This can only be set at database
        account creation.
  provisioning_state:
    description:
      - undefined
  document_endpoint:
    description:
      - The connection endpoint for the Cosmos DB database account.
  database_account_offer_type:
    description:
      - >-
        The offer type for the Cosmos DB database account. Default value:
        Standard.
  ip_range_filter:
    description:
      - >-
        Cosmos DB Firewall Support: This value specifies the set of IP addresses
        or IP address ranges in CIDR form to be included as the allowed list of
        client IPs for a given database account. IP addresses/ranges must be
        comma separated and must not contain any spaces.
  is_virtual_network_filter_enabled:
    description:
      - Flag to indicate whether to enable/disable Virtual Network ACL rules.
  enable_automatic_failover:
    description:
      - >-
        Enables automatic failover of the write region in the rare event that
        the region is unavailable due to an outage. Automatic failover will
        result in a new write region for the account and is chosen based on the
        failover priorities configured for the account.
  consistency_policy:
    description:
      - The consistency policy for the Cosmos DB database account.
    suboptions:
      default_consistency_level:
        description:
          - >-
            The default consistency level and configuration settings of the
            Cosmos DB account.
        required: true
      max_staleness_prefix:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the number of stale requests tolerated. Accepted range
            for this value is 1 – 2,147,483,647. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
      max_interval_in_seconds:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the time amount of staleness (in seconds) tolerated.
            Accepted range for this value is 5 - 86400. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
  capabilities:
    description:
      - List of Cosmos DB capabilities for the account
    type: list
    suboptions:
      name:
        description:
          - >-
            Name of the Cosmos DB capability. For example, "name":
            "EnableCassandra". Current values also include "EnableTable" and
            "EnableGremlin".
  write_locations:
    description:
      - An array that contains the write location for the Cosmos DB account.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region within the database account.
            Example: &lt;accountName&gt;-&lt;locationName&gt;.
      location_name:
        description:
          - The name of the region.
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
      provisioning_state:
        description:
          - undefined
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  read_locations:
    description:
      - >-
        An array that contains of the read locations enabled for the Cosmos DB
        account.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region within the database account.
            Example: &lt;accountName&gt;-&lt;locationName&gt;.
      location_name:
        description:
          - The name of the region.
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
      provisioning_state:
        description:
          - undefined
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  failover_policies:
    description:
      - An array that contains the regions ordered by their failover priorities.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region in which the database account
            replicates to. Example: &lt;accountName&gt;-&lt;locationName&gt;.
      location_name:
        description:
          - The name of the region in which the database account exists.
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  virtual_network_rules:
    description:
      - List of Virtual Network ACL rules configured for the Cosmos DB account.
    type: list
    suboptions:
      id:
        description:
          - >-
            Resource ID of a subnet, for example:
            /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
      ignore_missing_vnet_service_endpoint:
        description:
          - >-
            Create firewall rule before the virtual network has vnet service
            endpoint enabled.
  enable_multiple_write_locations:
    description:
      - Enables the account to write in multiple locations
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: CosmosDBDatabaseAccountList
  azure_rm_cosmosdbdatabaseaccount_info: {}
- name: CosmosDBDatabaseAccountListByResourceGroup
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
- name: CosmosDBDatabaseAccountGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBDatabaseAccountGetUsages
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBDatabaseAccountGetMetrics
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBDatabaseAccountListReadOnlyKeys
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBDatabaseAccountGetMetricDefinitions
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBTableList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBSqlDatabaseList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBMongoDatabaseList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBGremlinDatabaseList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBCassandraKeyspaceList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBTableGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    table_rid: myTable
- name: CosmosDBSqlDatabaseGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBMongoDatabaseGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBGremlinDatabaseGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBCassandraKeyspaceGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    keyspace_rid: myKeyspace
- name: CosmosDBSqlContainerList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBCassandraTableList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    keyspace_rid: myKeyspace
- name: CosmosDBMongoCollectionList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBGremlinContainerList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
- name: CosmosDBCassandraTableGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    table_rid: myTable
    keyspace_rid: myKeyspace
- name: CosmosDBSqlContainerGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
    container_rid: myContainer
- name: CosmosDBMongoCollectionGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
    collection_rid: myCollection
- name: CosmosDBGremlinContainerGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    database_rid: myDatabase
    container_rid: myContainer

'''

RETURN = '''
database_accounts:
  description: >-
    A list of dict results where the key is the name of the DatabaseAccount and
    the values are the facts for that DatabaseAccount.
  returned: always
  type: complex
  contains:
    databaseaccount_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - The unique resource identifier of the database account.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the database account.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of Azure resource.
          returned: always
          type: str
          sample: null
        location:
          description:
            - The location of the resource group to which the resource belongs.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"229","$type":"DictionaryType","valueType":{"$id":"230","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"231","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"232","fixed":false},"deprecated":false}]
          sample: null
        kind:
          description:
            - >-
              Indicates the type of database account. This can only be set at
              database account creation.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
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
    from azure.mgmt.cosmosdb import CosmosDBClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDatabaseAccountsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            ),
            table_rid=dict(
                type='str'
            ),
            database_rid=dict(
                type='str'
            ),
            keyspace_rid=dict(
                type='str'
            ),
            container_rid=dict(
                type='str'
            ),
            collection_rid=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.table_rid = None
        self.database_rid = None
        self.keyspace_rid = None
        self.container_rid = None
        self.collection_rid = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.tags = None
        self.kind = None
        self.properties = None

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
        super(AzureRMDatabaseAccountsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDBClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.database_rid is not None and
            self.collection_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getmongocollection())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None and
              self.container_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getsqlcontainer())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None and
              self.container_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getgremlincontainer())
        elif (self.resource_group is not None and
              self.name is not None and
              self.keyspace_rid is not None and
              self.table_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getcassandratable())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None):
            self.results['database_accounts'] = self.format_item(self.listmongocollections())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None):
            self.results['database_accounts'] = self.format_item(self.listsqlcontainers())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None):
            self.results['database_accounts'] = self.format_item(self.listgremlincontainers())
        elif (self.resource_group is not None and
              self.name is not None and
              self.keyspace_rid is not None):
            self.results['database_accounts'] = self.format_item(self.listcassandratables())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getsqldatabase())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getmongodatabase())
        elif (self.resource_group is not None and
              self.name is not None and
              self.database_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getgremlindatabase())
        elif (self.resource_group is not None and
              self.name is not None and
              self.keyspace_rid is not None):
            self.results['database_accounts'] = self.format_item(self.getcassandrakeyspace())
        elif (self.resource_group is not None and
              self.name is not None and
              self.table_rid is not None):
            self.results['database_accounts'] = self.format_item(self.gettable())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listcassandrakeyspaces())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listsqldatabases())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listmongodatabases())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listgremlindatabases())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listtables())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listmetricdefinitions())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.getreadonlykeys())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listmetrics())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.listusages())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['database_accounts'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['database_accounts'] = [self.format_item(self.list())]
        return self.results

    def getmongocollection(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_mongo_collection(resource_group_name=self.resource_group,
                                                                               account_name=self.name,
                                                                               database_rid=self.database_rid,
                                                                               collection_rid=self.collection_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getsqlcontainer(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_sql_container(resource_group_name=self.resource_group,
                                                                            account_name=self.name,
                                                                            database_rid=self.database_rid,
                                                                            container_rid=self.container_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getgremlincontainer(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_gremlin_container(resource_group_name=self.resource_group,
                                                                                account_name=self.name,
                                                                                database_rid=self.database_rid,
                                                                                container_rid=self.container_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getcassandratable(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_cassandra_table(resource_group_name=self.resource_group,
                                                                              account_name=self.name,
                                                                              keyspace_rid=self.keyspace_rid,
                                                                              table_rid=self.table_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listmongocollections(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_mongo_collections(resource_group_name=self.resource_group,
                                                                                 account_name=self.name,
                                                                                 database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listsqlcontainers(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_sql_containers(resource_group_name=self.resource_group,
                                                                              account_name=self.name,
                                                                              database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listgremlincontainers(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_gremlin_containers(resource_group_name=self.resource_group,
                                                                                  account_name=self.name,
                                                                                  database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listcassandratables(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_cassandra_tables(resource_group_name=self.resource_group,
                                                                                account_name=self.name,
                                                                                keyspace_rid=self.keyspace_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getsqldatabase(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_sql_database(resource_group_name=self.resource_group,
                                                                           account_name=self.name,
                                                                           database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getmongodatabase(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_mongo_database(resource_group_name=self.resource_group,
                                                                             account_name=self.name,
                                                                             database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getgremlindatabase(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_gremlin_database(resource_group_name=self.resource_group,
                                                                               account_name=self.name,
                                                                               database_rid=self.database_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getcassandrakeyspace(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_cassandra_keyspace(resource_group_name=self.resource_group,
                                                                                 account_name=self.name,
                                                                                 keyspace_rid=self.keyspace_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def gettable(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_table(resource_group_name=self.resource_group,
                                                                    account_name=self.name,
                                                                    table_rid=self.table_rid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listcassandrakeyspaces(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_cassandra_keyspaces(resource_group_name=self.resource_group,
                                                                                   account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listsqldatabases(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_sql_databases(resource_group_name=self.resource_group,
                                                                             account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listmongodatabases(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_mongo_databases(resource_group_name=self.resource_group,
                                                                               account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listgremlindatabases(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_gremlin_databases(resource_group_name=self.resource_group,
                                                                                 account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listtables(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_tables(resource_group_name=self.resource_group,
                                                                      account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listmetricdefinitions(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_metric_definitions(resource_group_name=self.resource_group,
                                                                                  account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getreadonlykeys(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get_read_only_keys(resource_group_name=self.resource_group,
                                                                             account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listmetrics(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_metrics(resource_group_name=self.resource_group,
                                                                       account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listusages(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_usages(resource_group_name=self.resource_group,
                                                                      account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.get(resource_group_name=self.resource_group,
                                                              account_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.database_accounts.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMDatabaseAccountsInfo()


if __name__ == '__main__':
    main()
