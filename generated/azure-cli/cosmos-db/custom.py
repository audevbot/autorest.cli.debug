# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_cosmosdbdatabaseaccount
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
                     failover_policies=None):
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
    return client.database_accounts.create_or_update(resource_group_name=resource_group, account_name=name)

# module equivalent: azure_rm_cosmosdbdatabaseaccount
def update_cosmos-db(cmd, client,
                     resource_group,
                     name):
    body={}
    return client.database_accounts.create_or_update(resource_group_name=resource_group, account_name=name)

# module equivalent: azure_rm_cosmosdbdatabaseaccount
def delete_cosmos-db(cmd, client,
                     resource_group,
                     name):
    return client.database_accounts.delete(resource_group_name=resource_group, account_name=name)

# module equivalent: azure_rm_cosmosdbdatabaseaccount
def list_cosmos-db(cmd, client,
                   resource_group,
                   name):
    if resource_group is not None and name is not None:
        return client.database_accounts.list_mongo_dbdatabases(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_mongo_dbcollections(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_gremlin_databases(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_usages(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_cassandra_tables(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_sql_containers(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_gremlin_graphs(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_cassandra_keyspaces(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_metrics(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_sql_databases(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_tables(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None and name is not None:
        return client.database_accounts.list_metric_definitions(resource_group_name=resource_group, account_name=name)
    elif resource_group is not None:
        return client.database_accounts.list_by_resource_group(resource_group_name=resource_group)
    else:
        return client.database_accounts.list()

# module equivalent: azure_rm_cosmosdbdatabaseaccount
def show_cosmos-db(cmd, client,
                   resource_group,
                   name):
    return client.database_accounts.get(resource_group_name=resource_group, account_name=name)