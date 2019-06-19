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

    with self.argument_context('cosmos-db') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db_name', cosmos-db_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db tables databases keyspaces graphs containers collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db tables databases keyspaces graphs containers collections_name', cosmos-db tables databases keyspaces graphs containers collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db tables databases keyspaces graphs containers collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('cosmos-db tables databases keyspaces graphs containers collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db databases') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db databases_name', cosmos-db databases_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db databases') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db databases collections_name', cosmos-db databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db region databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region databases collections_name', cosmos-db region databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db region') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region_name', cosmos-db region_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db sourceregion targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db sourceregion targetregion_name', cosmos-db sourceregion targetregion_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db sourceregion targetregion') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db targetregion_name', cosmos-db targetregion_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db targetregion') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db_name', cosmos-db_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db region databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region databases collections_name', cosmos-db region databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db databases collections_name', cosmos-db databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db databases collections partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db databases collections partitionkeyrangeid_name', cosmos-db databases collections partitionkeyrangeid_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db databases collections partitionkeyrangeid') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('cosmos-db region databases collections partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region databases collections partitionkeyrangeid_name', cosmos-db region databases collections partitionkeyrangeid_name_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region databases collections partitionkeyrangeid') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])