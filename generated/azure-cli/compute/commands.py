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


    with self.command_group('galleries', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_galleries')
        g.custom_command('delete', 'delete_galleries')
        g.custom_command('list', 'list_galleries')
        g.custom_command('show', 'show_galleries')
    with self.command_group('galleries', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('show', 'show_galleries')
        g.custom_command('list', 'list_galleries')
    with self.command_group('galleries images', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_galleries_images')
        g.custom_command('delete', 'delete_galleries_images')
        g.custom_command('list', 'list_galleries_images')
        g.custom_command('show', 'show_galleries_images')
    with self.command_group('galleries images', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('show', 'show_galleries_images')
        g.custom_command('list', 'list_galleries_images')
    with self.command_group('galleries images versions', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_galleries_images_versions')
        g.custom_command('delete', 'delete_galleries_images_versions')
        g.custom_command('list', 'list_galleries_images_versions')
        g.custom_command('show', 'show_galleries_images_versions')
    with self.command_group('galleries images versions', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('show', 'show_galleries_images_versions')
        g.custom_command('list', 'list_galleries_images_versions')