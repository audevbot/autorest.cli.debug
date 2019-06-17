# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.mgmtgroups._client_factory import cf_mgmtgroups
def load_command_table(self, _):

    mgmtgroups_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.mgmtgroups.operations#ApiManagementOperations.{}',
        client_factory=cf_mgmtgroups)


    with self.command_group('managementgroups', mgmtgroups_sdk, client_factory=cf_mgmtgroups) as g:
        g.custom_command('create', 'create_managementgroups')
        g.custom_command('update', 'update_managementgroups')
        g.custom_command('delete', 'delete_managementgroups')
        g.custom_command('list', 'list_managementgroups')
        g.custom_command('show', 'show_managementgroups')
    with self.command_group('managementgroups', mgmtgroups_sdk, client_factory=cf_mgmtgroups) as g:
        g.custom_command('show', 'show_managementgroups')
        g.custom_command('list', 'list_managementgroups')
    with self.command_group('managementgroups', mgmtgroups_sdk, client_factory=cf_mgmtgroups) as g:
        g.custom_command('create', 'create_managementgroups')
        g.custom_command('delete', 'delete_managementgroups')
    with self.command_group('', mgmtgroups_sdk, client_factory=cf_mgmtgroups) as g:
        g.custom_command('list', 'list_')