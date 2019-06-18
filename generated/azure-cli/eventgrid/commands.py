# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.eventgrid._client_factory import cf_eventgrid
def load_command_table(self, _):

    eventgrid_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.eventgrid.operations#ApiManagementOperations.{}',
        client_factory=cf_eventgrid)


    with self.command_group('eventgrid eventsubscriptions', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('create', 'create_eventgrid_eventsubscriptions')
        g.custom_command('update', 'update_eventgrid_eventsubscriptions')
        g.custom_command('delete', 'delete_eventgrid_eventsubscriptions')
        g.custom_command('list', 'list_eventgrid_eventsubscriptions')
        g.custom_command('show', 'show_eventgrid_eventsubscriptions')
    with self.command_group('eventgrid eventsubscriptions locations topictypes providers {providernamespace} {resourcetypename}', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('list', 'list_eventgrid_eventsubscriptions_locations_topictypes_providers_{providernamespace}_{resourcetypename}')
        g.custom_command('show', 'show_eventgrid_eventsubscriptions_locations_topictypes_providers_{providernamespace}_{resourcetypename}')
    with self.command_group('', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('list', 'list_')
    with self.command_group('eventgrid', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('create', 'create_eventgrid')
        g.custom_command('update', 'update_eventgrid')
        g.custom_command('delete', 'delete_eventgrid')
        g.custom_command('list', 'list_eventgrid')
        g.custom_command('show', 'show_eventgrid')
    with self.command_group('eventgrid providers {providernamespace} {resourcetypename}', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('list', 'list_eventgrid_providers_{providernamespace}_{resourcetypename}')
        g.custom_command('show', 'show_eventgrid_providers_{providernamespace}_{resourcetypename}')
    with self.command_group('eventgrid', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('list', 'list_eventgrid')
        g.custom_command('show', 'show_eventgrid')