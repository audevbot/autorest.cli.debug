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
    return client.management_groups.create()


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
    return client.management_groups.update()


def delete_mgmtgroups(cmd, client,
                      group_id):
    return client.management_groups.delete()


def list_mgmtgroups(cmd, client,
                    group_id):
    return client.management_groups.list()


def show_mgmtgroups(cmd, client,
                    group_id):
    return client.management_groups.show()


def show_mgmtgroups(cmd, client,
                    group_id):
    return client.management_groups.show()


def list_mgmtgroups(cmd, client,
                    group_id):
    return client.management_groups.list()


def create_mgmtgroups(cmd, client,
                      group_id):
    return client.management_group_subscriptions.create()


def delete_mgmtgroups(cmd, client,
                      group_id):
    return client.management_group_subscriptions.delete()


def list_(cmd, client):
    return client.operations.list()