# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.create()


def update_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.update()


def delete_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.delete()


def list_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.list()


def show_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.show()


def show_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.show()


def list_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_groups.list()


def create_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_group_subscriptions.create()


def delete_mgmtgroups(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.management_group_subscriptions.delete()


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.operations.list()