# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.managementgroups
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtManagementGroupsClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtManagementGroupsClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.managementgroups.ManagementGroupsClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_mgmtgroups(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_groups.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_groups.get(MANAGEMENT_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_groups.get(MANAGEMENT_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_groups.get(MANAGEMENT_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "id": "/providers/Microsoft.Management/managementGroups/ChildGroup",
          "type": "/providers/Microsoft.Management/managementGroups",
          "name": "ChildGroup",
          "properties": {
            "tenant_id": "20000000-0000-0000-0000-000000000000",
            "display_name": "ChildGroup",
            "details": {
              "parent": {
                "id": "/providers/Microsoft.Management/managementGroups/RootGroup"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.management_groups.create_or_update(MANAGEMENT_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "display_name": "AlternateDisplayName",
          "parent_group_id": "/providers/Microsoft.Management/managementGroups/AlternateRootGroup"
        }
        azure_operation_poller = self.mgmt_client.management_groups.update(MANAGEMENT_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_groups.delete(MANAGEMENT_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_groups.get_descendants(MANAGEMENT_GROUP_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_group_subscriptions.create(MANAGEMENT_GROUP_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.management_group_subscriptions.delete(MANAGEMENT_GROUP_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "nameTocheck",
          "type": "/providers/Microsoft.Management/managementGroups"
        }
        azure_operation_poller = self.mgmt_client..check_name_availability(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client..start_tenant_backfill(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client..tenant_backfill_status(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.entities.list(, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()