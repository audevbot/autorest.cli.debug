# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_cosmos-db(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_accounts.create()


def delete_cosmos-db(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_accounts.delete()


def list_cosmos-db(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_accounts.list()


def show_cosmos-db(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_accounts.show()


def list_cosmos-db tables databases keyspaces graphs containers collections(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_accounts.list()


def show_cosmos-db tables databases keyspaces graphs containers collections(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_accounts.show()


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.operations.list()


def list_cosmos-db databases(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database.list()


def list_cosmos-db databases collections(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.collection.list()


def list_cosmos-db region databases collections(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.collection_region.list()


def list_cosmos-db region(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.database_account_region.list()


def list_cosmos-db sourceregion targetregion(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.percentile_source_target.list()


def list_cosmos-db targetregion(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.percentile_target.list()


def list_cosmos-db(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.percentile.list()


def list_cosmos-db region databases collections(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.collection_partition_region.list()


def list_cosmos-db databases collections(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.collection_partition.list()


def list_cosmos-db databases collections partitionkeyrangeid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.partition_key_range_id.list()


def list_cosmos-db region databases collections partitionkeyrangeid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.partition_key_range_id_region.list()