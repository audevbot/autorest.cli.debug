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


    with self.command_group('frontdoors', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoors')
        g.custom_command('delete', 'delete_frontdoors')
        g.custom_command('list', 'list_frontdoors')
        g.custom_command('show', 'show_frontdoors')
    with self.command_group('frontdoors', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoors')
        g.custom_command('list', 'list_frontdoors')
    with self.command_group('frontdoors routingrules', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoors_routingrules')
        g.custom_command('delete', 'delete_frontdoors_routingrules')
        g.custom_command('list', 'list_frontdoors_routingrules')
        g.custom_command('show', 'show_frontdoors_routingrules')
    with self.command_group('frontdoors routingrules', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoors_routingrules')
        g.custom_command('list', 'list_frontdoors_routingrules')
    with self.command_group('frontdoors healthprobesettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoors_healthprobesettings')
        g.custom_command('delete', 'delete_frontdoors_healthprobesettings')
        g.custom_command('list', 'list_frontdoors_healthprobesettings')
        g.custom_command('show', 'show_frontdoors_healthprobesettings')
    with self.command_group('frontdoors healthprobesettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoors_healthprobesettings')
        g.custom_command('list', 'list_frontdoors_healthprobesettings')
    with self.command_group('frontdoors loadbalancingsettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoors_loadbalancingsettings')
        g.custom_command('delete', 'delete_frontdoors_loadbalancingsettings')
        g.custom_command('list', 'list_frontdoors_loadbalancingsettings')
        g.custom_command('show', 'show_frontdoors_loadbalancingsettings')
    with self.command_group('frontdoors loadbalancingsettings', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoors_loadbalancingsettings')
        g.custom_command('list', 'list_frontdoors_loadbalancingsettings')
    with self.command_group('frontdoors backendpools', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoors_backendpools')
        g.custom_command('delete', 'delete_frontdoors_backendpools')
        g.custom_command('list', 'list_frontdoors_backendpools')
        g.custom_command('show', 'show_frontdoors_backendpools')
    with self.command_group('frontdoors backendpools', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoors_backendpools')
        g.custom_command('list', 'list_frontdoors_backendpools')
    with self.command_group('frontdoors frontendendpoints', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoors_frontendendpoints')
        g.custom_command('delete', 'delete_frontdoors_frontendendpoints')
        g.custom_command('list', 'list_frontdoors_frontendendpoints')
        g.custom_command('show', 'show_frontdoors_frontendendpoints')
    with self.command_group('frontdoors frontendendpoints', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('show', 'show_frontdoors_frontendendpoints')
        g.custom_command('list', 'list_frontdoors_frontendendpoints')