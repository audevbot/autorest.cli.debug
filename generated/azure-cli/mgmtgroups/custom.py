# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_mgmtgroups(cmd, client,
                      group_id,
                      properties=None,
                      display_name=None,
                      details=None,
                      tenant_id=None,
                      roles=None,
                      children=None,
                      id=None,
                      type=None):
    body={}
    body['properties'] = properties
    body['display_name'] = display_name
    body['details'] = details
    body['tenant_id'] = tenant_id
    body['roles'] = roles
    body['children'] = children
    return client.management_groups.create_or_update(group_id=group_id, createManagementGroupRequest=createManagementGroupRequest)


def update_mgmtgroups(cmd, client,
                      group_id,
                      properties=None,
                      display_name=None,
                      details=None,
                      tenant_id=None,
                      roles=None,
                      children=None,
                      id=None,
                      type=None):
    body={}
    body['properties'] = properties
    body['display_name'] = display_name
    body['details'] = details
    body['tenant_id'] = tenant_id
    body['roles'] = roles
    body['children'] = children
    return client.management_groups.create_or_update(group_id=group_id, createManagementGroupRequest=createManagementGroupRequest)


def delete_mgmtgroups(cmd, client,
                      group_id):
    body={}
    return client.management_groups.delete(group_id=group_id)


def list_mgmtgroups(cmd, client,
                    group_id):
    body={}
    return client.management_groups.list(group_id=group_id)


def show_mgmtgroups(cmd, client,
                    group_id):
    body={}
    return client.management_groups.get(group_id=group_id)


def show_mgmtgroups(cmd, client,
                    group_id):
    body={}
    return client.management_groups.get(group_id=group_id)


def list_mgmtgroups(cmd, client,
                    group_id):
    body={}
    return client.management_groups.list(group_id=group_id)


def create_mgmtgroups(cmd, client,
                      group_id):
    body={}
    return client.management_group_subscriptions.create(group_id=group_id)


def delete_mgmtgroups(cmd, client,
                      group_id):
    body={}
    return client.management_group_subscriptions.delete(group_id=group_id)


def list_(cmd, client):
    body={}
    return client.operations.list()