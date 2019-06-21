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


    with self.argument_context('cosmos-db create') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('location', name_arg_type, id_part=None, help='The location of the resource group to which the resource belongs.')
        c.argument('tags', name_arg_type, id_part=None, help='undefined')
        c.argument('kind', name_arg_type, id_part=None, help='Indicates the type of database account. This can only be set at database account creation.')
        c.argument('properties', name_arg_type, id_part=None, help='undefined')
        c.argument('consistency_policy', name_arg_type, id_part=None, help='The consistency policy for the Cosmos DB account.')
        c.argument('locations', name_arg_type, id_part=None, help='An array that contains the georeplication locations enabled for the Cosmos DB account.')
        c.argument('database_account_offer_type', name_arg_type, id_part=None, help='The offer type for the database')
        c.argument('ip_range_filter', name_arg_type, id_part=None, help='Cosmos DB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.')
        c.argument('is_virtual_network_filter_enabled', name_arg_type, id_part=None, help='Flag to indicate whether to enable/disable Virtual Network ACL rules.')
        c.argument('enable_automatic_failover', name_arg_type, id_part=None, help='Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.')
        c.argument('capabilities', name_arg_type, id_part=None, help='List of Cosmos DB capabilities for the account')
        c.argument('virtual_network_rules', name_arg_type, id_part=None, help='List of Virtual Network ACL rules configured for the Cosmos DB account.')
        c.argument('enable_multiple_write_locations', name_arg_type, id_part=None, help='Enables the account to write in multiple locations')
        c.argument('provisioning_state', name_arg_type, id_part=None, help='undefined')
        c.argument('document_endpoint', name_arg_type, id_part=None, help='The connection endpoint for the Cosmos DB database account.')
        c.argument('write_locations', name_arg_type, id_part=None, help='An array that contains the write location for the Cosmos DB account.')
        c.argument('read_locations', name_arg_type, id_part=None, help='An array that contains of the read locations enabled for the Cosmos DB account.')
        c.argument('failover_policies', name_arg_type, id_part=None, help='An array that contains the regions ordered by their failover priorities.')
        c.argument('id', name_arg_type, id_part=None, help='The unique resource identifier of the database account.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the database account.')
        c.argument('type', name_arg_type, id_part=None, help='The type of Azure resource.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db table database keyspace graph container collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('account_name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('table_name', name_arg_type, id_part=None, help='Cosmos DB table name.')
        c.argument('database_name', name_arg_type, id_part=None, help='Cosmos DB database name.')
        c.argument('keyspace_name', name_arg_type, id_part=None, help='Cosmos DB keyspace name.')
        c.argument('graph_name', name_arg_type, id_part=None, help='Cosmos DB graph name.')
        c.argument('container_name', name_arg_type, id_part=None, help='Cosmos DB container name.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB collection name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db table database keyspace graph container collection show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('account_name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('table_name', name_arg_type, id_part=None, help='Cosmos DB table name.')
        c.argument('database_name', name_arg_type, id_part=None, help='Cosmos DB database name.')
        c.argument('keyspace_name', name_arg_type, id_part=None, help='Cosmos DB keyspace name.')
        c.argument('graph_name', name_arg_type, id_part=None, help='Cosmos DB graph name.')
        c.argument('container_name', name_arg_type, id_part=None, help='Cosmos DB container name.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB collection name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db database list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('collection_rid', name_arg_type, id_part=None, help='Cosmos DB collection rid.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db region database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('region', name_arg_type, id_part=None, help='Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('collection_rid', name_arg_type, id_part=None, help='Cosmos DB collection rid.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db region list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('region', name_arg_type, id_part=None, help='Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db sourceregion targetregion list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('source_region', name_arg_type, id_part=None, help='Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('target_region', name_arg_type, id_part=None, help='Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db targetregion list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('target_region', name_arg_type, id_part=None, help='Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db region database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('region', name_arg_type, id_part=None, help='Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('collection_rid', name_arg_type, id_part=None, help='Cosmos DB collection rid.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db database collection list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('collection_rid', name_arg_type, id_part=None, help='Cosmos DB collection rid.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db database collection partitionkeyrangeid list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('collection_rid', name_arg_type, id_part=None, help='Cosmos DB collection rid.')
        c.argument('partition_key_range_id', name_arg_type, id_part=None, help='Partition Key Range Id for which to get data.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('cosmos-db region database collection partitionkeyrangeid list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='Name of an Azure resource group.')
        c.argument('name', name_arg_type, id_part=None, help='Cosmos DB database account name.')
        c.argument('region', name_arg_type, id_part=None, help='Cosmos DB region, with spaces between words and each word capitalized.')
        c.argument('database_rid', name_arg_type, id_part=None, help='Cosmos DB database rid.')
        c.argument('collection_rid', name_arg_type, id_part=None, help='Cosmos DB collection rid.')
        c.argument('partition_key_range_id', name_arg_type, id_part=None, help='Partition Key Range Id for which to get data.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])