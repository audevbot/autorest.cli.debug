# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import json

# module equivalent: azure_rm_azurefirewall
def create_network(cmd, client,
                   resource_group,
                   name,
                   id=None,
                   location=None,
                   tags=None,
                   application_rule_collections=None,
                   nat_rule_collections=None,
                   network_rule_collections=None,
                   ip_configurations=None):
    body={}
    body['id'] = id # str
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"440","$type":"DictionaryType","valueType":{"$id":"441","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"442","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"443","fixed":false},"deprecated":false}]
    body['application_rule_collections'] = json.parse(application_rule_collections) if isinstance(application_rule_collections, str) else application_rule_collections
    body['nat_rule_collections'] = json.parse(nat_rule_collections) if isinstance(nat_rule_collections, str) else nat_rule_collections
    body['network_rule_collections'] = json.parse(network_rule_collections) if isinstance(network_rule_collections, str) else network_rule_collections
    body['ip_configurations'] = json.parse(ip_configurations) if isinstance(ip_configurations, str) else ip_configurations
    return client.azure_firewalls.create_or_update(resource_group_name=resource_group, azure_firewall_name=name, parameters=body)

# module equivalent: azure_rm_azurefirewall
def update_network(cmd, client,
                   resource_group,
                   name,
                   id=None,
                   location=None,
                   tags=None,
                   application_rule_collections=None,
                   nat_rule_collections=None,
                   network_rule_collections=None,
                   ip_configurations=None):
    body={}
    body['id'] = id # str
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"440","$type":"DictionaryType","valueType":{"$id":"441","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"442","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"443","fixed":false},"deprecated":false}]
    body['application_rule_collections'] = json.parse(application_rule_collections) if isinstance(application_rule_collections, str) else application_rule_collections
    body['nat_rule_collections'] = json.parse(nat_rule_collections) if isinstance(nat_rule_collections, str) else nat_rule_collections
    body['network_rule_collections'] = json.parse(network_rule_collections) if isinstance(network_rule_collections, str) else network_rule_collections
    body['ip_configurations'] = json.parse(ip_configurations) if isinstance(ip_configurations, str) else ip_configurations
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