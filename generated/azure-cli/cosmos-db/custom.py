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
    body={}
    body['location'] = location
    body['tags'] = tags
    body['kind'] = kind
    body['properties'] = properties
    body['consistency_policy'] = consistency_policy
    body['locations'] = locations
    body['database_account_offer_type'] = database_account_offer_type
    body['ip_range_filter'] = ip_range_filter
    body['is_virtual_network_filter_enabled'] = is_virtual_network_filter_enabled
    body['enable_automatic_failover'] = enable_automatic_failover
    body['capabilities'] = capabilities
    body['virtual_network_rules'] = virtual_network_rules
    body['enable_multiple_write_locations'] = enable_multiple_write_locations
    body['provisioning_state'] = provisioning_state
    body['document_endpoint'] = document_endpoint
    body['write_locations'] = write_locations
    body['read_locations'] = read_locations
    body['failover_policies'] = failover_policies
    return client.database_accounts.create_or_update(resource_group_name=resource_group, account_name=name, createUpdateParameters=createUpdateParameters)


def update_cosmos-db(cmd, client,
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
    body={}
    body['location'] = location
    body['tags'] = tags
    body['kind'] = kind
    body['properties'] = properties
    body['consistency_policy'] = consistency_policy
    body['locations'] = locations
    body['database_account_offer_type'] = database_account_offer_type
    body['ip_range_filter'] = ip_range_filter
    body['is_virtual_network_filter_enabled'] = is_virtual_network_filter_enabled
    body['enable_automatic_failover'] = enable_automatic_failover
    body['capabilities'] = capabilities
    body['virtual_network_rules'] = virtual_network_rules
    body['enable_multiple_write_locations'] = enable_multiple_write_locations
    body['provisioning_state'] = provisioning_state
    body['document_endpoint'] = document_endpoint
    body['write_locations'] = write_locations
    body['read_locations'] = read_locations
    body['failover_policies'] = failover_policies
    return client.database_accounts.create_or_update(resource_group_name=resource_group, account_name=name, createUpdateParameters=createUpdateParameters)


def delete_cosmos-db(cmd, client,
                     resource_group,
                     name):
    return client.database_accounts.delete(resource_group_name=resource_group, account_name=name)


def list_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.database_accounts.list(resource_group_name=resource_group, account_name=name)


def show_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.database_accounts.get(resource_group_name=resource_group, account_name=name)


def list_cosmos-db_table_database_keyspace_graph_container_collection(cmd, client,
                                                                      resource_group,
                                                                      account_name,
                                                                      table_name,
                                                                      database_name,
                                                                      keyspace_name,
                                                                      graph_name,
                                                                      container_name,
                                                                      name):
    return client.database_accounts.list_mongo_dbcollections(resource_group_name=resource_group, account_name=account_name)


def show_cosmos-db_table_database_keyspace_graph_container_collection(cmd, client,
                                                                      resource_group,
                                                                      account_name,
                                                                      table_name,
                                                                      database_name,
                                                                      keyspace_name,
                                                                      graph_name,
                                                                      container_name,
                                                                      name):
    return client.database_accounts.get(resource_group_name=resource_group, account_name=account_name)


def list_(cmd, client):
    return client.operations.list()


def list_cosmos-db_database(cmd, client,
                            resource_group,
                            name,
                            database_rid):
    return client.database.list_metric_definitions()


def list_cosmos-db_database_collection(cmd, client,
                                       resource_group,
                                       name,
                                       database_rid,
                                       collection_rid):
    return client.collection.list_metric_definitions()


def list_cosmos-db_region_database_collection(cmd, client,
                                              resource_group,
                                              name,
                                              region,
                                              database_rid,
                                              collection_rid):
    return client.collection_region.list_metrics()


def list_cosmos-db_region(cmd, client,
                          resource_group,
                          name,
                          region):
    return client.database_account_region.list_metrics()


def list_cosmos-db_sourceregion_targetregion(cmd, client,
                                             resource_group,
                                             name,
                                             source_region,
                                             target_region):
    return client.percentile_source_target.list_metrics()


def list_cosmos-db_targetregion(cmd, client,
                                resource_group,
                                name,
                                target_region):
    return client.percentile_target.list_metrics()


def list_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.percentile.list_metrics()


def list_cosmos-db_region_database_collection(cmd, client,
                                              resource_group,
                                              name,
                                              region,
                                              database_rid,
                                              collection_rid):
    return client.collection_partition_region.list_metrics()


def list_cosmos-db_database_collection(cmd, client,
                                       resource_group,
                                       name,
                                       database_rid,
                                       collection_rid):
    return client.collection_partition.list_usages()


def list_cosmos-db_database_collection_partitionkeyrangeid(cmd, client,
                                                           resource_group,
                                                           name,
                                                           database_rid,
                                                           collection_rid,
                                                           partition_key_range_id):
    return client.partition_key_range_id.list_metrics()


def list_cosmos-db_region_database_collection_partitionkeyrangeid(cmd, client,
                                                                  resource_group,
                                                                  name,
                                                                  region,
                                                                  database_rid,
                                                                  collection_rid,
                                                                  partition_key_range_id):
    return client.partition_key_range_id_region.list_metrics()