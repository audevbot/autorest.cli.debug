# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.automation
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtAutomationManagementTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtAutomationManagementTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.automation.AutomationManagement
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_automationjob(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.get_output(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.get_runbook_content(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.suspend(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.stop(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.get(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "runbook": {
              "name": "TestRunbook"
            },
            "parameters": {
              "key01": "value01",
              "key02": "value02"
            },
            "run_on": ""
          }
        }
        azure_operation_poller = self.mgmt_client.job.create(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.list_by_automation_account(resource_group.name, AUTOMATION_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job.resume(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job_stream.get(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, STREAM_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.job_stream.list_by_job(resource_group.name, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()