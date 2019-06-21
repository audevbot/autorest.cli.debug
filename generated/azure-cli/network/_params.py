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
        c.argument('resource_group', id_part=None, help='The name of the resource group.')
        c.argument('name', id_part=None, help='The name of the Azure Firewall.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('location', id_part=None, help='Resource location.')
        c.argument('tags', id_part=None, help='Resource tags.')
        c.argument('properties', id_part=None, help='undefined')
        c.argument('application_rule_collections', id_part=None, help='Collection of application rule collections used by Azure Firewall.')
        c.argument('nat_rule_collections', id_part=None, help='Collection of NAT rule collections used by Azure Firewall.')
        c.argument('network_rule_collections', id_part=None, help='Collection of network rule collections used by Azure Firewall.')
        c.argument('ip_configurations', id_part=None, help='IP configuration of the Azure Firewall resource.')
        c.argument('provisioning_state', id_part=None, help='The provisioning state of the resource.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('etag', id_part=None, help='Gets a unique read-only string that changes whenever the resource is updated.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('network delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group.')
        c.argument('name', id_part=None, help='The name of the Azure Firewall.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('network list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group.')
        c.argument('name', id_part=None, help='The name of the Azure Firewall.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('network show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group.')
        c.argument('name', id_part=None, help='The name of the Azure Firewall.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('network show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group.')
        c.argument('name', id_part=None, help='The name of the Azure Firewall.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('network list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group.')
        c.argument('name', id_part=None, help='The name of the Azure Firewall.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])