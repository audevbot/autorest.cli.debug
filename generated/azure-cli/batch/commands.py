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


    with self.command_group('batch', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch')
        g.custom_command('update', 'update_batch')
        g.custom_command('delete', 'delete_batch')
        g.custom_command('list', 'list_batch')
        g.custom_command('show', 'show_batch')
    with self.command_group('batch', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batch')
        g.custom_command('list', 'list_batch')
    with self.command_group('batch applications versions', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_applications_versions')
        g.custom_command('delete', 'delete_batch_applications_versions')
        g.custom_command('list', 'list_batch_applications_versions')
        g.custom_command('show', 'show_batch_applications_versions')
    with self.command_group('batch applications versions', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batch_applications_versions')
        g.custom_command('list', 'list_batch_applications_versions')
    with self.command_group('batch applications', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_applications')
        g.custom_command('update', 'update_batch_applications')
        g.custom_command('delete', 'delete_batch_applications')
        g.custom_command('list', 'list_batch_applications')
        g.custom_command('show', 'show_batch_applications')
    with self.command_group('batch applications', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batch_applications')
        g.custom_command('list', 'list_batch_applications')
    with self.command_group('batch', batch_sdk, client_factory=cf_batch) as g:
    with self.command_group('', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('list', 'list_')
    with self.command_group('batch certificates', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_certificates')
        g.custom_command('update', 'update_batch_certificates')
        g.custom_command('delete', 'delete_batch_certificates')
        g.custom_command('list', 'list_batch_certificates')
        g.custom_command('show', 'show_batch_certificates')
    with self.command_group('batch certificates', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batch_certificates')
        g.custom_command('list', 'list_batch_certificates')
    with self.command_group('batch pools', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('create', 'create_batch_pools')
        g.custom_command('update', 'update_batch_pools')
        g.custom_command('delete', 'delete_batch_pools')
        g.custom_command('list', 'list_batch_pools')
        g.custom_command('show', 'show_batch_pools')
    with self.command_group('batch pools', batch_sdk, client_factory=cf_batch) as g:
        g.custom_command('show', 'show_batch_pools')
        g.custom_command('list', 'list_batch_pools')