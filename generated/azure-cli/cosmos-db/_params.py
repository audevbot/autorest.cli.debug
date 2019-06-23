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
        c.argument('resource_group', id_part=None, help='Name of an Azure resource group.')
        c.argument('name', id_part=None, help='Cosmos DB database account name.')
        c.argument('location', id_part=None, help='The location of the resource group to which the resource belongs.')
        c.argument('tags', id_part=None, help='undefined')
        c.argument('kind', id_part=None, help='Indicates the type of database account. This can only be set at database account creation.')
        c.argument('properties', id_part=None, help='undefined')
        c.argument('consistency_policy', id_part=None, help='The consistency policy for the Cosmos DB account.')
        c.argument('locations', id_part=None, help='An array that contains the georeplication locations enabled for the Cosmos DB account.')
        c.argument('database_account_offer_type', id_part=None, help='The offer type for the database')
        c.argument('ip_range_filter', id_part=None, help='Cosmos DB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.')
        c.argument('is_virtual_network_filter_enabled', id_part=None, help='Flag to indicate whether to enable/disable Virtual Network ACL rules.')
        c.argument('enable_automatic_failover', id_part=None, help='Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.')
        c.argument('capabilities', id_part=None, help='List of Cosmos DB capabilities for the account')
        c.argument('virtual_network_rules', id_part=None, help='List of Virtual Network ACL rules configured for the Cosmos DB account.')
        c.argument('enable_multiple_write_locations', id_part=None, help='Enables the account to write in multiple locations')
        c.argument('provisioning_state', id_part=None, help='undefined')
        c.argument('document_endpoint', id_part=None, help='The connection endpoint for the Cosmos DB database account.')
        c.argument('write_locations', id_part=None, help='An array that contains the write location for the Cosmos DB account.')
        c.argument('read_locations', id_part=None, help='An array that contains of the read locations enabled for the Cosmos DB account.')
        c.argument('failover_policies', id_part=None, help='An array that contains the regions ordered by their failover priorities.')
        c.argument('id', id_part=None, help='The unique resource identifier of the database account.')
        c.argument('type', id_part=None, help='The type of Azure resource.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db update') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure resource group.')
        c.argument('name', id_part=None, help='Cosmos DB database account name.')
        c.argument('location', id_part=None, help='The location of the resource group to which the resource belongs.')
        c.argument('tags', id_part=None, help='undefined')
        c.argument('kind', id_part=None, help='Indicates the type of database account. This can only be set at database account creation.')
        c.argument('properties', id_part=None, help='undefined')
        c.argument('consistency_policy', id_part=None, help='The consistency policy for the Cosmos DB account.')
        c.argument('locations', id_part=None, help='An array that contains the georeplication locations enabled for the Cosmos DB account.')
        c.argument('database_account_offer_type', id_part=None, help='The offer type for the database')
        c.argument('ip_range_filter', id_part=None, help='Cosmos DB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.')
        c.argument('is_virtual_network_filter_enabled', id_part=None, help='Flag to indicate whether to enable/disable Virtual Network ACL rules.')
        c.argument('enable_automatic_failover', id_part=None, help='Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.')
        c.argument('capabilities', id_part=None, help='List of Cosmos DB capabilities for the account')
        c.argument('virtual_network_rules', id_part=None, help='List of Virtual Network ACL rules configured for the Cosmos DB account.')
        c.argument('enable_multiple_write_locations', id_part=None, help='Enables the account to write in multiple locations')
        c.argument('provisioning_state', id_part=None, help='undefined')
        c.argument('document_endpoint', id_part=None, help='The connection endpoint for the Cosmos DB database account.')
        c.argument('write_locations', id_part=None, help='An array that contains the write location for the Cosmos DB account.')
        c.argument('read_locations', id_part=None, help='An array that contains of the read locations enabled for the Cosmos DB account.')
        c.argument('failover_policies', id_part=None, help='An array that contains the regions ordered by their failover priorities.')
        c.argument('id', id_part=None, help='The unique resource identifier of the database account.')
        c.argument('type', id_part=None, help='The type of Azure resource.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db delete') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure resource group.')
        c.argument('name', id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db list') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure resource group.')
        c.argument('name', id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('cosmos-db show') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure resource group.')
        c.argument('name', id_part=None, help='Cosmos DB database account name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])