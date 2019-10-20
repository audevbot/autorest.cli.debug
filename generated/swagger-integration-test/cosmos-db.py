# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.cosmosdb
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtCosmosDBTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtCosmosDBTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.cosmosdb.CosmosDB
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_cosmos-db(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get(resource_group.name, DATABASE_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "dept": "finance"
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.patch(resource_group.name, DATABASE_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "westus",
          "properties": {
            "database_account_offer_type": "Standard",
            "locations": [
              {
                "failover_priority": "0",
                "location_name": "southcentralus",
                "is_zone_redundant": False
              }
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_or_update(resource_group.name, DATABASE_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "westus",
          "kind": "GlobalDocumentDB",
          "properties": {
            "database_account_offer_type": "Standard",
            "ip_range_filter": "10.10.10.10",
            "is_virtual_network_filter_enabled": True,
            "virtual_network_rules": [
              {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
                "ignore_missing_vnet_service_endpoint": False
              }
            ],
            "locations": [
              {
                "failover_priority": "0",
                "location_name": "southcentralus",
                "is_zone_redundant": False
              },
              {
                "failover_priority": "1",
                "location_name": "eastus",
                "is_zone_redundant": False
              }
            ],
            "consistency_policy": {
              "default_consistency_level": "BoundedStaleness",
              "max_interval_in_seconds": "10",
              "max_staleness_prefix": "200"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_or_update(resource_group.name, DATABASE_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete(resource_group.name, DATABASE_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "failover_policies": [
            {
              "location_name": "eastus",
              "failover_priority": "0"
            },
            {
              "location_name": "westus",
              "failover_priority": "1"
            }
          ]
        }
        azure_operation_poller = self.mgmt_client.database_accounts.failover_priority_change(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_keys(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_connection_strings(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_connection_strings(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        [
          {
            "region": "North Europe"
          }
        ]
        azure_operation_poller = self.mgmt_client.database_accounts.offline_region(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        [
          {
            "region": "North Europe"
          }
        ]
        azure_operation_poller = self.mgmt_client.database_accounts.online_region(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_read_only_keys(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_read_only_keys(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "key_kind": "primary"
        }
        azure_operation_poller = self.mgmt_client.database_accounts.regenerate_key(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.check_name_exists(DATABASE_ACCOUNT_NAME_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_usages(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_metric_definitions(resource_group.name, DATABASE_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_sql_databases(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_sql_database(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "databaseName"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_sql_database(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_sql_database(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_sql_database_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_sql_database_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_sql_containers(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_sql_container(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "containerName",
              "indexing_policy": {
                "indexing_mode": "Consistent",
                "automatic": True,
                "included_paths": [
                  {
                    "path": "/*",
                    "indexes": [
                      {
                        "kind": "Range",
                        "data_type": "String",
                        "precision": "-1"
                      },
                      {
                        "kind": "Range",
                        "data_type": "Number",
                        "precision": "-1"
                      }
                    ]
                  }
                ],
                "excluded_paths": []
              },
              "partition_key": {
                "paths": [
                  "/AccountNumber"
                ],
                "kind": "Hash"
              },
              "default_ttl": "100",
              "unique_key_policy": {
                "unique_keys": [
                  {
                    "paths": [
                      "/testPath"
                    ]
                  }
                ]
              },
              "conflict_resolution_policy": {
                "mode": "LastWriterWins",
                "conflict_resolution_path": "/path"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_sql_container(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_sql_container(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_sql_container_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_sql_container_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_mongo_dbdatabases(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_mongo_dbdatabase(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "updatedDatabaseName"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_mongo_dbdatabase(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_mongo_dbdatabase(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_mongo_dbdatabase_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_mongo_dbdatabase_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_mongo_dbcollections(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_mongo_dbcollection(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "testcoll",
              "indexes": [
                {
                  "key": {
                    "keys": [
                      "testKey"
                    ]
                  },
                  "options": {
                    "expire_after_seconds": "100",
                    "unique": True
                  }
                }
              ],
              "shard_key": {
                "test_key": "Hash"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_mongo_dbcollection(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_mongo_dbcollection(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_mongo_dbcollection_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_mongo_dbcollection_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_tables(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_table(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "tableName"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_table(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_table(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_table_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_table_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_cassandra_keyspaces(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_cassandra_keyspace(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "keyspaceName"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_cassandra_keyspace(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_cassandra_keyspace(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_cassandra_keyspace_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_cassandra_keyspace_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_cassandra_tables(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_cassandra_table(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "tableName",
              "default_ttl": "100",
              "schema": {
                "columns": [
                  {
                    "name": "columnA",
                    "type": "Ascii"
                  }
                ],
                "partition_keys": [
                  {
                    "name": "columnA"
                  }
                ],
                "cluster_keys": [
                  {
                    "name": "columnA",
                    "order_by": "Asc"
                  }
                ]
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_cassandra_table(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_cassandra_table(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_cassandra_table_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_cassandra_table_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_gremlin_databases(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_gremlin_database(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "databaseName"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_gremlin_database(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_gremlin_database(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_gremlin_database_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_gremlin_database_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.list_gremlin_graphs(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_gremlin_graph(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "id": "graphName",
              "indexing_policy": {
                "indexing_mode": "Consistent",
                "automatic": True,
                "included_paths": [
                  {
                    "path": "/*",
                    "indexes": [
                      {
                        "kind": "Range",
                        "data_type": "String",
                        "precision": "-1"
                      },
                      {
                        "kind": "Range",
                        "data_type": "Number",
                        "precision": "-1"
                      }
                    ]
                  }
                ],
                "excluded_paths": []
              },
              "partition_key": {
                "paths": [
                  "/AccountNumber"
                ],
                "kind": "Hash"
              },
              "default_ttl": "100",
              "unique_key_policy": {
                "unique_keys": [
                  {
                    "paths": [
                      "/testPath"
                    ]
                  }
                ]
              },
              "conflict_resolution_policy": {
                "mode": "LastWriterWins",
                "conflict_resolution_path": "/path"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.create_update_gremlin_graph(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.delete_gremlin_graph(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_accounts.get_gremlin_graph_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.database_accounts.update_gremlin_graph_throughput(resource_group.name, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, SETTING_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.operations.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database.list_usages(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database.list_metric_definitions(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.collection.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.collection.list_usages(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.collection.list_metric_definitions(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.collection_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.collection.list_usages(resource_group.name, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.database_account_region.list_metrics(resource_group.name, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()