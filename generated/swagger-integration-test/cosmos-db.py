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

        # documentdb_databaseaccounts_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_put
        body = (
                 '{'
                 '  "location": "westus",'
                 '  "properties": {'
                 '    "databaseAccountOfferType": "Standard",'
                 '    "locations": ['
                 '      {'
                 '        "failoverPriority": "0",'
                 '        "locationName": "southcentralus",'
                 '        "isZoneRedundant": False'
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

        # documentdb_databaseaccounts_put_1
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
                 '        "ignoreMissingVNetServiceEndpoint": False'
                 '      }'
                 '    ],'
                 '    "locations": ['
                 '      {'
                 '        "failoverPriority": "0",'
                 '        "locationName": "southcentralus",'
                 '        "isZoneRedundant": False'
                 '      },'
                 '      {'
                 '        "failoverPriority": "1",'
                 '        "locationName": "eastus",'
                 '        "isZoneRedundant": False'
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

        # documentdb_databaseaccounts_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_failoverprioritychange_post
        body = (
                 '{'
                 '  "failoverPolicies": ['
                 '    {'
                 '      "locationName": "eastus",'
                 '      "failoverPriority": "0"'
                 '    },'
                 '    {'
                 '      "locationName": "westus",'
                 '      "failoverPriority": "1"'
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

        # documentdb_databaseaccounts_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.DocumentDB/databaseAccounts?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/listKeys?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # documentdb_databaseaccounts_listconnectionstrings_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/listConnectionStrings?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # documentdb_databaseaccounts_listconnectionstrings_post_1
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/listConnectionStrings?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # documentdb_databaseaccounts_offlineregion_post
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

        # documentdb_databaseaccounts_onlineregion_post
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

        # documentdb_databaseaccounts_readonlykeys_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/readonlykeys?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_readonlykeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/readonlykeys?api-version=2015-04-08 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # documentdb_databaseaccounts_regeneratekey_post
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

        # documentdb_databaseaccountnames_head
        self.cmd('rest '
                 '--method head '
                 '--uri /providers/Microsoft.DocumentDB/databaseAccountNames/{DATABASE_ACCOUNT_NAME_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_usages_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_metricdefinitions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/metricDefinitions?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_put
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

        # documentdb_databaseaccounts_apis_databases_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_settings_put
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

        # documentdb_databaseaccounts_apis_databases_containers_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_containers_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_containers_put
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
                 '                "dataType": "String",'
                 '                "precision": "-1"'
                 '              },'
                 '              {'
                 '                "kind": "Range",'
                 '                "dataType": "Number",'
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

        # documentdb_databaseaccounts_apis_databases_containers_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_containers_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/containers/{CONTAINER_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_containers_settings_put
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

        # documentdb_databaseaccounts_apis_databases_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_put_1
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

        # documentdb_databaseaccounts_apis_databases_delete_1
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_settings_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_settings_put_1
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

        # documentdb_databaseaccounts_apis_databases_collections_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_collections_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_collections_put
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
                 '            "expireAfterSeconds": "100",'
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

        # documentdb_databaseaccounts_apis_databases_collections_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_collections_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_collections_settings_put
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

        # documentdb_databaseaccounts_apis_tables_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_tables_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_tables_put
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

        # documentdb_databaseaccounts_apis_tables_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_tables_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/tables/{TABLE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_tables_settings_put
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

        # documentdb_databaseaccounts_apis_keyspaces_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_put
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

        # documentdb_databaseaccounts_apis_keyspaces_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_settings_put
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

        # documentdb_databaseaccounts_apis_keyspaces_tables_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_tables_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_tables_put
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
                 '            "orderBy": "Asc"'
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

        # documentdb_databaseaccounts_apis_keyspaces_tables_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_tables_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/keyspaces/{KEYSPACE_NAME}/tables/{TABLE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_keyspaces_tables_settings_put
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

        # documentdb_databaseaccounts_apis_databases_get_4
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_get_5
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_put_2
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

        # documentdb_databaseaccounts_apis_databases_delete_2
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_settings_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_settings_put_2
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

        # documentdb_databaseaccounts_apis_databases_graphs_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_graphs_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_graphs_put
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
                 '                "dataType": "String",'
                 '                "precision": "-1"'
                 '              },'
                 '              {'
                 '                "kind": "Range",'
                 '                "dataType": "Number",'
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

        # documentdb_databaseaccounts_apis_databases_graphs_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_graphs_settings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/apis/{API_NAME}/databases/{DATABASE_NAME}/graphs/{GRAPH_NAME}/settings/{SETTING_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_apis_databases_graphs_settings_put
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

        # documentdb_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.DocumentDB/operations?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_usages_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_metricdefinitions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/metricDefinitions?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_collections_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_collections_usages_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/usages?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_collections_metricdefinitions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/metricDefinitions?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_region_databases_collections_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_region_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_sourceregion_targetregion_percentile_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/sourceRegion/{SOURCE_REGION_NAME}/targetRegion/{TARGET_REGION_NAME}/percentile/{PERCENTILE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_targetregion_percentile_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/targetRegion/{TARGET_REGION_NAME}/percentile/{PERCENTILE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_percentile_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/percentile/{PERCENTILE_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_region_databases_collections_partitions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/partitions/{PARTITION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_collections_partitions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/partitions/{PARTITION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_collections_partitions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/partitions/{PARTITION_NAME}?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_databases_collections_partitionkeyrangeid_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/partitionKeyRangeId/{PARTITION_KEY_RANGE_ID_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])

        # documentdb_databaseaccounts_region_databases_collections_partitionkeyrangeid_metrics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.DocumentDB/databaseAccounts/{DATABASE_ACCOUNT_NAME}/region/{REGION_NAME}/databases/{DATABASE_NAME}/collections/{COLLECTION_NAME}/partitionKeyRangeId/{PARTITION_KEY_RANGE_ID_NAME}/metrics?api-version=2015-04-08 '
                 , checks=[
                          ])