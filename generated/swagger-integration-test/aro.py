# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.containerservice
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtOpenShiftTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtOpenShiftTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.containerservice.OpenShift
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_aro(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_shift_managed_clusters.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_shift_managed_clusters.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_shift_managed_clusters.get(resource_group.name, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "location1",
          "tags": {
            "tier": "production",
            "archv2": ""
          },
          "properties": {
            "open_shift_version": "v3.11",
            "network_profile": {
              "vnet_cidr": "10.0.0.0/8"
            },
            "master_pool_profile": {
              "name": "master",
              "count": "3",
              "vm_size": "Standard_D4s_v3",
              "os_type": "Linux",
              "subnet_cidr": "10.0.0.0/24"
            },
            "agent_pool_profiles": [
              {
                "name": "infra",
                "role": "infra",
                "count": "2",
                "vm_size": "Standard_D4s_v3",
                "os_type": "Linux",
                "subnet_cidr": "10.0.0.0/24"
              },
              {
                "name": "compute",
                "role": "compute",
                "count": "4",
                "vm_size": "Standard_D4s_v3",
                "os_type": "Linux",
                "subnet_cidr": "10.0.0.0/24"
              }
            ],
            "router_profiles": [
              {
                "name": "default"
              }
            ],
            "auth_profile": {
              "identity_providers": [
                {
                  "name": "Azure AD",
                  "provider": {
                    "kind": "AADIdentityProvider",
                    "client_id": "clientId",
                    "secret": "secret",
                    "tenant_id": "tenantId",
                    "customer_admin_group_id": "customerAdminGroupId"
                  }
                }
              ]
            }
          }
        }
        azure_operation_poller = self.mgmt_client.open_shift_managed_clusters.create_or_update(resource_group.name, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "tier": "testing",
            "archv3": ""
          }
        }
        azure_operation_poller = self.mgmt_client.open_shift_managed_clusters.update_tags(resource_group.name, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_shift_managed_clusters.delete(resource_group.name, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()