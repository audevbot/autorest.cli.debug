# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import time
import mock
import unittest

from azure_devtools.scenario_tests.const import MOCKED_SUBSCRIPTION_ID
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, LiveScenarioTest, ResourceGroupPreparer, create_random_name, live_only, record_only
from azure.cli.core.util import get_file_json


class ResourceGroupScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_rg_scenario')
    def test_resource_group(self, resource_group):

        self.cmd('group create -n {rg} -l westus --tag a=b c', checks=[
            self.check('name', '{rg}'),
            self.check('tags', {'a': 'b', 'c': ''})
        ])

        self.kwargs['sub'] = self.get_subscription_id()
        self.kwargs['name'] = 'zimsxyzname'

        # CosmosDBDatabaseAccountGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountPatch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountCreateMin
        body = (
                 '{'
                 '  "location": "westus",'
                 '  "properties": {'
                 '    "databaseAccountOfferType": "Standard",'
                 '    "locations": ['
                 '      {'
                 '        "failover_priority": "0",'
                 '        "location_name": "southcentralus",'
                 '        "is_zone_redundant": False'
                 '      }'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountCreateMax
        body = (
                 '{'
                 '  "location": "westus",'
                 '  "tags": {},'
                 '  "kind": "GlobalDocumentDB",'
                 '  "properties": {'
                 '    "databaseAccountOfferType": "Standard",'
                 '    "ipRangeFilter": "10.10.10.10",'
                 '    "isVirtualNetworkFilterEnabled": True,'
                 '    "virtualNetworkRules": ['
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",'
                 '        "ignore_missing_vnet_service_endpoint": False'
                 '      }'
                 '    ],'
                 '    "locations": ['
                 '      {'
                 '        "failover_priority": "0",'
                 '        "location_name": "southcentralus",'
                 '        "is_zone_redundant": False'
                 '      },'
                 '      {'
                 '        "failover_priority": "1",'
                 '        "location_name": "eastus",'
                 '        "is_zone_redundant": False'
                 '      }'
                 '    ],'
                 '    "consistencyPolicy": {'
                 '      "defaultConsistencyLevel": "BoundedStaleness",'
                 '      "maxIntervalInSeconds": "10",'
                 '      "maxStalenessPrefix": "200"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountFailoverPriorityChange
        body = (
                 '{'
                 '  "failoverPolicies": ['
                 '    {'
                 '      "location_name": "eastus",'
                 '      "failover_priority": "0"'
                 '    },'
                 '    {'
                 '      "location_name": "westus",'
                 '      "failover_priority": "1"'
                 '    }'
                 '  ]'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/failoverPriorityChange?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.DocumentDB/databaseAccounts?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountListByResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountListKeys
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/listKeys?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountListConnectionStrings
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/listConnectionStrings?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountListConnectionStringsMongo
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/listConnectionStrings?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountOfflineRegion
        body = (
                 '['
                 '  {'
                 '    "region": "North Europe"'
                 '  }'
                 ']'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/offlineRegion?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountOnlineRegion
        body = (
                 '['
                 '  {'
                 '    "region": "North Europe"'
                 '  }'
                 ']'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/onlineRegion?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountListReadOnlyKeys
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/readonlykeys?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountListReadOnlyKeys
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/readonlykeys?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegenerateKey
        body = (
                 '{'
                 '  "keyKind": "primary"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/regenerateKey?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountCheckNameExists
        self.cmd('rest '
                 '--method head '
                 '--uri /providers/Microsoft.DocumentDB/databaseAccountNames/{DATABASE_ACCOUNT_NAME_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountGetUsages
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountGetMetricDefinitions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/metricDefinitions?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlDatabaseList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlDatabaseGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlDatabaseCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "databaseName"'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBSqlDatabaseDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlDatabaseThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlDatabaseThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBSqlContainerList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlContainerGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlContainerCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "containerName",'
                 '      "indexingPolicy": {'
                 '        "indexingMode": "Consistent",'
                 '        "automatic": True,'
                 '        "includedPaths": ['
                 '          {'
                 '            "path": "/*",'
                 '            "indexes": ['
                 '              {'
                 '                "kind": "Range",'
                 '                "data_type": "String",'
                 '                "precision": "-1"'
                 '              },'
                 '              {'
                 '                "kind": "Range",'
                 '                "data_type": "Number",'
                 '                "precision": "-1"'
                 '              }'
                 '            ]'
                 '          }'
                 '        ],'
                 '        "excludedPaths": []'
                 '      },'
                 '      "partitionKey": {'
                 '        "paths": ['
                 '          "/AccountNumber"'
                 '        ],'
                 '        "kind": "Hash"'
                 '      },'
                 '      "defaultTtl": "100",'
                 '      "uniqueKeyPolicy": {'
                 '        "uniqueKeys": ['
                 '          {'
                 '            "paths": ['
                 '              "/testPath"'
                 '            ]'
                 '          }'
                 '        ]'
                 '      },'
                 '      "conflictResolutionPolicy": {'
                 '        "mode": "LastWriterWins",'
                 '        "conflictResolutionPath": "/path"'
                 '      }'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBSqlContainerDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlContainerThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBSqlContainerThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBMongoDBDatabaseList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBDatabaseGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBDatabaseCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "updatedDatabaseName"'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBMongoDBDatabaseDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBDatabaseThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBDatabaseThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBMongoDBCollectionList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBCollectionGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBCollectionCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "testcoll",'
                 '      "indexes": ['
                 '        {'
                 '          "key": {'
                 '            "keys": ['
                 '              "testKey"'
                 '            ]'
                 '          },'
                 '          "options": {'
                 '            "expire_after_seconds": "100",'
                 '            "unique": True'
                 '          }'
                 '        }'
                 '      ],'
                 '      "shardKey": {'
                 '        "testKey": "Hash"'
                 '      }'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBMongoDBCollectionDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBCollectionThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBMongoDBCollectionThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBTableList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBTableGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBTableReplace
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "tableName"'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBTableDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBTableThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBTableThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBCassandraKeyspaceList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraKeyspaceGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraKeyspaceCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "keyspaceName"'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBCassandraKeyspaceDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraKeyspaceThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraKeyspaceThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBCassandraTableList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraTableGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraTableCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "tableName",'
                 '      "defaultTtl": "100",'
                 '      "schema": {'
                 '        "columns": ['
                 '          {'
                 '            "name": "columnA",'
                 '            "type": "Ascii"'
                 '          }'
                 '        ],'
                 '        "partitionKeys": ['
                 '          {'
                 '            "name": "columnA"'
                 '          }'
                 '        ],'
                 '        "clusterKeys": ['
                 '          {'
                 '            "name": "columnA",'
                 '            "order_by": "Asc"'
                 '          }'
                 '        ]'
                 '      }'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBCassandraTableDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraTableThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCassandraTableThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBGremlinDatabaseList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinDatabaseGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinDatabaseCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "databaseName"'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBGremlinDatabaseDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinDatabaseThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinDatabaseThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBGremlinGraphList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinGraphGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinGraphCreateUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "id": "graphName",'
                 '      "indexingPolicy": {'
                 '        "indexingMode": "Consistent",'
                 '        "automatic": True,'
                 '        "includedPaths": ['
                 '          {'
                 '            "path": "/*",'
                 '            "indexes": ['
                 '              {'
                 '                "kind": "Range",'
                 '                "data_type": "String",'
                 '                "precision": "-1"'
                 '              },'
                 '              {'
                 '                "kind": "Range",'
                 '                "data_type": "Number",'
                 '                "precision": "-1"'
                 '              }'
                 '            ]'
                 '          }'
                 '        ],'
                 '        "excludedPaths": []'
                 '      },'
                 '      "partitionKey": {'
                 '        "paths": ['
                 '          "/AccountNumber"'
                 '        ],'
                 '        "kind": "Hash"'
                 '      },'
                 '      "defaultTtl": "100",'
                 '      "uniqueKeyPolicy": {'
                 '        "uniqueKeys": ['
                 '          {'
                 '            "paths": ['
                 '              "/testPath"'
                 '            ]'
                 '          }'
                 '        ]'
                 '      },'
                 '      "conflictResolutionPolicy": {'
                 '        "mode": "LastWriterWins",'
                 '        "conflictResolutionPath": "/path"'
                 '      }'
                 '    },'
                 '    "options": {}'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBGremlinGraphDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinGraphThroughputGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBGremlinGraphThroughputUpdate
        body = (
                 '{'
                 '  "properties": {'
                 '    "resource": {'
                 '      "throughput": "400"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CosmosDBOperationsList
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.DocumentDB/operations?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseGetUsages
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseGetMetricDefinitions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/metricDefinitions?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCollectionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCollectionGetUsages
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCollectionGetMetricDefinitions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/metricDefinitions?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBRegionCollectionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBCollectionGetUsages
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # CosmosDBDatabaseAccountRegionGetMetrics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])