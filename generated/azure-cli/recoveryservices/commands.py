# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.recoveryservices._client_factory import cf_recoveryservices
def load_command_table(self, _):

    recoveryservices_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.recoveryservices.operations#ApiManagementOperations.{}',
        client_factory=cf_recoveryservices)


    with self.command_group('recoveryservices resourcegroup vault replicationalertsetting', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationalertsetting')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationalertsetting')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationalertsetting')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationnetwork replicationnetworkmapping', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationprotectioncontainer', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationprotectioncontainer replicationmigrationitem', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationprotectioncontainer replicationprotecteditem', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationprotectioncontainer replicationprotectioncontainermapping', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationrecoveryservicesprovider', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationstorageclassification replicationstorageclassificationmapping', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping')
    with self.command_group('recoveryservices resourcegroup vault replicationfabric replicationvcenter', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter')
    with self.command_group('recoveryservices resourcegroup vault replicationpolicy', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationpolicy')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationpolicy')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationpolicy')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationpolicy')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationpolicy')
    with self.command_group('recoveryservices resourcegroup vault replicationrecoveryplan', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationrecoveryplan')
        g.custom_command('update', 'update_recoveryservices_resourcegroup_vault_replicationrecoveryplan')
        g.custom_command('delete', 'delete_recoveryservices_resourcegroup_vault_replicationrecoveryplan')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationrecoveryplan')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationrecoveryplan')
    with self.command_group('recoveryservices resourcegroup vault replicationvaultsetting', recoveryservices_sdk, client_factory=cf_recoveryservices) as g:
        g.custom_command('create', 'create_recoveryservices_resourcegroup_vault_replicationvaultsetting')
        g.custom_command('list', 'list_recoveryservices_resourcegroup_vault_replicationvaultsetting')
        g.custom_command('show', 'show_recoveryservices_resourcegroup_vault_replicationvaultsetting')