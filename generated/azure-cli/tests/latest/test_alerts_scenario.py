# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimgmtScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_apimgmt')
    def test_apimgmt(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

# create_or_update -- create
        self.cmd('alerts create  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule" --description "Sample smart detector alert rule description" --state "Enabled" --severity "Sev3" --frequency "PT5M" --scope "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1"', checks=[
        ])

        self.cmd('alerts create  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule"', checks=[
        ])

# create_or_update -- update
        self.cmd('alerts update  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule" --description "Sample smart detector alert rule description" --state "Enabled" --severity "Sev3" --frequency "PT5M" --scope "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1"', checks=[
        ])

        self.cmd('alerts update  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule"', checks=[
        ])

# delete -- delete
        self.cmd('alerts delete  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule"', checks=[
        ])

        self.cmd('alerts delete  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('alerts list  --resource-group "MyAlertRules"', checks=[
        ])

        self.cmd('alerts list  --resource-group "MyAlertRules"', checks=[
        ])

# list -- list
        self.cmd('alerts list  --resource-group "MyAlertRules"', checks=[
        ])

        self.cmd('alerts list  --resource-group "MyAlertRules"', checks=[
        ])

# get -- show
        self.cmd('alerts show  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule"', checks=[
        ])

        self.cmd('alerts show  --resource-group "MyAlertRules" --alert-rule-name "MyAlertRule"', checks=[
        ])
