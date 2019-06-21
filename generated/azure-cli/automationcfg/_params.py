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


    with self.argument_context('automationcfg softwareupdateconfiguration create') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The name of the software update configuration to be created.')
        c.argument('client_request_id', id_part=None, help='Identifies this specific client request.')
        c.argument('properties', id_part=None, help='Software update configuration properties.')
        c.argument('update_configuration', id_part=None, help='update specific properties for the Software update configuration')
        c.argument('schedule_info', id_part=None, help='Schedule information for the Software update configuration')
        c.argument('error', id_part=None, help='Details of provisioning error')
        c.argument('tasks', id_part=None, help='Tasks information for the Software update configuration.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state for the software update configuration, which only appears in the response.')
        c.argument('creation_time', id_part=None, help='Creation time of the resource, which only appears in the response.')
        c.argument('created_by', id_part=None, help='CreatedBy property, which only appears in the response.')
        c.argument('last_modified_time', id_part=None, help='Last time resource was modified, which only appears in the response.')
        c.argument('last_modified_by', id_part=None, help='LastModifiedBy property, which only appears in the response.')
        c.argument('id', id_part=None, help='Resource Id.')
        c.argument('type', id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('automationcfg softwareupdateconfiguration delete') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The name of the software update configuration to be created.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationcfg softwareupdateconfiguration list') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The name of the software update configuration to be created.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('automationcfg softwareupdateconfiguration list') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The name of the software update configuration to be created.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])