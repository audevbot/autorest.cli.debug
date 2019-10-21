# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.compute
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtDiskResourceProviderClientTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtDiskResourceProviderClientTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.compute.DiskResourceProviderClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_compute(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {
          "name": "myDisk",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Empty"
            },
            "disk_size_gb": "200"
          }
        }
        azure_operation_poller = self.mgmt_client.disks.create_or_update(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "myDisk",
          "location": "West US",
          "properties": {
            "os_type": "Windows",
            "creation_data": {
              "create_option": "FromImage",
              "image_reference": {
                "id": "/Subscriptions/{subscriptionId}/Providers/Microsoft.Compute/Locations/uswest/Publishers/Microsoft/ArtifactTypes/VMImage/Offers/{offer}"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.disks.create_or_update(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "myDisk2",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Copy",
              "source_resource_id": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDisk1"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.disks.create_or_update(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "myDisk",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Import",
              "source_uri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.disks.create_or_update(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "myDisk",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Import",
              "storage_account_id": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount",
              "source_uri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.disks.create_or_update(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "myDisk",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Copy",
              "source_resource_id": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.disks.create_or_update(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disks.get(resource_group.name, DISK_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disks.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disks.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "mySnapshot2",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Copy",
              "source_resource_id": "subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot1"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.snapshots.create_or_update(resource_group.name, SNAPSHOT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "mySnapshot1",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Import",
              "source_uri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.snapshots.create_or_update(resource_group.name, SNAPSHOT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "mySnapshot1",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Import",
              "storage_account_id": "subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount",
              "source_uri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.snapshots.create_or_update(resource_group.name, SNAPSHOT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.snapshots.get(resource_group.name, SNAPSHOT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.snapshots.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.snapshots.list(, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()