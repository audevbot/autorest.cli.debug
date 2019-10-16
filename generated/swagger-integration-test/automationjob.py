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

        # Get Job Output
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/output?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # Get Job Runbook Content
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/runbookContent?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # Suspend job
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/suspend?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Stop job
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/stop?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Get job
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # Create job
        body = (
                 '{'
                 '  "properties": {'
                 '    "runbook": {'
                 '      "name": "TestRunbook"'
                 '    },'
                 '    "parameters": {'
                 '      "key01": "value01",'
                 '      "key02": "value02"'
                 '    },'
                 '    "runOn": ""'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # List jobs by automation account
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # Resume job
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/resume?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Get job stream
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/streams/{STREAM_NAME}?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # List job streams by job name
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/streams?api-version=2017-05-15-preview '
                 , checks=[
                          ])