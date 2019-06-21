# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.automationcfg._client_factory import cf_automationcfg
def load_command_table(self, _):

    automationcfg_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.automationcfg.operations#ApiManagementOperations.{}',
        client_factory=cf_automationcfg)


    with self.command_group('automationcfg softwareupdateconfiguration', automationcfg_sdk, client_factory=cf_automationcfg) as g:
        g.custom_command('create', 'create_automationcfg_softwareupdateconfiguration')
        g.custom_command('delete', 'delete_automationcfg_softwareupdateconfiguration')
        g.custom_command('list', 'list_automationcfg_softwareupdateconfiguration')
    with self.command_group('automationcfg softwareupdateconfiguration', automationcfg_sdk, client_factory=cf_automationcfg) as g:
        g.custom_command('list', 'list_automationcfg_softwareupdateconfiguration')