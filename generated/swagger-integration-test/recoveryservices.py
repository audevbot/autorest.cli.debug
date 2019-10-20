# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.recoveryservices
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtRecoveryServicesTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtRecoveryServicesTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.recoveryservices.RecoveryServices
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_recoveryservices(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {
          "name": "swaggerExample",
          "type": "Microsoft.RecoveryServices/Vaults"
        }
        azure_operation_poller = self.mgmt_client.recovery_services.check_name_availability(resource_group.name, LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "swaggerExample2",
          "type": "Microsoft.RecoveryServices/Vaults"
        }
        azure_operation_poller = self.mgmt_client.recovery_services.check_name_availability(resource_group.name, LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.vaults.list_by_subscription_id(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.vaults.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.vaults.get(resource_group.name, VAULT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "sku": {
            "name": "Standard"
          },
          "location": "West US"
        }
        azure_operation_poller = self.mgmt_client.vaults.create_or_update(resource_group.name, VAULT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.vaults.delete(resource_group.name, VAULT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "patch_key": "PatchKeyUpdated"
          }
        }
        azure_operation_poller = self.mgmt_client.vaults.update(resource_group.name, VAULT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.operations.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.vault_extended_info.get(resource_group.name, VAULT_NAME, EXTENDED_INFORMATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "integrity_key": "J99wzS27fmJ+Wjot7xO5wA==",
            "algorithm": "None"
          }
        }
        azure_operation_poller = self.mgmt_client.vault_extended_info.create_or_update(resource_group.name, VAULT_NAME, EXTENDED_INFORMATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "integrity_key": "J99wzS27fmJ+Wjot7xO5wA==",
            "algorithm": "None"
          }
        }
        azure_operation_poller = self.mgmt_client.vault_extended_info.update(resource_group.name, VAULT_NAME, EXTENDED_INFORMATION_NAME, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()