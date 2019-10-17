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
        output = mgmt_client.open_shift_managed_clusters.list(, BODY)
        BODY = {}
        output = mgmt_client.open_shift_managed_clusters.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.open_shift_managed_clusters.get(RESOURCE_GROUP, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
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
        output = mgmt_client.open_shift_managed_clusters.create_or_update(RESOURCE_GROUP, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
        BODY = {
          "tags": {
            "tier": "testing",
            "archv3": ""
          }
        }
        output = mgmt_client.open_shift_managed_clusters.update_tags(RESOURCE_GROUP, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
        BODY = {}
        output = mgmt_client.open_shift_managed_clusters.delete(RESOURCE_GROUP, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()