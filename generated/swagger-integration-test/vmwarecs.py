# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.vmwarecloudsimple
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtVMwareCloudSimpleTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtVMwareCloudSimpleTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.vmwarecloudsimple.VMwareCloudSimple
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_vmwarecs(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.operations.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.operations.get(LOCATION_NAME, OPERATION_RESULT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.operations.get(LOCATION_NAME, OPERATION_RESULT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_nodes.list_by_subscription(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_nodes.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_nodes.get(resource_group.name, DEDICATED_CLOUD_NODE_NAME, BODY)
        result_create = azure_operation_poller.result()
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
        azure_operation_poller = self.mgmt_client.dedicated_cloud_nodes.create_or_update(resource_group.name, DEDICATED_CLOUD_NODE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_nodes.delete(resource_group.name, DEDICATED_CLOUD_NODE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "my_tag": "tagValue"
          }
        }
        azure_operation_poller = self.mgmt_client.dedicated_cloud_nodes.update(resource_group.name, DEDICATED_CLOUD_NODE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_services.list_by_subscription(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_services.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_services.get(resource_group.name, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "westus",
          "properties": {
            "gateway_subnet": "10.0.0.0"
          }
        }
        azure_operation_poller = self.mgmt_client.dedicated_cloud_services.create_or_update(resource_group.name, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.dedicated_cloud_services.delete(resource_group.name, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "my_tag": "tagValue"
          }
        }
        azure_operation_poller = self.mgmt_client.dedicated_cloud_services.update(resource_group.name, DEDICATED_CLOUD_SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.skus_availability.list(LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.private_clouds.list(LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.private_clouds.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.resource_pools.list(LOCATION_NAME, PRIVATE_CLOUD_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.resource_pools.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, RESOURCE_POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machine_templates.list(LOCATION_NAME, PRIVATE_CLOUD_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machine_templates.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, VIRTUAL_MACHINE_TEMPLATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_networks.list(LOCATION_NAME, PRIVATE_CLOUD_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_networks.get(LOCATION_NAME, PRIVATE_CLOUD_NAME, VIRTUAL_NETWORK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.usages.list(LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.list_by_subscription(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.get(resource_group.name, VIRTUAL_MACHINE_NAME, BODY)
        result_create = azure_operation_poller.result()
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
        azure_operation_poller = self.mgmt_client.virtual_machines.create_or_update(resource_group.name, VIRTUAL_MACHINE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.delete(resource_group.name, VIRTUAL_MACHINE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "my_tag": "tagValue"
          }
        }
        azure_operation_poller = self.mgmt_client.virtual_machines.update(resource_group.name, VIRTUAL_MACHINE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.start(resource_group.name, VIRTUAL_MACHINE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.stop(resource_group.name, VIRTUAL_MACHINE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.virtual_machines.stop(resource_group.name, VIRTUAL_MACHINE_NAME, , BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()