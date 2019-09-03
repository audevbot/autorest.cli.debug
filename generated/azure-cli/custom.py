# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

import json


# module equivalent: azure_rm_vmwarecloudsimplededicatedcloudnode
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{{ dedicated_cloud_node_name }}
def create_vmwarecs(cmd, client,
                    resource_group,
                    name,
                    location,
                    availability_zone_id,
                    nodes_count,
                    placement_group_id,
                    purchase_id,
                    sku_name,
                    referer=None,
                    sku_description=None,
                    sku_capacity=None,
                    sku_family=None,
                    sku_tier=None,
                    tags=None):
    return client.create_or_update(resource_group_name=resource_group, referer=referer, dedicated_cloud_node_name=name)


# module equivalent: azure_rm_vmwarecloudsimplededicatedcloudnode
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{{ dedicated_cloud_node_name }}
def update_vmwarecs(cmd, client, body,
                    resource_group,
                    name,
                    location,
                    availability_zone_id,
                    nodes_count,
                    placement_group_id,
                    purchase_id,
                    sku_name,
                    referer=None,
                    sku_description=None,
                    sku_capacity=None,
                    sku_family=None,
                    sku_tier=None,
                    tags=None):
    return client.create_or_update(resource_group_name=resource_group, referer=referer, dedicated_cloud_node_name=name)


# module equivalent: azure_rm_vmwarecloudsimplededicatedcloudnode
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{{ dedicated_cloud_node_name }}
def list_vmwarecs(cmd, client,
                  resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


# module equivalent: azure_rm_vmwarecloudsimplededicatedcloudservice
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{{ dedicated_cloud_service_name }}
def create_vmwarecs(cmd, client,
                    resource_group,
                    name,
                    location,
                    gateway_subnet,
                    nodes=None,
                    service_url=None,
                    tags=None):
    return client.create_or_update(resource_group_name=resource_group, dedicated_cloud_service_name=name)


# module equivalent: azure_rm_vmwarecloudsimplededicatedcloudservice
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{{ dedicated_cloud_service_name }}
def update_vmwarecs(cmd, client, body,
                    resource_group,
                    name,
                    location,
                    gateway_subnet,
                    nodes=None,
                    service_url=None,
                    tags=None):
    return client.create_or_update(resource_group_name=resource_group, dedicated_cloud_service_name=name)


# module equivalent: azure_rm_vmwarecloudsimplededicatedcloudservice
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{{ dedicated_cloud_service_name }}
def list_vmwarecs(cmd, client,
                  resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


# module equivalent: azure_rm_vmwarecloudsimplevirtualmachine
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{{ virtual_machine_name }}
def create_vmwarecs(cmd, client,
                    resource_group,
                    name,
                    location,
                    amount_of_ram,
                    guest_os,
                    guest_ostype,
                    number_of_cores,
                    private_cloud_id,
                    referer=None,
                    disks=None,
                    expose_to_guest_vm=None,
                    nics=None,
                    password=None,
                    resource_pool=None,
                    template_id=None,
                    username=None,
                    v_sphere_networks=None,
                    tags=None):
    return client.create_or_update(resource_group_name=resource_group, referer=referer, virtual_machine_name=name)


# module equivalent: azure_rm_vmwarecloudsimplevirtualmachine
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{{ virtual_machine_name }}
def update_vmwarecs(cmd, client, body,
                    resource_group,
                    name,
                    location,
                    amount_of_ram,
                    guest_os,
                    guest_ostype,
                    number_of_cores,
                    private_cloud_id,
                    referer=None,
                    disks=None,
                    expose_to_guest_vm=None,
                    nics=None,
                    password=None,
                    resource_pool=None,
                    template_id=None,
                    username=None,
                    v_sphere_networks=None,
                    tags=None):
    return client.create_or_update(resource_group_name=resource_group, referer=referer, virtual_machine_name=name)


# module equivalent: azure_rm_vmwarecloudsimplevirtualmachine
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{{ virtual_machine_name }}
def list_vmwarecs(cmd, client,
                  resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()
