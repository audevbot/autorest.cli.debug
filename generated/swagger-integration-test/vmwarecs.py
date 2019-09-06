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

        # ListOperations
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.VMwareCloudSimple/operations?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListDedicatedCloudNodes
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListRGDedicatedCloudNodes
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetDedicatedCloudNode
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # CreateDedicatedCloudNode
        body = (
                 '{'
                 '  "location": "westus",'
                 '  "properties": {'
                 '    "skuDescription": {'
                 '      "id": "general",'
                 '      "name": "CS28-Node"'
                 '    },'
                 '    "placementGroupId": "n1",'
                 '    "availabilityZoneId": "az1",'
                 '    "nodesCount": "1",'
                 '    "purchaseId": "56acbd46-3d36-4bbf-9b08-57c30fdf6932"'
                 '  },'
                 '  "sku": {'
                 '    "name": "VMware_CloudSimple_CS28"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # DeleteDedicatedCloudNode
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # PatchDedicatedCloudNode
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListDedicatedCloudServices
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListRGDedicatedCloudServices
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetDedicatedCloudService
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # CreateDedicatedCloudService
        body = (
                 '{'
                 '  "location": "westus",'
                 '  "properties": {'
                 '    "gatewaySubnet": "10.0.0.0"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # DeleteDedicatedCloudService
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # PatchDedicatedService
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListAvailabilities
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/availabilities?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetFailedOperationResult
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/operationResults/{OPERATION_RESULT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetOperationResult
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/operationResults/{OPERATION_RESULT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetPrivateCloud
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListPrivateCloudInLocation
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListResourcePools
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/resourcePools?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetResourcePool
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/resourcePools/{RESOURCE_POOL_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListVirtualMachineTemplates
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualMachineTemplates?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetVirtualMachineTemplate
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualMachineTemplates/{VIRTUAL_MACHINE_TEMPLATE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListVirtualNetworks
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualNetworks?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetVirtualNetwork
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualNetworks/{VIRTUAL_NETWORK_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListUsages
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/usages?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListVirtualMachines
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/virtualMachines?api-version=2019-04-01 '
                 , checks=[
                          ])

        # ListRGVirtualMachines
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines?api-version=2019-04-01 '
                 , checks=[
                          ])

        # GetVirtualMachine
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # CreateVirtualMachine
        body = (
                 '{'
                 '  "location": "westus2",'
                 '  "properties": {'
                 '    "privateCloudId": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "",'
                 '    "templateId": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualMachineTemplates/" + VIRTUAL_MACHINE_TEMPLATE_NAME + "",'
                 '    "numberOfCores": "2",'
                 '    "amountOfRam": "4096",'
                 '    "disks": ['
                 '      {'
                 '        "controllerId": "1000",'
                 '        "independenceMode": "persistent",'
                 '        "totalSize": "10485760",'
                 '        "virtualDiskId": "2000"'
                 '      }'
                 '    ],'
                 '    "resourcePool": {'
                 '      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/resourcePools/" + RESOURCE_POOL_NAME + ""'
                 '    },'
                 '    "guestOS": "Other (32-bit)",'
                 '    "guestOSType": "other",'
                 '    "nics": ['
                 '      {'
                 '        "network": {'
                 '          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualNetworks/" + VIRTUAL_NETWORK_NAME + ""'
                 '        },'
                 '        "nicType": "E1000",'
                 '        "powerOnBoot": True,'
                 '        "virtualNicId": "4000"'
                 '      }'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # DeleteVirtualMachine
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # PatchVirtualMachine
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # StartVirtualMachine
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}/start?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # StopInBodyVirtualMachine
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}/stop?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # StopInQueryVirtualMachine
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}/stop?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])