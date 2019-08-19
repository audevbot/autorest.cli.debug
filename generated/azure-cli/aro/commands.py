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

    from ._client_factory import cf_open_shift_managed_clusters
    aro_open_shift_managed_clusters = CliCommandType(
        operations_tmpl='azure.mgmt.containerservice.operations.open_shift_managed_clusters_operations#OpenShiftManagedClustersOperations.{}',
        client_factory=cf_open_shift_managed_clusters)
    with self.command_group('aro', aro_open_shift_managed_clusters, client_factory=cf_open_shift_managed_clusters) as g:
        g.custom_command('create', 'create_aro')
        g.generic_update_command('update', custom_func_name='update_aro')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_aro')
        g.show_command('show', 'get')
