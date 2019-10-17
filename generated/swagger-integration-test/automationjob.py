# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

        BODY = {}
        output = mgmt_client.job.get_output(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        BODY = {}
        output = mgmt_client.job.get_runbook_content(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        BODY = {}
        output = mgmt_client.job.suspend(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        BODY = {}
        output = mgmt_client.job.stop(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        BODY = {}
        output = mgmt_client.job.get(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, BODY)
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
        output = mgmt_client.job.create(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, BODY)
        BODY = {}
        output = mgmt_client.job.list_by_automation_account(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.job.resume(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)
        BODY = {}
        output = mgmt_client.job_stream.get(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, STREAM_NAME, BODY)
        BODY = {}
        output = mgmt_client.job_stream.list_by_job(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, JOB_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()