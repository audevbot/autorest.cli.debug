# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_cosmos-db(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None,
                     kind=None,
                     properties=None,
                     consistency_policy=None,
                     locations=None,
                     database_account_offer_type=None,
                     ip_range_filter=None,
                     is_virtual_network_filter_enabled=None,
                     enable_automatic_failover=None,
                     capabilities=None,
                     virtual_network_rules=None,
                     enable_multiple_write_locations=None,
                     provisioning_state=None,
                     document_endpoint=None,
                     write_locations=None,
                     read_locations=None,
                     failover_policies=None,
                     id=None,
                     type=None):
    return client.database_accounts.create()


def delete_cosmos-db(cmd, client,
                     resource_group,
                     name):
    return client.database_accounts.delete()


def list_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.database_accounts.list()


def show_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.database_accounts.show()


def list_cosmos-db_table_database_keyspace_graph_container_collection(cmd, client,
                                                                      resource_group,
                                                                      account_name,
                                                                      table_name,
                                                                      database_name,
                                                                      keyspace_name,
                                                                      graph_name,
                                                                      container_name,
                                                                      name):
    return client.database_accounts.list()


def show_cosmos-db_table_database_keyspace_graph_container_collection(cmd, client,
                                                                      resource_group,
                                                                      account_name,
                                                                      table_name,
                                                                      database_name,
                                                                      keyspace_name,
                                                                      graph_name,
                                                                      container_name,
                                                                      name):
    return client.database_accounts.show()


def list_(cmd, client):
    return client.operations.list()


def list_cosmos-db_database(cmd, client,
                            resource_group,
                            name,
                            database_rid):
    return client.database.list()


def list_cosmos-db_database_collection(cmd, client,
                                       resource_group,
                                       name,
                                       database_rid,
                                       collection_rid):
    return client.collection.list()


def list_cosmos-db_region_database_collection(cmd, client,
                                              resource_group,
                                              name,
                                              region,
                                              database_rid,
                                              collection_rid):
    return client.collection_region.list()


def list_cosmos-db_region(cmd, client,
                          resource_group,
                          name,
                          region):
    return client.database_account_region.list()


def list_cosmos-db_sourceregion_targetregion(cmd, client,
                                             resource_group,
                                             name,
                                             source_region,
                                             target_region):
    return client.percentile_source_target.list()


def list_cosmos-db_targetregion(cmd, client,
                                resource_group,
                                name,
                                target_region):
    return client.percentile_target.list()


def list_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.percentile.list()


def list_cosmos-db_region_database_collection(cmd, client,
                                              resource_group,
                                              name,
                                              region,
                                              database_rid,
                                              collection_rid):
    return client.collection_partition_region.list()


def list_cosmos-db_database_collection(cmd, client,
                                       resource_group,
                                       name,
                                       database_rid,
                                       collection_rid):
    return client.collection_partition.list()


def list_cosmos-db_database_collection_partitionkeyrangeid(cmd, client,
                                                           resource_group,
                                                           name,
                                                           database_rid,
                                                           collection_rid,
                                                           partition_key_range_id):
    return client.partition_key_range_id.list()


def list_cosmos-db_region_database_collection_partitionkeyrangeid(cmd, client,
                                                                  resource_group,
                                                                  name,
                                                                  region,
                                                                  database_rid,
                                                                  collection_rid,
                                                                  partition_key_range_id):
    return client.partition_key_range_id_region.list()