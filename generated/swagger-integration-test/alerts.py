# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import time
import mock
import unittest

from azure_devtools.scenario_tests.const import MOCKED_SUBSCRIPTION_ID
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, LiveScenarioTest, ResourceGroupPreparer, create_random_name, live_only, record_only
from azure.cli.core.util import get_file_json


class ResourceGroupScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_rg_scenario')
    def test_resource_group(self, resource_group):

        self.cmd('group create -n {rg} -l westus --tag a=b c', checks=[
            self.check('name', '{rg}'),
            self.check('tags', {'a': 'b', 'c': ''})
        ])

        self.kwargs['sub'] = self.get_subscription_id()
        self.kwargs['name'] = 'zimsxyzname'

        # alertsmanagement_alertsmetadata_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.AlertsManagement/alertsMetaData?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_alerts_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/alerts?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_alerts_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/alerts/{ALERT_NAME}?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_alerts_changestate_post
        body = (
                 '{'
                 '  "comments": "Acknowledging alert"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/alerts/{ALERT_NAME}/changestate?api-version=2019-05-05-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # alertsmanagement_alerts_history_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/alerts/{ALERT_NAME}/history?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_alertssummary_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/alertsSummary?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_smartgroups_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/smartGroups?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_smartgroups_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/smartGroups/{SMART_GROUP_NAME}?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_smartgroups_changestate_post
        body = (
                 '{'
                 '  "comments": "Acknowledging smart group"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/smartGroups/{SMART_GROUP_NAME}/changeState?api-version=2019-05-05-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # alertsmanagement_smartgroups_history_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/smartGroups/{SMART_GROUP_NAME}/history?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_actionrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.AlertsManagement/actionRules?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_actionrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.AlertsManagement/actionRules?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_actionrules_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.AlertsManagement/actionRules/{ACTION_RULE_NAME}?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_actionrules_put
        body = (
                 '{'
                 '  "location": "Global",'
                 '  "tags": {},'
                 '  "properties": {'
                 '    "scope": {'
                 '      "scopeType": "ResourceGroup",'
                 '      "values": ['
                 '        "/subscriptions/1e3ff1c0-771a-4119-a03b-be82a51e232d/resourceGroups/alertscorrelationrg"'
                 '      ]'
                 '    },'
                 '    "conditions": {'
                 '      "severity": {'
                 '        "operator": "Equals",'
                 '        "values": ['
                 '          "Sev0",'
                 '          "Sev2"'
                 '        ]'
                 '      },'
                 '      "monitorService": {'
                 '        "operator": "Equals",'
                 '        "values": ['
                 '          "Platform",'
                 '          "Application Insights"'
                 '        ]'
                 '      },'
                 '      "monitorCondition": {'
                 '        "operator": "Equals",'
                 '        "values": ['
                 '          "Fired"'
                 '        ]'
                 '      },'
                 '      "targetResourceType": {'
                 '        "operator": "NotEquals",'
                 '        "values": ['
                 '          "Microsoft.Compute/VirtualMachines"'
                 '        ]'
                 '      }'
                 '    },'
                 '    "type": "Suppression",'
                 '    "suppressionConfig": {'
                 '      "recurrenceType": "Daily",'
                 '      "schedule": {'
                 '        "startDate": "12/09/2018",'
                 '        "endDate": "12/18/2018",'
                 '        "startTime": "06:00:00",'
                 '        "endTime": "14:00:00"'
                 '      }'
                 '    },'
                 '    "description": "Action rule on resource group for daily suppression",'
                 '    "status": "Enabled"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.AlertsManagement/actionRules/{ACTION_RULE_NAME}?api-version=2019-05-05-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # alertsmanagement_actionrules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.AlertsManagement/actionRules/{ACTION_RULE_NAME}?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_actionrules_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.AlertsManagement/actionRules/{ACTION_RULE_NAME}?api-version=2019-05-05-preview '
                 , checks=[
                          ])

        # alertsmanagement_smartdetectoralertrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/microsoft.alertsManagement/smartDetectorAlertRules?api-version=2019-06-01 '
                 , checks=[
                          ])

        # alertsmanagement_smartdetectoralertrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/microsoft.alertsManagement/smartDetectorAlertRules?api-version=2019-06-01 '
                 , checks=[
                          ])

        # alertsmanagement_smartdetectoralertrules_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{SMART_DETECTOR_ALERT_RULE_NAME}?api-version=2019-06-01 '
                 , checks=[
                          ])

        # alertsmanagement_smartdetectoralertrules_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "description": "Sample smart detector alert rule description",'
                 '    "state": "Enabled",'
                 '    "severity": "Sev3",'
                 '    "frequency": "PT5M",'
                 '    "detector": {'
                 '      "id": "VMMemoryLeak"'
                 '    },'
                 '    "scope": ['
                 '      "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1"'
                 '    ],'
                 '    "actionGroups": {'
                 '      "customEmailSubject": "My custom email subject",'
                 '      "customWebhookPayload": "{\"AlertRuleName\":\"#alertrulename\"}",'
                 '      "groupIds": ['
                 '        "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourcegroups/actionGroups/providers/microsoft.insights/actiongroups/MyActionGroup"'
                 '      ]'
                 '    },'
                 '    "throttling": {'
                 '      "duration": "PT20M"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{SMART_DETECTOR_ALERT_RULE_NAME}?api-version=2019-06-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # alertsmanagement_smartdetectoralertrules_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{SMART_DETECTOR_ALERT_RULE_NAME}?api-version=2019-06-01 '
                 , checks=[
                          ])

        # alertsmanagement_smartdetectoralertrules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{SMART_DETECTOR_ALERT_RULE_NAME}?api-version=2019-06-01 '
                 , checks=[
                          ])