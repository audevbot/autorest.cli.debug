# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.frontdoor._client_factory import cf_frontdoor
def load_command_table(self, _):

    frontdoor_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.frontdoor.operations#ApiManagementOperations.{}',
        client_factory=cf_frontdoor)


    with self.command_group('frontdoor', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor')
        g.custom_command('delete', 'delete_frontdoor')
        g.custom_command('list', 'list_frontdoor')
        g.custom_command('show', 'show_frontdoor')
    with self.command_group('frontdoor', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoor')
        g.custom_command('list', 'list_frontdoor')
    with self.command_group('frontdoor routingrules', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_routingrules')
        g.custom_command('delete', 'delete_frontdoor_routingrules')
        g.custom_command('list', 'list_frontdoor_routingrules')
        g.custom_command('show', 'show_frontdoor_routingrules')
    with self.command_group('frontdoor routingrules', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoor_routingrules')
        g.custom_command('list', 'list_frontdoor_routingrules')
    with self.command_group('frontdoor healthprobesettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_healthprobesettings')
        g.custom_command('delete', 'delete_frontdoor_healthprobesettings')
        g.custom_command('list', 'list_frontdoor_healthprobesettings')
        g.custom_command('show', 'show_frontdoor_healthprobesettings')
    with self.command_group('frontdoor healthprobesettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoor_healthprobesettings')
        g.custom_command('list', 'list_frontdoor_healthprobesettings')
    with self.command_group('frontdoor loadbalancingsettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_loadbalancingsettings')
        g.custom_command('delete', 'delete_frontdoor_loadbalancingsettings')
        g.custom_command('list', 'list_frontdoor_loadbalancingsettings')
        g.custom_command('show', 'show_frontdoor_loadbalancingsettings')
    with self.command_group('frontdoor loadbalancingsettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoor_loadbalancingsettings')
        g.custom_command('list', 'list_frontdoor_loadbalancingsettings')
    with self.command_group('frontdoor backendpools', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_backendpools')
        g.custom_command('delete', 'delete_frontdoor_backendpools')
        g.custom_command('list', 'list_frontdoor_backendpools')
        g.custom_command('show', 'show_frontdoor_backendpools')
    with self.command_group('frontdoor backendpools', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoor_backendpools')
        g.custom_command('list', 'list_frontdoor_backendpools')
    with self.command_group('frontdoor frontendendpoints', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontendendpoints')
        g.custom_command('delete', 'delete_frontdoor_frontendendpoints')
        g.custom_command('list', 'list_frontdoor_frontendendpoints')
        g.custom_command('show', 'show_frontdoor_frontendendpoints')
    with self.command_group('frontdoor frontendendpoints', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoor_frontendendpoints')
        g.custom_command('list', 'list_frontdoor_frontendendpoints')