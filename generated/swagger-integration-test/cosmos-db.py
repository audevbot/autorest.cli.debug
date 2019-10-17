# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

        BODY = {}
        output = mgmt_client.database_accounts.get(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, BODY)
        BODY = {
          "tags": {
            "dept": "finance"
          }
        }
        output = mgmt_client.database_accounts.patch(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, BODY)
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
        output = mgmt_client.database_accounts.create_or_update(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, BODY)
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
        output = mgmt_client.database_accounts.create_or_update(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, BODY)
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
        output = mgmt_client.database_accounts.failover_priority_change(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list(, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_keys(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_connection_strings(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_connection_strings(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        [
          {
            "region": "North Europe"
          }
        ]
        output = mgmt_client.database_accounts.offline_region(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        [
          {
            "region": "North Europe"
          }
        ]
        output = mgmt_client.database_accounts.online_region(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_read_only_keys(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_read_only_keys(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {
          "key_kind": "primary"
        }
        output = mgmt_client.database_accounts.regenerate_key(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.check_name_exists(DATABASE_ACCOUNT_NAME_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_usages(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_metric_definitions(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_sql_databases(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_sql_database(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "id": "databaseName"
            }
          }
        }
        output = mgmt_client.database_accounts.create_update_sql_database(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_sql_database(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_sql_database_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_sql_database_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_sql_containers(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_sql_container(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, BODY)
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
        output = mgmt_client.database_accounts.create_update_sql_container(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_sql_container(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_sql_container_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_sql_container_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, CONTAINER_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_mongo_dbdatabases(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_mongo_dbdatabase(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "id": "updatedDatabaseName"
            }
          }
        }
        output = mgmt_client.database_accounts.create_update_mongo_dbdatabase(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_mongo_dbdatabase(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_mongo_dbdatabase_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_mongo_dbdatabase_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_mongo_dbcollections(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_mongo_dbcollection(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, BODY)
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
        output = mgmt_client.database_accounts.create_update_mongo_dbcollection(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_mongo_dbcollection(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_mongo_dbcollection_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_mongo_dbcollection_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, COLLECTION_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_tables(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_table(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "id": "tableName"
            }
          }
        }
        output = mgmt_client.database_accounts.create_update_table(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_table(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_table_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_table_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, TABLE_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_cassandra_keyspaces(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_cassandra_keyspace(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "id": "keyspaceName"
            }
          }
        }
        output = mgmt_client.database_accounts.create_update_cassandra_keyspace(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_cassandra_keyspace(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_cassandra_keyspace_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_cassandra_keyspace_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_cassandra_tables(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_cassandra_table(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, BODY)
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
        output = mgmt_client.database_accounts.create_update_cassandra_table(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_cassandra_table(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_cassandra_table_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_cassandra_table_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, KEYSPACE_NAME, TABLE_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_gremlin_databases(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_gremlin_database(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "id": "databaseName"
            }
          }
        }
        output = mgmt_client.database_accounts.create_update_gremlin_database(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_gremlin_database(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_gremlin_database_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_gremlin_database_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.list_gremlin_graphs(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_gremlin_graph(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, BODY)
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
        output = mgmt_client.database_accounts.create_update_gremlin_graph(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.delete_gremlin_graph(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, BODY)
        BODY = {}
        output = mgmt_client.database_accounts.get_gremlin_graph_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, SETTING_NAME, BODY)
        BODY = {
          "properties": {
            "resource": {
              "throughput": "400"
            }
          }
        }
        output = mgmt_client.database_accounts.update_gremlin_graph_throughput(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, API_NAME, DATABASE_NAME, GRAPH_NAME, SETTING_NAME, BODY)
        BODY = {}
        output = mgmt_client.operations.list(, BODY)
        BODY = {}
        output = mgmt_client.database.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database.list_usages(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database.list_metric_definitions(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.collection.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.collection.list_usages(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.collection.list_metric_definitions(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.collection_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.collection.list_usages(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, DATABASE_NAME, COLLECTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.database_account_region.list_metrics(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, REGION_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()