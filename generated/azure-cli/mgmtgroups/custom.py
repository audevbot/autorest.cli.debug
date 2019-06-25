# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_managementgroup
def create_mgmtgroups(cmd, client,
                      group_id):
    body={}
    return client.management_groups.create_or_update(group_id=group_id)

# module equivalent: azure_rm_managementgroup
def update_mgmtgroups(cmd, client,
                      group_id):
    body={}
    return client.management_groups.create_or_update(group_id=group_id)

# module equivalent: azure_rm_managementgroup
def delete_mgmtgroups(cmd, client,
                      group_id):
    return client.management_groups.delete(group_id=group_id)

# module equivalent: azure_rm_managementgroup
def list_mgmtgroups(cmd, client):
    return client.management_groups.list()

# module equivalent: azure_rm_managementgroup
def show_mgmtgroups(cmd, client,
                    group_id):
    return client.management_groups.get(group_id=group_id)

# module equivalent: azure_rm_managementgroupsubscription
def create_mgmtgroups_subscription(cmd, client,
                                   group_id):
    body={}
    return client.management_group_subscriptions.create(group_id=group_id)

# module equivalent: azure_rm_managementgroupsubscription
def delete_mgmtgroups_subscription(cmd, client,
                                   group_id):
    return client.management_group_subscriptions.delete(group_id=group_id)