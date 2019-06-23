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


    with self.command_group('cosmos-db databaseaccount', cosmos-db_sdk, client_factory=cf_cosmos-db) as g:
        g.custom_command('create', 'create_cosmos-db_databaseaccount')
        g.custom_command('update', 'update_cosmos-db_databaseaccount')
        g.custom_command('delete', 'delete_cosmos-db_databaseaccount')
        g.custom_command('list', 'list_cosmos-db_databaseaccount')
        g.custom_command('show', 'show_cosmos-db_databaseaccount')