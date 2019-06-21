# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('network create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group.)
        c.argument('name', name_arg_type, id_part=None,The name of the Azure Firewall.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('location', name_arg_type, id_part=None,Resource location.)
        c.argument('tags', name_arg_type, id_part=None,Resource tags.)
        c.argument('properties', name_arg_type, id_part=None,undefined)
        c.argument('application_rule_collections', name_arg_type, id_part=None,Collection of application rule collections used by Azure Firewall.)
        c.argument('nat_rule_collections', name_arg_type, id_part=None,Collection of NAT rule collections used by Azure Firewall.)
        c.argument('network_rule_collections', name_arg_type, id_part=None,Collection of network rule collections used by Azure Firewall.)
        c.argument('ip_configurations', name_arg_type, id_part=None,IP configuration of the Azure Firewall resource.)
        c.argument('provisioning_state', name_arg_type, id_part=None,The provisioning state of the resource.)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('etag', name_arg_type, id_part=None,Gets a unique read-only string that changes whenever the resource is updated.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('network delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group.)
        c.argument('name', name_arg_type, id_part=None,The name of the Azure Firewall.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('network list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group.)
        c.argument('name', name_arg_type, id_part=None,The name of the Azure Firewall.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('network show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group.)
        c.argument('name', name_arg_type, id_part=None,The name of the Azure Firewall.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('network show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group.)
        c.argument('name', name_arg_type, id_part=None,The name of the Azure Firewall.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('network list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group.)
        c.argument('name', name_arg_type, id_part=None,The name of the Azure Firewall.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])