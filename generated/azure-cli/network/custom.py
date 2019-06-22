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
    return client.azure_firewalls.create(resource_group, name, body)


def delete_network(cmd, client,
                   resource_group,
                   name):
    return client.azure_firewalls.delete(resource_group, name)


def list_network(cmd, client,
                 resource_group,
                 name):
    return client.azure_firewalls.list(resource_group, name)


def show_network(cmd, client,
                 resource_group,
                 name):
    return client.azure_firewalls.show(resource_group, name)


def show_network(cmd, client,
                 resource_group,
                 name):
    return client.azure_firewalls.show(resource_group, name)


def list_network(cmd, client,
                 resource_group,
                 name):
    return client.azure_firewalls.list(resource_group, name)