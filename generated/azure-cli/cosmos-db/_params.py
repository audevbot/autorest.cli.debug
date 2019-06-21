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

    with self.argument_context('cosmos-db') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db table database keyspace graph container collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db table database keyspace graph container collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db table database keyspace graph container collection') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db table database keyspace graph container collection') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database collection') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region database collection') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db sourceregion targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db sourceregion targetregion_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db sourceregion targetregion') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db targetregion_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db targetregion') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region database collection') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database collection') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database collection partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database collection partitionkeyrangeid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database collection partitionkeyrangeid') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region database collection partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region database collection partitionkeyrangeid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region database collection partitionkeyrangeid') as c:
        c.argument('cosmos-db_name', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])