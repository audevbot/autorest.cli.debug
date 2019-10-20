# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.subscriptions
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtSubscriptionTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtSubscriptionTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.subscriptions.Subscription
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_subscription(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription_operations.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "offer_type": "MS-AZR-0017P",
          "display_name": "Test Ea Azure Sub",
          "owners": [
            {
              "object_id": "973034ff-acb7-409c-b731-e789672c7b31"
            },
            {
              "object_id": "67439a9e-8519-4016-a630-f5f805eba567"
            }
          ],
          "additional_parameters": {
            "custom_data": {
              "key1": "value1",
              "key2": True
            }
          }
        }
        azure_operation_poller = self.mgmt_client.subscription_factory.create_subscription_in_enrollment_account(ENROLLMENT_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()