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


    with self.command_group('batchaccounts', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batchaccounts')
        g.custom_command('update', 'update_batchaccounts')
        g.custom_command('delete', 'delete_batchaccounts')
        g.custom_command('list', 'list_batchaccounts')
        g.custom_command('show', 'show_batchaccounts')
    with self.command_group('batchaccounts', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batchaccounts')
        g.custom_command('list', 'list_batchaccounts')
    with self.command_group('batchaccounts applications versions', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batchaccounts_applications_versions')
        g.custom_command('delete', 'delete_batchaccounts_applications_versions')
        g.custom_command('list', 'list_batchaccounts_applications_versions')
        g.custom_command('show', 'show_batchaccounts_applications_versions')
    with self.command_group('batchaccounts applications versions', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batchaccounts_applications_versions')
        g.custom_command('list', 'list_batchaccounts_applications_versions')
    with self.command_group('batchaccounts applications', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batchaccounts_applications')
        g.custom_command('update', 'update_batchaccounts_applications')
        g.custom_command('delete', 'delete_batchaccounts_applications')
        g.custom_command('list', 'list_batchaccounts_applications')
        g.custom_command('show', 'show_batchaccounts_applications')
    with self.command_group('batchaccounts applications', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batchaccounts_applications')
        g.custom_command('list', 'list_batchaccounts_applications')
    with self.command_group('locations', batch_sdk, client_factory=cf_batch) as g:
    with self.command_group('', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('list', 'list_')
    with self.command_group('batchaccounts certificates', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batchaccounts_certificates')
        g.custom_command('update', 'update_batchaccounts_certificates')
        g.custom_command('delete', 'delete_batchaccounts_certificates')
        g.custom_command('list', 'list_batchaccounts_certificates')
        g.custom_command('show', 'show_batchaccounts_certificates')
    with self.command_group('batchaccounts certificates', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batchaccounts_certificates')
        g.custom_command('list', 'list_batchaccounts_certificates')
    with self.command_group('batchaccounts pools', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batchaccounts_pools')
        g.custom_command('update', 'update_batchaccounts_pools')
        g.custom_command('delete', 'delete_batchaccounts_pools')
        g.custom_command('list', 'list_batchaccounts_pools')
        g.custom_command('show', 'show_batchaccounts_pools')
    with self.command_group('batchaccounts pools', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batchaccounts_pools')
        g.custom_command('list', 'list_batchaccounts_pools')