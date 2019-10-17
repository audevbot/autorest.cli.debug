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
        output = mgmt_client.operations.list(, BODY)
        BODY = {}
        output = mgmt_client.operations.get(LOCATION_NAME, OPERATION_RESULT_NAME, BODY)
        BODY = {}
        output = mgmt_client.operations.get(LOCATION_NAME, OPERATION_RESULT_NAME, BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_nodes.list_by_subscription(, BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_nodes.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_nodes.get(RESOURCE_GROUP, DEDICATED_CLOUD_NODE_NAME, BODY)
        BODY = {
          "location": "westus",
          "properties": {
            "sku_description": {
              "id": "general",
              "name": "CS28-Node"
            },
            "placement_group_id": "n1",
            "availability_zone_id": "az1",
            "nodes_count": "1",
            "purchase_id": "56acbd46-3d36-4bbf-9b08-57c30fdf6932"
          },
          "sku": {
            "name": "VMware_CloudSimple_CS28"
          }
        }
        output = mgmt_client.dedicated_cloud_nodes.create_or_update(RESOURCE_GROUP, DEDICATED_CLOUD_NODE_NAME, BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_nodes.delete(RESOURCE_GROUP, DEDICATED_CLOUD_NODE_NAME, BODY)
        BODY = {
          "tags": {
            "my_tag": "tagValue"
          }
        }
        output = mgmt_client.dedicated_cloud_nodes.update(RESOURCE_GROUP, DEDICATED_CLOUD_NODE_NAME, BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_services.list_by_subscription(, BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_services.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_services.get(RESOURCE_GROUP, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        BODY = {
          "location": "westus",
          "properties": {
            "gateway_subnet": "10.0.0.0"
          }
        }
        output = mgmt_client.dedicated_cloud_services.create_or_update(RESOURCE_GROUP, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.dedicated_cloud_services.delete(RESOURCE_GROUP, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        BODY = {
          "tags": {
            "my_tag": "tagValue"
          }
        }
        output = mgmt_client.dedicated_cloud_services.update(RESOURCE_GROUP, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.skus_availability.list(LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.private_clouds.list(LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.private_clouds.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, BODY)
        BODY = {}
        output = mgmt_client.resource_pools.list(LOCATION_NAME, PRIVATE_CLOUD_NAME, , BODY)
        BODY = {}
        output = mgmt_client.resource_pools.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, RESOURCE_POOL_NAME, BODY)
        BODY = {}
        output = mgmt_client.virtual_machine_templates.list(LOCATION_NAME, PRIVATE_CLOUD_NAME, , BODY)
        BODY = {}
        output = mgmt_client.virtual_machine_templates.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, VIRTUAL_MACHINE_TEMPLATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.virtual_networks.list(LOCATION_NAME, PRIVATE_CLOUD_NAME, , BODY)
        BODY = {}
        output = mgmt_client.virtual_networks.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, VIRTUAL_NETWORK_NAME, BODY)
        BODY = {}
        output = mgmt_client.usages.list(LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.list_by_subscription(, BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.get(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, BODY)
        BODY = {
          "location": "westus2",
          "properties": {
            "private_cloud_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "",
            "template_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualMachineTemplates/" + VIRTUAL_MACHINE_TEMPLATE_NAME + "",
            "number_of_cores": "2",
            "amount_of_ram": "4096",
            "disks": [
              {
                "controller_id": "1000",
                "independence_mode": "persistent",
                "total_size": "10485760",
                "virtual_disk_id": "2000"
              }
            ],
            "resource_pool": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/resourcePools/" + RESOURCE_POOL_NAME + ""
            },
            "nics": [
              {
                "network": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualNetworks/" + VIRTUAL_NETWORK_NAME + ""
                },
                "nic_type": "E1000",
                "power_on_boot": True,
                "virtual_nic_id": "4000"
              }
            ]
          }
        }
        output = mgmt_client.virtual_machines.create_or_update(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.delete(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, BODY)
        BODY = {
          "tags": {
            "my_tag": "tagValue"
          }
        }
        output = mgmt_client.virtual_machines.update(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.start(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.stop(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.virtual_machines.stop(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()