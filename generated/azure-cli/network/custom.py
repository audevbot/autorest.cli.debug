# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_azurefirewall
def create_network(cmd, client,
                   resource_group,
                   name,
                   parameters=None,
                   id=None,
                   location=None,
                   tags=None,
                   application_rule_collections=None,
                   nat_rule_collections=None,
                   network_rule_collections=None,
                   ip_configurations=None):
    body={}
    body['id'] = id
    body['location'] = location
    body['tags'] = tags
    body['application_rule_collections'] = application_rule_collections
    body['nat_rule_collections'] = nat_rule_collections
    body['network_rule_collections'] = network_rule_collections
    body['ip_configurations'] = ip_configurations
    return client.azure_firewalls.create_or_update(resource_group_name=resource_group, azure_firewall_name=name, parameters=body)

# module equivalent: azure_rm_azurefirewall
def update_network(cmd, client,
                   resource_group,
                   name,
                   parameters=None):
    body={}
    return client.azure_firewalls.create_or_update(resource_group_name=resource_group, azure_firewall_name=name, parameters=body)

# module equivalent: azure_rm_azurefirewall
def delete_network(cmd, client,
                   resource_group,
                   name):
    return client.azure_firewalls.delete(resource_group_name=resource_group, azure_firewall_name=name)

# module equivalent: azure_rm_azurefirewall
def list_network(cmd, client,
                 resource_group):
    if resource_group is not None:
        return client.azure_firewalls.list(resource_group_name=resource_group)
    else:
        return client.azure_firewalls.list_all()

# module equivalent: azure_rm_azurefirewall
def show_network(cmd, client,
                 resource_group,
                 name):
    return client.azure_firewalls.get(resource_group_name=resource_group, azure_firewall_name=name)