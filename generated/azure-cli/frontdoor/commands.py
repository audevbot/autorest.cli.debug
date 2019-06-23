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


    with self.command_group('frontdoor frontdoor', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontdoor')
        g.custom_command('update', 'update_frontdoor_frontdoor')
        g.custom_command('delete', 'delete_frontdoor_frontdoor')
        g.custom_command('list', 'list_frontdoor_frontdoor')
        g.custom_command('show', 'show_frontdoor_frontdoor')
    with self.command_group('frontdoor frontdoor routingrule', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontdoor_routingrule')
        g.custom_command('update', 'update_frontdoor_frontdoor_routingrule')
        g.custom_command('delete', 'delete_frontdoor_frontdoor_routingrule')
        g.custom_command('list', 'list_frontdoor_frontdoor_routingrule')
        g.custom_command('show', 'show_frontdoor_frontdoor_routingrule')
    with self.command_group('frontdoor frontdoor healthprobesetting', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontdoor_healthprobesetting')
        g.custom_command('update', 'update_frontdoor_frontdoor_healthprobesetting')
        g.custom_command('delete', 'delete_frontdoor_frontdoor_healthprobesetting')
        g.custom_command('list', 'list_frontdoor_frontdoor_healthprobesetting')
        g.custom_command('show', 'show_frontdoor_frontdoor_healthprobesetting')
    with self.command_group('frontdoor frontdoor loadbalancingsetting', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontdoor_loadbalancingsetting')
        g.custom_command('update', 'update_frontdoor_frontdoor_loadbalancingsetting')
        g.custom_command('delete', 'delete_frontdoor_frontdoor_loadbalancingsetting')
        g.custom_command('list', 'list_frontdoor_frontdoor_loadbalancingsetting')
        g.custom_command('show', 'show_frontdoor_frontdoor_loadbalancingsetting')
    with self.command_group('frontdoor frontdoor backendpool', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontdoor_backendpool')
        g.custom_command('update', 'update_frontdoor_frontdoor_backendpool')
        g.custom_command('delete', 'delete_frontdoor_frontdoor_backendpool')
        g.custom_command('list', 'list_frontdoor_frontdoor_backendpool')
        g.custom_command('show', 'show_frontdoor_frontdoor_backendpool')
    with self.command_group('frontdoor frontdoor frontendendpoint', frontdoor_sdk, client_factory=cf_frontdoor) as g:
        g.custom_command('create', 'create_frontdoor_frontdoor_frontendendpoint')
        g.custom_command('update', 'update_frontdoor_frontdoor_frontendendpoint')
        g.custom_command('delete', 'delete_frontdoor_frontdoor_frontendendpoint')
        g.custom_command('list', 'list_frontdoor_frontdoor_frontendendpoint')
        g.custom_command('show', 'show_frontdoor_frontdoor_frontendendpoint')