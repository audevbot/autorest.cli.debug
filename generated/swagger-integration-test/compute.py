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

        # compute_disks_put
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

        # compute_disks_put_1
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

        # compute_disks_put_2
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

        # compute_disks_put_3
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

        # compute_disks_put_4
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

        # compute_disks_put_5
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

        # compute_disks_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{DISK_NAME}?api-version=2018-09-30 '
                 , checks=[
                          ])

        # compute_disks_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/disks?api-version=2018-09-30 '
                 , checks=[
                          ])

        # compute_disks_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Compute/disks?api-version=2018-09-30 '
                 , checks=[
                          ])

        # compute_snapshots_put
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

        # compute_snapshots_put_1
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

        # compute_snapshots_put_2
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

        # compute_snapshots_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots/{SNAPSHOT_NAME}?api-version=2018-09-30 '
                 , checks=[
                          ])

        # compute_snapshots_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Compute/snapshots?api-version=2018-09-30 '
                 , checks=[
                          ])

        # compute_snapshots_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Compute/snapshots?api-version=2018-09-30 '
                 , checks=[
                          ])