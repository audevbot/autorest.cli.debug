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

    with self.argument_context('automationcfg softwareupdateconfiguration') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('automationcfg softwareupdateconfiguration_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('automationcfg softwareupdateconfiguration create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('client_request_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('update_configuration', name_arg_type, id_part=None)
        c.argument('schedule_info', name_arg_type, id_part=None)
        c.argument('error', name_arg_type, id_part=None)
        c.argument('tasks', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('creation_time', name_arg_type, id_part=None)
        c.argument('created_by', name_arg_type, id_part=None)
        c.argument('last_modified_time', name_arg_type, id_part=None)
        c.argument('last_modified_by', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('automationcfg softwareupdateconfiguration delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationcfg softwareupdateconfiguration list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('automationcfg softwareupdateconfiguration') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('automationcfg softwareupdateconfiguration_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('automationcfg softwareupdateconfiguration list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])