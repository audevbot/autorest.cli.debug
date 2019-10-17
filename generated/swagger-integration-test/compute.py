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
          "name": "myDisk",
          "location": "West US",
          "properties": {
            "creation_data": {
              "create_option": "Empty"
            },
            "disk_size_gb": "200"
          }
        }
        output = mgmt_client.disks.create_or_update(RESOURCE_GROUP, DISK_NAME, BODY)
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
        output = mgmt_client.disks.create_or_update(RESOURCE_GROUP, DISK_NAME, BODY)
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
        output = mgmt_client.disks.create_or_update(RESOURCE_GROUP, DISK_NAME, BODY)
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
        output = mgmt_client.disks.create_or_update(RESOURCE_GROUP, DISK_NAME, BODY)
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
        output = mgmt_client.disks.create_or_update(RESOURCE_GROUP, DISK_NAME, BODY)
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
        output = mgmt_client.disks.create_or_update(RESOURCE_GROUP, DISK_NAME, BODY)
        BODY = {}
        output = mgmt_client.disks.get(RESOURCE_GROUP, DISK_NAME, BODY)
        BODY = {}
        output = mgmt_client.disks.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.disks.list(, BODY)
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
        output = mgmt_client.snapshots.create_or_update(RESOURCE_GROUP, SNAPSHOT_NAME, BODY)
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
        output = mgmt_client.snapshots.create_or_update(RESOURCE_GROUP, SNAPSHOT_NAME, BODY)
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
        output = mgmt_client.snapshots.create_or_update(RESOURCE_GROUP, SNAPSHOT_NAME, BODY)
        BODY = {}
        output = mgmt_client.snapshots.get(RESOURCE_GROUP, SNAPSHOT_NAME, BODY)
        BODY = {}
        output = mgmt_client.snapshots.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.snapshots.list(, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()