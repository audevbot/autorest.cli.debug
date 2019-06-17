# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors_name', frontdoors_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors_name', frontdoors_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors routingrules_name', frontdoors routingrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors routingrules_name', frontdoors routingrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors routingrules') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors healthprobesettings_name', frontdoors healthprobesettings_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors healthprobesettings_name', frontdoors healthprobesettings_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors healthprobesettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors loadbalancingsettings_name', frontdoors loadbalancingsettings_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors loadbalancingsettings_name', frontdoors loadbalancingsettings_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors loadbalancingsettings') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors backendpools_name', frontdoors backendpools_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors backendpools_name', frontdoors backendpools_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors backendpools') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors frontendendpoints_name', frontdoors frontendendpoints_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoors frontendendpoints_name', frontdoors frontendendpoints_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoors frontendendpoints') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])