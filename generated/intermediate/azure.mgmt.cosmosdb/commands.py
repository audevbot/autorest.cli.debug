# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.cosmosdb._client_factory import cf_cosmosdb
def load_command_table(self, _):

    cosmosdb_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.cosmosdb.operations#ApiManagementOperations.{}',
        client_factory=cf_cosmosdb)


    with self.command_group('databaseaccounts', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('create', 'create_databaseaccounts')
        g.custom_command('delete', 'delete_databaseaccounts')
        g.custom_command('list', 'list_databaseaccounts')
        g.custom_command('show', 'show_databaseaccounts')
    with self.command_group('databaseaccounts tables databases keyspaces containers collections', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_tables_databases_keyspaces_containers_collections')
        g.custom_command('show', 'show_databaseaccounts_tables_databases_keyspaces_containers_collections')
    with self.command_group('', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_')
    with self.command_group('databaseaccounts databases', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_databases')
    with self.command_group('databaseaccounts databases collections', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_databases_collections')
    with self.command_group('databaseaccounts region databases collections', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_region_databases_collections')
    with self.command_group('databaseaccounts region', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_region')
    with self.command_group('databaseaccounts sourceregion targetregion', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_sourceregion_targetregion')
    with self.command_group('databaseaccounts targetregion', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_targetregion')
    with self.command_group('databaseaccounts', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts')
    with self.command_group('databaseaccounts region databases collections', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_region_databases_collections')
    with self.command_group('databaseaccounts databases collections', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_databases_collections')
    with self.command_group('databaseaccounts databases collections partitionkeyrangeid', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_databases_collections_partitionkeyrangeid')
    with self.command_group('databaseaccounts region databases collections partitionkeyrangeid', cosmosdb_sdk, client_factory=cf_cosmosdb) as g:
        g.custom_command('list', 'list_databaseaccounts_region_databases_collections_partitionkeyrangeid')