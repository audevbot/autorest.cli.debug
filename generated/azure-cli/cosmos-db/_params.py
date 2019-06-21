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

    with self.argument_context('cosmos-db create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('kind', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('consistency_policy', name_arg_type, id_part=None)
        c.argument('locations', name_arg_type, id_part=None)
        c.argument('database_account_offer_type', name_arg_type, id_part=None)
        c.argument('ip_range_filter', name_arg_type, id_part=None)
        c.argument('is_virtual_network_filter_enabled', name_arg_type, id_part=None)
        c.argument('enable_automatic_failover', name_arg_type, id_part=None)
        c.argument('capabilities', name_arg_type, id_part=None)
        c.argument('virtual_network_rules', name_arg_type, id_part=None)
        c.argument('enable_multiple_write_locations', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('document_endpoint', name_arg_type, id_part=None)
        c.argument('write_locations', name_arg_type, id_part=None)
        c.argument('read_locations', name_arg_type, id_part=None)
        c.argument('failover_policies', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db table database keyspace graph container collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db table database keyspace graph container collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db table database keyspace graph container collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('table_name', name_arg_type, id_part=None)
        c.argument('database_name', name_arg_type, id_part=None)
        c.argument('keyspace_name', name_arg_type, id_part=None)
        c.argument('graph_name', name_arg_type, id_part=None)
        c.argument('container_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db table database keyspace graph container collection show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('table_name', name_arg_type, id_part=None)
        c.argument('database_name', name_arg_type, id_part=None)
        c.argument('keyspace_name', name_arg_type, id_part=None)
        c.argument('graph_name', name_arg_type, id_part=None)
        c.argument('container_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('collection_rid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('region', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('collection_rid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('region', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db sourceregion targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db sourceregion targetregion_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db sourceregion targetregion list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('source_region', name_arg_type, id_part=None)
        c.argument('target_region', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db targetregion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db targetregion_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db targetregion list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('target_region', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('region', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('collection_rid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database collection') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database collection_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('collection_rid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db database collection partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db database collection partitionkeyrangeid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db database collection partitionkeyrangeid list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('collection_rid', name_arg_type, id_part=None)
        c.argument('partition_key_range_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('cosmos-db region database collection partitionkeyrangeid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cosmos-db region database collection partitionkeyrangeid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('cosmos-db region database collection partitionkeyrangeid list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('region', name_arg_type, id_part=None)
        c.argument('database_rid', name_arg_type, id_part=None)
        c.argument('collection_rid', name_arg_type, id_part=None)
        c.argument('partition_key_range_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])