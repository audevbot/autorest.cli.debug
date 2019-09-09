# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimgmtScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_apimgmt')
    def test_apimgmt(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

# create_or_update -- create
        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myNode" --location "westus" --availability-zone-id "az1" --nodes-count "1" --placement-group-id "n1" --purchase-id "56acbd46-3d36-4bbf-9b08-57c30fdf6932" --sku-name "VMware_CloudSimple_CS28"', checks=[
        ])

        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myNode"', checks=[
        ])

        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

# create_or_update -- update
        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myNode" --location "westus" --availability-zone-id "az1" --nodes-count "1" --placement-group-id "n1" --purchase-id "56acbd46-3d36-4bbf-9b08-57c30fdf6932" --sku-name "VMware_CloudSimple_CS28"', checks=[
        ])

        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myNode"', checks=[
        ])

        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

# delete -- delete
        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myNode"', checks=[
        ])

# create_or_update -- create
        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --name "myService" --location "westus" --gateway-subnet "10.0.0.0"', checks=[
        ])

        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

# create_or_update -- update
        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --name "myService" --location "westus" --gateway-subnet "10.0.0.0"', checks=[
        ])

        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

# delete -- delete
        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myService"', checks=[
        ])

# create_or_update -- create
        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myVirtualMachine" --location "westus2" --amount-of-ram "4096" --guest-os "Other (32-bit)" --guest-ostype "other" --number-of-cores "2" --private-cloud-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}" --template-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}/virtualMachineTemplates/{{ virtual_machine_template_name }}"', checks=[
        ])

        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --name "myVirtualMachine"', checks=[
        ])

        self.cmd('vmwarecs create  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myVirtualMachine"', checks=[
        ])

# create_or_update -- update
        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myVirtualMachine" --location "westus2" --amount-of-ram "4096" --guest-os "Other (32-bit)" --guest-ostype "other" --number-of-cores "2" --private-cloud-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}" --template-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}/virtualMachineTemplates/{{ virtual_machine_template_name }}"', checks=[
        ])

        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --name "myVirtualMachine"', checks=[
        ])

        self.cmd('vmwarecs update  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myVirtualMachine"', checks=[
        ])

# delete -- delete
        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myVirtualMachine"', checks=[
        ])

        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --name "myVirtualMachine"', checks=[
        ])

        self.cmd('vmwarecs delete  --resource-group "myResourceGroup" --referer "https://management.azure.com/" --name "myVirtualMachine"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('vmwarecs list  --resource-group "myResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myVirtualMachine"', checks=[
        ])

        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myVirtualMachine"', checks=[
        ])

        self.cmd('vmwarecs show  --resource-group "myResourceGroup" --name "myVirtualMachine"', checks=[
        ])
