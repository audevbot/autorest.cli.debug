# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.compute._client_factory import cf_compute
def load_command_table(self, _):

    compute_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.compute.operations#ApiManagementOperations.{}',
        client_factory=cf_compute)


    with self.command_group('compute', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_compute')
        g.custom_command('delete', 'delete_compute')
        g.custom_command('list', 'list_compute')
        g.custom_command('show', 'show_compute')
    with self.command_group('compute', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('show', 'show_compute')
        g.custom_command('list', 'list_compute')
    with self.command_group('compute images', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_compute_images')
        g.custom_command('delete', 'delete_compute_images')
        g.custom_command('list', 'list_compute_images')
        g.custom_command('show', 'show_compute_images')
    with self.command_group('compute images', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('show', 'show_compute_images')
        g.custom_command('list', 'list_compute_images')
    with self.command_group('compute images versions', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_compute_images_versions')
        g.custom_command('delete', 'delete_compute_images_versions')
        g.custom_command('list', 'list_compute_images_versions')
        g.custom_command('show', 'show_compute_images_versions')
    with self.command_group('compute images versions', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('show', 'show_compute_images_versions')
        g.custom_command('list', 'list_compute_images_versions')