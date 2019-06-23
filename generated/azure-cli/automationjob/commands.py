# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.automationjob._client_factory import cf_automationjob
def load_command_table(self, _):

    automationjob_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.automationjob.operations#ApiManagementOperations.{}',
        client_factory=cf_automationjob)


    with self.command_group('automationjob automationaccount job', automationjob_sdk, client_factory=cf_automationjob) as g:
        g.custom_command('create', 'create_automationjob_automationaccount_job')
        g.custom_command('list', 'list_automationjob_automationaccount_job')
        g.custom_command('show', 'show_automationjob_automationaccount_job')