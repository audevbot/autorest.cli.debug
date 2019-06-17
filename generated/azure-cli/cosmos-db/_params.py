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

    with self.argument_context('databaseaccounts') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts_name', databaseaccounts_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('databaseaccounts') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('databaseaccounts') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('databaseaccounts') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts tables databases keyspaces containers collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts tables databases keyspaces containers collections_name', databaseaccounts tables databases keyspaces containers collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts tables databases keyspaces containers collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)

    with self.argument_context('databaseaccounts tables databases keyspaces containers collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts databases') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts databases_name', databaseaccounts databases_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts databases') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts databases collections_name', databaseaccounts databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts region databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts region databases collections_name', databaseaccounts region databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts region databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts region') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts region_name', databaseaccounts region_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts region') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts sourceregion targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts sourceregion targetregion_name', databaseaccounts sourceregion targetregion_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts sourceregion targetregion') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts targetregion_name', databaseaccounts targetregion_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts targetregion') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts_name', databaseaccounts_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts region databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts region databases collections_name', databaseaccounts region databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts region databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts databases collections') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts databases collections_name', databaseaccounts databases collections_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts databases collections') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts databases collections partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts databases collections partitionkeyrangeid_name', databaseaccounts databases collections partitionkeyrangeid_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts databases collections partitionkeyrangeid') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('databaseaccounts region databases collections partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('databaseaccounts region databases collections partitionkeyrangeid_name', databaseaccounts region databases collections partitionkeyrangeid_name_type, options_list=['--name', '-n'])

    with self.argument_context('databaseaccounts region databases collections partitionkeyrangeid') as c:
        c.argument('cosmos-db_name', cosmos-db_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])