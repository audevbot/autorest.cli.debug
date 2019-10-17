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
        output = mgmt_client.management_groups.list(, BODY)
BODY = {}
        output = mgmt_client.management_groups.get(MANAGEMENT_GROUP_NAME, BODY)
BODY = {}
        output = mgmt_client.management_groups.get(MANAGEMENT_GROUP_NAME, BODY)
BODY = {}
        output = mgmt_client.management_groups.get(MANAGEMENT_GROUP_NAME, BODY)
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
        output = mgmt_client.management_groups.create_or_update(MANAGEMENT_GROUP_NAME, BODY)
BODY = {
  "display_name": "AlternateDisplayName",
  "parent_group_id": "/providers/Microsoft.Management/managementGroups/AlternateRootGroup"
}
        output = mgmt_client.management_groups.update(MANAGEMENT_GROUP_NAME, BODY)
BODY = {}
        output = mgmt_client.management_groups.delete(MANAGEMENT_GROUP_NAME, BODY)
BODY = {}
        output = mgmt_client.management_groups.get_descendants(MANAGEMENT_GROUP_NAME, , BODY)
BODY = {}
        output = mgmt_client.management_group_subscriptions.create(MANAGEMENT_GROUP_NAME, , BODY)
BODY = {}
        output = mgmt_client.management_group_subscriptions.delete(MANAGEMENT_GROUP_NAME, , BODY)
BODY = {
  "name": "nameTocheck",
  "type": "/providers/Microsoft.Management/managementGroups"
}
        output = mgmt_client..check_name_availability(, BODY)
BODY = {}
        output = mgmt_client..start_tenant_backfill(, BODY)
BODY = {}
        output = mgmt_client..tenant_backfill_status(, BODY)
BODY = {}
        output = mgmt_client.entities.list(, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()