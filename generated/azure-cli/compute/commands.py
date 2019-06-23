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


    with self.command_group('compute gallery', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_compute_gallery')
        g.custom_command('update', 'update_compute_gallery')
        g.custom_command('delete', 'delete_compute_gallery')
        g.custom_command('list', 'list_compute_gallery')
        g.custom_command('show', 'show_compute_gallery')
    with self.command_group('compute gallery image', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_compute_gallery_image')
        g.custom_command('update', 'update_compute_gallery_image')
        g.custom_command('delete', 'delete_compute_gallery_image')
        g.custom_command('list', 'list_compute_gallery_image')
        g.custom_command('show', 'show_compute_gallery_image')
    with self.command_group('compute gallery image version', compute_sdk, client_factory=cf_compute) as g:
        g.custom_command('create', 'create_compute_gallery_image_version')
        g.custom_command('update', 'update_compute_gallery_image_version')
        g.custom_command('delete', 'delete_compute_gallery_image_version')
        g.custom_command('list', 'list_compute_gallery_image_version')
        g.custom_command('show', 'show_compute_gallery_image_version')