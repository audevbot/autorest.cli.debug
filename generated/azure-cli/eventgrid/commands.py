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


    with self.command_group('eventgrid  eventsubscription', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('create', 'create_eventgrid__eventsubscription')
        g.custom_command('update', 'update_eventgrid__eventsubscription')
        g.custom_command('delete', 'delete_eventgrid__eventsubscription')
        g.custom_command('list', 'list_eventgrid__eventsubscription')
        g.custom_command('show', 'show_eventgrid__eventsubscription')
    with self.command_group('eventgrid topic', eventgrid_sdk, client_factory=cf_eventgrid) as g:
        g.custom_command('create', 'create_eventgrid_topic')
        g.custom_command('update', 'update_eventgrid_topic')
        g.custom_command('delete', 'delete_eventgrid_topic')
        g.custom_command('list', 'list_eventgrid_topic')
        g.custom_command('show', 'show_eventgrid_topic')