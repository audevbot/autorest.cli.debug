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

        BODY = {
          "name": "swaggerExample",
          "type": "Microsoft.RecoveryServices/Vaults"
        }
        output = mgmt_client.recovery_services.check_name_availability(RESOURCE_GROUP, LOCATION_NAME, , BODY)
        BODY = {
          "name": "swaggerExample2",
          "type": "Microsoft.RecoveryServices/Vaults"
        }
        output = mgmt_client.recovery_services.check_name_availability(RESOURCE_GROUP, LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.vaults.list_by_subscription_id(, BODY)
        BODY = {}
        output = mgmt_client.vaults.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.vaults.get(RESOURCE_GROUP, VAULT_NAME, BODY)
        BODY = {
          "sku": {
            "name": "Standard"
          },
          "location": "West US"
        }
        output = mgmt_client.vaults.create_or_update(RESOURCE_GROUP, VAULT_NAME, BODY)
        BODY = {}
        output = mgmt_client.vaults.delete(RESOURCE_GROUP, VAULT_NAME, BODY)
        BODY = {
          "tags": {
            "patch_key": "PatchKeyUpdated"
          }
        }
        output = mgmt_client.vaults.update(RESOURCE_GROUP, VAULT_NAME, BODY)
        BODY = {}
        output = mgmt_client.operations.list(, BODY)
        BODY = {}
        output = mgmt_client.vault_extended_info.get(RESOURCE_GROUP, VAULT_NAME, EXTENDED_INFORMATION_NAME, BODY)
        BODY = {
          "properties": {
            "integrity_key": "J99wzS27fmJ+Wjot7xO5wA==",
            "algorithm": "None"
          }
        }
        output = mgmt_client.vault_extended_info.create_or_update(RESOURCE_GROUP, VAULT_NAME, EXTENDED_INFORMATION_NAME, BODY)
        BODY = {
          "properties": {
            "integrity_key": "J99wzS27fmJ+Wjot7xO5wA==",
            "algorithm": "None"
          }
        }
        output = mgmt_client.vault_extended_info.update(RESOURCE_GROUP, VAULT_NAME, EXTENDED_INFORMATION_NAME, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()