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

    from ._client_factory import cf_dedicated_cloud_nodes
    vmwarecs_dedicated_cloud_nodes = CliCommandType(
        operations_tmpl='azext_vmwarecs.vendored_sdks.vmwarecs.operations._dedicated_cloud_nodes_operations#DedicatedCloudNodesOperations.{}',
        client_factory=cf_dedicated_cloud_nodes)
    with self.command_group('vmwarecs', vmwarecs_dedicated_cloud_nodes, client_factory=cf_dedicated_cloud_nodes) as g:
        g.custom_command('create', 'create_vmwarecs')
        g.generic_update_command('update', custom_func_name='update_vmwarecs')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_vmwarecs')
        g.show_command('show', 'get')

    from ._client_factory import cf_dedicated_cloud_services
    vmwarecs_dedicated_cloud_services = CliCommandType(
        operations_tmpl='azext_vmwarecs.vendored_sdks.vmwarecs.operations._dedicated_cloud_services_operations#DedicatedCloudServicesOperations.{}',
        client_factory=cf_dedicated_cloud_services)
    with self.command_group('vmwarecs', vmwarecs_dedicated_cloud_services, client_factory=cf_dedicated_cloud_services) as g:
        g.custom_command('create', 'create_vmwarecs')
        g.generic_update_command('update', custom_func_name='update_vmwarecs')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_vmwarecs')
        g.show_command('show', 'get')

    from ._client_factory import cf_virtual_machines
    vmwarecs_virtual_machines = CliCommandType(
        operations_tmpl='azext_vmwarecs.vendored_sdks.vmwarecs.operations._virtual_machines_operations#VirtualMachinesOperations.{}',
        client_factory=cf_virtual_machines)
    with self.command_group('vmwarecs', vmwarecs_virtual_machines, client_factory=cf_virtual_machines) as g:
        g.custom_command('create', 'create_vmwarecs')
        g.generic_update_command('update', custom_func_name='update_vmwarecs')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_vmwarecs')
        g.show_command('show', 'get')
