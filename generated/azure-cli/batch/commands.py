# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.batch._client_factory import cf_batch
def load_command_table(self, _):

    batch_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.batch.operations#ApiManagementOperations.{}',
        client_factory=cf_batch)


    with self.command_group('batch batchaccount', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_batchaccount')
        g.custom_command('update', 'update_batch_batchaccount')
        g.custom_command('delete', 'delete_batch_batchaccount')
        g.custom_command('list', 'list_batch_batchaccount')
        g.custom_command('show', 'show_batch_batchaccount')
    with self.command_group('batch batchaccount application version', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_batchaccount_application_version')
        g.custom_command('delete', 'delete_batch_batchaccount_application_version')
        g.custom_command('list', 'list_batch_batchaccount_application_version')
        g.custom_command('show', 'show_batch_batchaccount_application_version')
    with self.command_group('batch batchaccount application', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_batchaccount_application')
        g.custom_command('update', 'update_batch_batchaccount_application')
        g.custom_command('delete', 'delete_batch_batchaccount_application')
        g.custom_command('list', 'list_batch_batchaccount_application')
        g.custom_command('show', 'show_batch_batchaccount_application')
    with self.command_group('batch batchaccount certificate', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_batchaccount_certificate')
        g.custom_command('update', 'update_batch_batchaccount_certificate')
        g.custom_command('delete', 'delete_batch_batchaccount_certificate')
        g.custom_command('list', 'list_batch_batchaccount_certificate')
        g.custom_command('show', 'show_batch_batchaccount_certificate')
    with self.command_group('batch batchaccount pool', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_batchaccount_pool')
        g.custom_command('update', 'update_batch_batchaccount_pool')
        g.custom_command('delete', 'delete_batch_batchaccount_pool')
        g.custom_command('list', 'list_batch_batchaccount_pool')
        g.custom_command('show', 'show_batch_batchaccount_pool')