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

        # vmwarecloudsimple_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.VMwareCloudSimple/operations?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudnodes_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudnodes_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudnodes_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudnodes_put
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

        # vmwarecloudsimple_dedicatedcloudnodes_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudnodes_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{DEDICATED_CLOUD_NODE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudservices_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudservices_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudservices_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudservices_put
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

        # vmwarecloudsimple_dedicatedcloudservices_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_dedicatedcloudservices_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{DEDICATED_CLOUD_SERVICE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_availabilities_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/availabilities?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_operationresults_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/operationResults/{OPERATION_RESULT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_operationresults_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/operationResults/{OPERATION_RESULT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_resourcepools_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/resourcePools?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_resourcepools_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/resourcePools/{RESOURCE_POOL_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_virtualmachinetemplates_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualMachineTemplates?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_virtualmachinetemplates_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualMachineTemplates/{VIRTUAL_MACHINE_TEMPLATE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_virtualnetworks_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualNetworks?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_privateclouds_virtualnetworks_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/privateClouds/{PRIVATE_CLOUD_NAME}/virtualNetworks/{VIRTUAL_NETWORK_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_locations_usages_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/locations/{LOCATION_NAME}/usages?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.VMwareCloudSimple/virtualMachines?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_put
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

        # vmwarecloudsimple_virtualmachines_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_start_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}/start?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_stop_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}/stop?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # vmwarecloudsimple_virtualmachines_stop_post_1
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{VIRTUAL_MACHINE_NAME}/stop?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])