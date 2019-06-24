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


    with self.argument_context('mgmtgroups create') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('properties', id_part=None, help='undefined')
        c.argument('display_name', id_part=None, help='The friendly name of the management group. If no value is passed then this  field will be set to the groupId.')
        c.argument('details', id_part=None, help='undefined')
        c.argument('tenant_id', id_part=None, help='The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000')
        c.argument('roles', id_part=None, help='The role definitions associated with the management group.')
        c.argument('children', id_part=None, help='The list of children.')
        c.argument('id', id_part=None, help='The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000')
        c.argument('type', id_part=None, help='The type of the resource.  For example, /providers/Microsoft.Management/managementGroups')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('mgmtgroups update') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('properties', id_part=None, help='undefined')
        c.argument('display_name', id_part=None, help='The friendly name of the management group. If no value is passed then this  field will be set to the groupId.')
        c.argument('details', id_part=None, help='undefined')
        c.argument('tenant_id', id_part=None, help='The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000')
        c.argument('roles', id_part=None, help='The role definitions associated with the management group.')
        c.argument('children', id_part=None, help='The list of children.')
        c.argument('id', id_part=None, help='The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000')
        c.argument('type', id_part=None, help='The type of the resource.  For example, /providers/Microsoft.Management/managementGroups')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('mgmtgroups delete') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('mgmtgroups list') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('mgmtgroups show') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('mgmtgroups subscription create') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('mgmtgroups subscription delete') as c:
        c.argument('group_id', id_part=None, help='Management Group ID.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])