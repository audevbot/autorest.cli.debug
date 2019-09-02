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

        # automation_automationaccounts_jobs_output_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/output?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_runbookcontent_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/runbookContent?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_suspend_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/suspend?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_stop_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/stop?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_put
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

        # automation_automationaccounts_jobs_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_resume_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/resume?api-version=2017-05-15-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_streams_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/streams/{STREAM_NAME}?api-version=2017-05-15-preview '
                 , checks=[
                          ])

        # automation_automationaccounts_jobs_streams_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Automation/automationAccounts/{AUTOMATION_ACCOUNT_NAME}/jobs/{JOB_NAME}/streams?api-version=2017-05-15-preview '
                 , checks=[
                          ])