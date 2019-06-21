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

    with self.argument_context('frontdoor') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor_name', frontdoor_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor_name', frontdoor_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor routingrule_name', frontdoor routingrule_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor routingrule_name', frontdoor routingrule_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor healthprobesetting_name', frontdoor healthprobesetting_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor healthprobesetting_name', frontdoor healthprobesetting_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor loadbalancingsetting_name', frontdoor loadbalancingsetting_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor loadbalancingsetting_name', frontdoor loadbalancingsetting_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor backendpool_name', frontdoor backendpool_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor backendpool_name', frontdoor backendpool_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor frontendendpoint_name', frontdoor frontendendpoint_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor frontendendpoint_name', frontdoor frontendendpoint_name_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('frontdoor_name', frontdoor_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])