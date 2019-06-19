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
  account_name:
    description:
      - Cosmos DB database account name.
  table_name:
    description:
      - Cosmos DB table name.
  database_name:
    description:
      - Cosmos DB database name.
  keyspace_name:
    description:
      - Cosmos DB keyspace name.
  graph_name:
    description:
      - Cosmos DB graph name.
  container_name:
    description:
      - Cosmos DB container name.
  name:
    description:
      - The name of the database account.
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
      is_zone_redundant:
        description:
          - >-
            Flag to indicate whether or not this region is an AvailabilityZone
            region
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
      is_zone_redundant:
        description:
          - >-
            Flag to indicate whether or not this region is an AvailabilityZone
            region
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
    account_name: myDatabaseAccount
- name: CosmosDBDatabaseAccountGetUsages
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBDatabaseAccountGetMetrics
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBDatabaseAccountListReadOnlyKeys
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBDatabaseAccountGetMetricDefinitions
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBTableList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBSqlDatabaseList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBMongoDBDatabaseList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBGremlinDatabaseList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBCassandraKeyspaceList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
- name: CosmosDBTableGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    table_name: myTable
- name: CosmosDBSqlDatabaseGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBMongoDBDatabaseGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBGremlinDatabaseGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBCassandraKeyspaceGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    keyspace_name: myKeyspace
- name: CosmosDBGremlinGraphList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBSqlContainerList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBCassandraTableList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    keyspace_name: myKeyspace
- name: CosmosDBTableThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    table_name: myTable
- name: CosmosDBMongoDBCollectionList
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBSqlDatabaseThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBGremlinGraphGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
    graph_name: myGraph
- name: CosmosDBGremlinDatabaseThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBMongoDBDatabaseThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
- name: CosmosDBCassandraTableGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    table_name: myTable
    keyspace_name: myKeyspace
- name: CosmosDBCassandraKeyspaceThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    keyspace_name: myKeyspace
- name: CosmosDBSqlContainerGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
    container_name: myContainer
- name: CosmosDBMongoDBCollectionGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
    name: myCollection
- name: CosmosDBGremlinGraphThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
    graph_name: myGraph
- name: CosmosDBCassandraTableThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    table_name: myTable
    keyspace_name: myKeyspace
- name: CosmosDBSqlContainerThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
    container_name: myContainer
- name: CosmosDBMongoDBCollectionThroughputGet
  azure_rm_cosmosdbdatabaseaccount_info:
    resource_group: myResourceGroup
    account_name: myDatabaseAccount
    database_name: myDatabase
    name: myCollection

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
            {"$id":"235","$type":"DictionaryType","valueType":{"$id":"236","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"237","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"238","fixed":false},"deprecated":false}]
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMDatabaseAccountsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            account_name=dict(
                type='str'
            ),
            table_name=dict(
                type='str'
            ),
            database_name=dict(
                type='str'
            ),
            keyspace_name=dict(
                type='str'
            ),
            graph_name=dict(
                type='str'
            ),
            container_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.account_name = None
        self.table_name = None
        self.database_name = None
        self.keyspace_name = None
        self.graph_name = None
        self.container_name = None
        self.name = None
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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.database_name is not None and
            self.name is not None):
            self.results['database_accounts'] = self.format_item(self.getmongodbcollectionthroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['database_accounts'] = self.format_item(self.getsqlcontainerthroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.graph_name is not None):
            self.results['database_accounts'] = self.format_item(self.getgremlingraphthroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.keyspace_name is not None and
              self.table_name is not None):
            self.results['database_accounts'] = self.format_item(self.getcassandratablethroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.name is not None):
            self.results['database_accounts'] = self.format_item(self.getmongodbcollection())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.container_name is not None):
            self.results['database_accounts'] = self.format_item(self.getsqlcontainer())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.keyspace_name is not None):
            self.results['database_accounts'] = self.format_item(self.getcassandrakeyspacethroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.getsqldatabasethroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.getgremlindatabasethroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.getmongodbdatabasethroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.keyspace_name is not None and
              self.table_name is not None):
            self.results['database_accounts'] = self.format_item(self.getcassandratable())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None and
              self.graph_name is not None):
            self.results['database_accounts'] = self.format_item(self.getgremlingraph())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.table_name is not None):
            self.results['database_accounts'] = self.format_item(self.gettablethroughput())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.listmongodbcollections())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.listsqlcontainers())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.keyspace_name is not None):
            self.results['database_accounts'] = self.format_item(self.listcassandratables())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.listgremlingraphs())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.getsqldatabase())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.getgremlindatabase())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.keyspace_name is not None):
            self.results['database_accounts'] = self.format_item(self.getcassandrakeyspace())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.database_name is not None):
            self.results['database_accounts'] = self.format_item(self.getmongodbdatabase())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.table_name is not None):
            self.results['database_accounts'] = self.format_item(self.gettable())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listcassandrakeyspaces())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listgremlindatabases())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listsqldatabases())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listmongodbdatabases())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listtables())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listmetricdefinitions())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.getreadonlykeys())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listmetrics())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.listusages())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['database_accounts'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['database_accounts'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['database_accounts'] = [self.format_item(self.list())]
        return self.results

    def getmongodbcollectionthroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/collections' +
                    '/{{ collection_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getsqlcontainerthroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/containers' +
                    '/{{ container_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getgremlingraphthroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/graphs' +
                    '/{{ graph_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getcassandratablethroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/keyspaces' +
                    '/{{ keyspace_name }}' +
                    '/tables' +
                    '/{{ table_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getmongodbcollection(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/collections' +
                    '/{{ collection_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getsqlcontainer(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/containers' +
                    '/{{ container_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getcassandrakeyspacethroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/keyspaces' +
                    '/{{ keyspace_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getsqldatabasethroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getgremlindatabasethroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getmongodbdatabasethroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getcassandratable(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/keyspaces' +
                    '/{{ keyspace_name }}' +
                    '/tables' +
                    '/{{ table_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getgremlingraph(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/graphs' +
                    '/{{ graph_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def gettablethroughput(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/tables' +
                    '/{{ table_name }}' +
                    '/settings' +
                    '/{{ setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listmongodbcollections(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/collections')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listsqlcontainers(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/containers')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listcassandratables(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/keyspaces' +
                    '/{{ keyspace_name }}' +
                    '/tables')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listgremlingraphs(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/graphs')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getsqldatabase(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getgremlindatabase(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getcassandrakeyspace(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/keyspaces' +
                    '/{{ keyspace_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getmongodbdatabase(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases' +
                    '/{{ database_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def gettable(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/tables' +
                    '/{{ table_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listcassandrakeyspaces(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/keyspaces')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listgremlindatabases(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listsqldatabases(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listmongodbdatabases(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/databases')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listtables(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/apis' +
                    '/{{ apis_name }}' +
                    '/tables')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listmetricdefinitions(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/metricDefinitions')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def getreadonlykeys(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/readonlykeys')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listmetrics(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/metrics')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def listusages(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/usages')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ apis_name }}', self.apis_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ setting_name }}', self.name)

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
    AzureRMDatabaseAccountsInfo()


if __name__ == '__main__':
    main()
