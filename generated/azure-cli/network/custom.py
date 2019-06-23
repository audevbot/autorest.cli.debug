# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_network(cmd, client,
                   resource_group,
                   name,
                   id=None,
                   location=None,
                   tags=None,
                   properties=None,
                   application_rule_collections=None,
                   nat_rule_collections=None,
                   network_rule_collections=None,
                   ip_configurations=None,
                   provisioning_state=None,
                   type=None,
                   etag=None):
    body={}
    body['id'] = id
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['application_rule_collections'] = application_rule_collections
    body['nat_rule_collections'] = nat_rule_collections
    body['network_rule_collections'] = network_rule_collections
    body['ip_configurations'] = ip_configurations
    body['provisioning_state'] = provisioning_state
    return client.azure_firewalls.create_or_update(resource_group_name=resource_group, azure_firewall_name=name, parameters=body)


def delete_network(cmd, client,
                   resource_group,
                   name):
    body={}
    return client.azure_firewalls.delete(resource_group_name=resource_group, azure_firewall_name=name)


def list_network(cmd, client,
                 resource_group,
                 name):
    body={}
    return client.azure_firewalls.list_all(resource_group_name=resource_group, azure_firewall_name=name)


def show_network(cmd, client,
                 resource_group,
                 name):
    body={}
    return client.azure_firewalls.get(resource_group_name=resource_group, azure_firewall_name=name)


def show_network(cmd, client,
                 resource_group,
                 name):
    body={}
    return client.azure_firewalls.get(resource_group_name=resource_group, azure_firewall_name=name)


def list_network(cmd, client,
                 resource_group,
                 name):
    body={}
    return client.azure_firewalls.list(resource_group_name=resource_group, azure_firewall_name=name)