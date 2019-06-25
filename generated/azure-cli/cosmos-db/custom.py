# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_cosmosdbdatabaseaccount
def create_cosmos-db(cmd, client,
                     resource_group,
                     name):
    body={}
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