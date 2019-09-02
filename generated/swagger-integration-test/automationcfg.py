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

        # automation_automationaccounts_softwareupdateconfigurations_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "updateConfiguration": {'
                 '      "operatingSystem": "Windows",'
                 '      "duration": "PT2H0M",'
                 '      "windows": {'
                 '        "excludedKbNumbers": ['
                 '          "168934",'
                 '          "168973"'
                 '        ],'
                 '        "includedUpdateClassifications": "Critical",'
                 '        "rebootSetting": "IfRequired"'
                 '      },'
                 '      "azureVirtualMachines": ['
                 '        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-01",'
                 '        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-02",'
                 '        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-03"'
                 '      ],'
                 '      "nonAzureComputerNames": ['
                 '        "box1.contoso.com",'
                 '        "box2.contoso.com"'
                 '      ],'
                 '      "targets": {'
                 '        "azureQueries": ['
                 '          {'
                 '            "scope": ['
                 '              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources",'
                 '              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067"'
                 '            ],'
                 '            "tagSettings": {'
                 '              "tags": ['
                 '                {'
                 '                  "tag1": ['
                 '                    "tag1Value1",'
                 '                    "tag1Value2",'
                 '                    "tag1Value3"'
                 '                  ]'
                 '                },'
                 '                {'
                 '                  "tag2": ['
                 '                    "tag2Value1",'
                 '                    "tag2Value2",'
                 '                    "tag2Value3"'
                 '                  ]'
                 '                }'
                 '              ],'
                 '              "filterOperator": "All"'
                 '            },'
                 '            "locations": ['
                 '              "Japan East",'
                 '              "UK South"'
                 '            ]'
                 '          }'
                 '        ],'
                 '        "nonAzureQueries": ['
                 '          {'
                 '            "functionAlias": "SavedSearch1",'
                 '            "workspaceId": "WorkspaceId1"'
                 '          },'
                 '          {'
                 '            "functionAlias": "SavedSearch2",'
                 '            "workspaceId": "WorkspaceId2"'
                 '          }'
                 '        ]'
                 '      }'
                 '    },'
                 '    "scheduleInfo": {'
                 '      "frequency": "Hour",'
                 '      "startTime": "2017-10-19T12:22:57+00:00",'
                 '      "timeZone": "America/Los_Angeles",'
                 '      "interval": "1",'
                 '      "expiryTime": "2018-11-09T11:22:57+00:00",'
                 '      "advancedSchedule": {'
                 '        "weekDays": ['
                 '          "Monday",'
                 '          "Thursday"'
                 '        ]'
                 '      }'
                 '    },'
                 '    "tasks": {'
                 '      "preTask": {'
                 '        "source": "HelloWorld",'
                 '        "parameters": {'
                 '          "COMPUTERNAME": "Computer1"'
                 '        }'
                 '      },'
                 '      "postTask": {'
                 '        "source": "GetCache",'
                 '        "parameters": null'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/softwareUpdateConfigurations/{SOFTWARE_UPDATE_CONFIGURATION_NAME}?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # automation_automationaccounts_softwareupdateconfigurations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/softwareUpdateConfigurations/{SOFTWARE_UPDATE_CONFIGURATION_NAME}?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_softwareupdateconfigurations_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/softwareUpdateConfigurations/{SOFTWARE_UPDATE_CONFIGURATION_NAME}?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_softwareupdateconfigurations_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/softwareUpdateConfigurations?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_softwareupdateconfigurations_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/softwareUpdateConfigurations?api-version=2017-05-15-preview '
                 , checks=[
                          ])