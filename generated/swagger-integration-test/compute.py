# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import time
import mock
import unittest

from azure_devtools.scenario_tests.const import MOCKED_SUBSCRIPTION_ID
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, LiveScenarioTest, ResourceGroupPreparer, create_random_name, live_only, record_only
from azure.cli.core.util import get_file_json


class ResourceGroupScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_rg_scenario')
    def test_resource_group(self, resource_group):

        self.cmd('group create -n {rg} -l westus --tag a=b c', checks=[
            self.check('name', '{rg}'),
            self.check('tags', {'a': 'b', 'c': ''})
        ])

        self.kwargs['sub'] = self.get_subscription_id()
        self.kwargs['name'] = 'zimsxyzname'

        # Create an empty managed disk.
        body = (
                 '{'
                 '  "name": "myDisk",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Empty"'
                 '    },'
                 '    "diskSizeGB": "200"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a managed disk from a platform image.
        body = (
                 '{'
                 '  "name": "myDisk",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "osType": "Windows",'
                 '    "creationData": {'
                 '      "createOption": "FromImage",'
                 '      "imageReference": {'
                 '        "id": "/Subscriptions/{subscriptionId}/Providers/Microsoft.Compute/Locations/uswest/Publishers/Microsoft/ArtifactTypes/VMImage/Offers/{offer}"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a managed disk from an existing managed disk in the same or different subscription.
        body = (
                 '{'
                 '  "name": "myDisk2",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Copy",'
                 '      "sourceResourceId": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDisk1"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a managed disk by importing an unmanaged blob from the same subscription.
        body = (
                 '{'
                 '  "name": "myDisk",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Import",'
                 '      "sourceUri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a managed disk by importing an unmanaged blob from a different subscription.
        body = (
                 '{'
                 '  "name": "myDisk",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Import",'
                 '      "storageAccountId": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount",'
                 '      "sourceUri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a managed disk by copying a snapshot.
        body = (
                 '{'
                 '  "name": "myDisk",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Copy",'
                 '      "sourceResourceId": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Get information about a managed disk.
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 , checks=[
                          ])

        # List all managed disks in a resource group.
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks?api-version=2018-09-30 '
                 , checks=[
                          ])

        # List all managed disks in a subscription.
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Compute/disks?api-version=2018-09-30 '
                 , checks=[
                          ])

        # Create a snapshot from an existing snapshot in the same or a different subscription.
        body = (
                 '{'
                 '  "name": "mySnapshot2",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Copy",'
                 '      "sourceResourceId": "subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot1"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots/{SNAPSHOT_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a snapshot by importing an unmanaged blob from the same subscription.
        body = (
                 '{'
                 '  "name": "mySnapshot1",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Import",'
                 '      "sourceUri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots/{SNAPSHOT_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Create a snapshot by importing an unmanaged blob from a different subscription.
        body = (
                 '{'
                 '  "name": "mySnapshot1",'
                 '  "location": "West US",'
                 '  "properties": {'
                 '    "creationData": {'
                 '      "createOption": "Import",'
                 '      "storageAccountId": "subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount",'
                 '      "sourceUri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots/{SNAPSHOT_NAME}?api-version=2018-09-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Get information about a snapshot.
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots/{SNAPSHOT_NAME}?api-version=2018-09-30 '
                 , checks=[
                          ])

        # List all snapshots in a resource group.
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots?api-version=2018-09-30 '
                 , checks=[
                          ])

        # List all snapshots in a subscription.
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Compute/snapshots?api-version=2018-09-30 '
                 , checks=[
                          ])