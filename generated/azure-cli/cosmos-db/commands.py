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


    with self.command_group('databaseaccounts', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('create', 'create_databaseaccounts')
        g.custom_command('delete', 'delete_databaseaccounts')
        g.custom_command('list', 'list_databaseaccounts')
        g.custom_command('show', 'show_databaseaccounts')
    with self.command_group('databaseaccounts tables databases keyspaces containers collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_tables_databases_keyspaces_containers_collections')
        g.custom_command('show', 'show_databaseaccounts_tables_databases_keyspaces_containers_collections')
    with self.command_group('', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_')
    with self.command_group('databaseaccounts databases', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_databases')
    with self.command_group('databaseaccounts databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_databases_collections')
    with self.command_group('databaseaccounts region databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_region_databases_collections')
    with self.command_group('databaseaccounts region', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_region')
    with self.command_group('databaseaccounts sourceregion targetregion', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_sourceregion_targetregion')
    with self.command_group('databaseaccounts targetregion', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_targetregion')
    with self.command_group('databaseaccounts', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts')
    with self.command_group('databaseaccounts region databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_region_databases_collections')
    with self.command_group('databaseaccounts databases collections', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_databases_collections')
    with self.command_group('databaseaccounts databases collections partitionkeyrangeid', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_databases_collections_partitionkeyrangeid')
    with self.command_group('databaseaccounts region databases collections partitionkeyrangeid', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('list', 'list_databaseaccounts_region_databases_collections_partitionkeyrangeid')