# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['vmwarecs'] = """
    type: group
    short-summary: Commands to manage dedicated cloud node.
"""

helps['vmwarecs create'] = """
    type: command
    short-summary: create dedicated cloud node.
    examples:
      - name: CreateDedicatedCloudNode
        text: |-
               az vmwarecs create --resource-group "myResourceGroup" --referer \\
               "https://management.azure.com/" --name "myNode" --location "westus" \\
               --availability-zone-id "az1" --nodes-count "1" --placement-group-id "n1" --purchase-id \\
               "56acbd46-3d36-4bbf-9b08-57c30fdf6932" --sku-name "VMware_CloudSimple_CS28"
"""

helps['vmwarecs update'] = """
    type: command
    short-summary: update dedicated cloud node.
    examples:
      - name: PatchDedicatedCloudNode
        text: |-
               az vmwarecs update --resource-group "myResourceGroup" --referer \\
               "https://management.azure.com/" --name "myNode"
"""

helps['vmwarecs delete'] = """
    type: command
    short-summary: delete dedicated cloud node.
    examples:
      - name: DeleteDedicatedCloudNode
        text: |-
               az vmwarecs delete --resource-group "myResourceGroup" --name "myNode"
"""

helps['vmwarecs list'] = """
    type: command
    short-summary: list dedicated cloud node.
"""

helps['vmwarecs show'] = """
    type: command
    short-summary: show dedicated cloud node.
"""

helps['vmwarecs'] = """
    type: group
    short-summary: Commands to manage dedicated cloud service.
"""

helps['vmwarecs create'] = """
    type: command
    short-summary: create dedicated cloud service.
    examples:
      - name: CreateDedicatedCloudService
        text: |-
               az vmwarecs create --resource-group "myResourceGroup" --name "myService" --location \\
               "westus" --gateway-subnet "10.0.0.0"
"""

helps['vmwarecs update'] = """
    type: command
    short-summary: update dedicated cloud service.
    examples:
      - name: PatchDedicatedService
        text: |-
               az vmwarecs update --resource-group "myResourceGroup" --name "myService"
"""

helps['vmwarecs delete'] = """
    type: command
    short-summary: delete dedicated cloud service.
    examples:
      - name: DeleteDedicatedCloudService
        text: |-
               az vmwarecs delete --resource-group "myResourceGroup" --name "myService"
"""

helps['vmwarecs list'] = """
    type: command
    short-summary: list dedicated cloud service.
"""

helps['vmwarecs show'] = """
    type: command
    short-summary: show dedicated cloud service.
"""

helps['vmwarecs'] = """
    type: group
    short-summary: Commands to manage virtual machine.
"""

helps['vmwarecs create'] = """
    type: command
    short-summary: create virtual machine.
    examples:
      - name: CreateVirtualMachine
        text: |-
               az vmwarecs create --resource-group "myResourceGroup" --referer \\
               "https://management.azure.com/" --name "myVirtualMachine" --location "westus2" \\
               --amount-of-ram "4096" --guest-os "Other (32-bit)" --guest-ostype "other" \\
               --number-of-cores "2" --private-cloud-id "/subscriptions/{{ subscription_id }}/providers/M
               icrosoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_na
               me }}" --template-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloud
               Simple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}/virtualMachine
               Templates/{{ virtual_machine_template_name }}"
"""

helps['vmwarecs update'] = """
    type: command
    short-summary: update virtual machine.
    examples:
      - name: PatchVirtualMachine
        text: |-
               az vmwarecs update --resource-group "myResourceGroup" --name "myVirtualMachine"
"""

helps['vmwarecs delete'] = """
    type: command
    short-summary: delete virtual machine.
    examples:
      - name: DeleteVirtualMachine
        text: |-
               az vmwarecs delete --resource-group "myResourceGroup" --referer \\
               "https://management.azure.com/" --name "myVirtualMachine"
"""

helps['vmwarecs list'] = """
    type: command
    short-summary: list virtual machine.
"""

helps['vmwarecs show'] = """
    type: command
    short-summary: show virtual machine.
"""
