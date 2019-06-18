# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.cosmos-db._client_factory import cf_cosmos-db
def load_command_table(self, _):

    cosmos-db_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.cosmos-db.operations#ApiManagementOperations.{}',
        client_factory=cf_cosmos-db)


    with self.command_group('cosmos-db', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('create', 'create_cosmos-db')
        g.custom_command('delete', 'delete_cosmos-db')
        g.custom_command('list', 'list_cosmos-db')
        g.custom_command('show', 'show_cosmos-db')
    with self.command_group('cosmos-db tables databases keyspaces containers collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_tables_databases_keyspaces_containers_collections')
        g.custom_command('show', 'show_cosmos-db_tables_databases_keyspaces_containers_collections')
    with self.command_group('', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_')
    with self.command_group('cosmos-db databases', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_databases')
    with self.command_group('cosmos-db databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_databases_collections')
    with self.command_group('cosmos-db region databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_region_databases_collections')
    with self.command_group('cosmos-db region', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_region')
    with self.command_group('cosmos-db sourceregion targetregion', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_sourceregion_targetregion')
    with self.command_group('cosmos-db targetregion', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_targetregion')
    with self.command_group('cosmos-db', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db')
    with self.command_group('cosmos-db region databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_region_databases_collections')
    with self.command_group('cosmos-db databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_databases_collections')
    with self.command_group('cosmos-db databases collections partitionkeyrangeid', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_databases_collections_partitionkeyrangeid')
    with self.command_group('cosmos-db region databases collections partitionkeyrangeid', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_cosmos-db_region_databases_collections_partitionkeyrangeid')