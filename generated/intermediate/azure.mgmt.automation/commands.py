# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.automation._client_factory import cf_automation
def load_command_table(self, _):

    automation_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.automation.operations#ApiManagementOperations.{}',
        client_factory=cf_automation)


    with self.command_group('automationaccounts jobs', automation_sdk, client_factory=cf_automation) as g:
        g.custom_command('create', 'create_automationaccounts_jobs')
        g.custom_command('list', 'list_automationaccounts_jobs')
        g.custom_command('show', 'show_automationaccounts_jobs')
    with self.command_group('automationaccounts jobs', automation_sdk, client_factory=cf_automation) as g:
        g.custom_command('show', 'show_automationaccounts_jobs')
        g.custom_command('list', 'list_automationaccounts_jobs')
    with self.command_group('automationaccounts jobs streams', automation_sdk, client_factory=cf_automation) as g:
        g.custom_command('show', 'show_automationaccounts_jobs_streams')
        g.custom_command('list', 'list_automationaccounts_jobs_streams')