# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ._client_factory import cf_dedicated_cloud_node
    vmwarecs_dedicated_cloud_node = CliCommandType(
        operations_tmpl='azure.mgmt.vmwarecloudsimple.operations.dedicated_cloud_node_operations#DedicatedCloudNodeOperations.{}',
        client_factory=cf_dedicated_cloud_node)
    with self.command_group('vmwarecs', vmwarecs_dedicated_cloud_node, client_factory=cf_dedicated_cloud_node) as g:
        g.custom_command('create', 'create_vmwarecs')
        g.generic_update_command('update', custom_func_name='update_vmwarecs')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_vmwarecs')
        g.show_command('show', 'get')

    from ._client_factory import cf_dedicated_cloud_service
    vmwarecs_dedicated_cloud_service = CliCommandType(
        operations_tmpl='azure.mgmt.vmwarecloudsimple.operations.dedicated_cloud_service_operations#DedicatedCloudServiceOperations.{}',
        client_factory=cf_dedicated_cloud_service)
    with self.command_group('vmwarecs', vmwarecs_dedicated_cloud_service, client_factory=cf_dedicated_cloud_service) as g:
        g.custom_command('create', 'create_vmwarecs')
        g.generic_update_command('update', custom_func_name='update_vmwarecs')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_vmwarecs')
        g.show_command('show', 'get')

    from ._client_factory import cf_virtual_machine
    vmwarecs_virtual_machine = CliCommandType(
        operations_tmpl='azure.mgmt.vmwarecloudsimple.operations.virtual_machine_operations#VirtualMachineOperations.{}',
        client_factory=cf_virtual_machine)
    with self.command_group('vmwarecs', vmwarecs_virtual_machine, client_factory=cf_virtual_machine) as g:
        g.custom_command('create', 'create_vmwarecs')
        g.generic_update_command('update', custom_func_name='update_vmwarecs')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_vmwarecs')
        g.show_command('show', 'get')
