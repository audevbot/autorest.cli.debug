# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):


    from ._client_factory import cf_smart_detector_alert_rules
    alerts_smart_detector_alert_rules = CliCommandType(
        operations_tmpl='azure.mgmt.alertsmanagement.operations.smart_detector_alert_rules_operations#SmartDetectorAlertRulesOperations.{}',
        client_factory=cf_smart_detector_alert_rules)
    with self.command_group('alerts', alerts_smart_detector_alert_rules, client_factory=cf_smart_detector_alert_rules) as g:
        g.custom_command('create', 'create_alerts')
        g.custom_command('update', 'update_alerts')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_alerts')
        g.command('show', 'get')
