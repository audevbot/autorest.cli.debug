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
    body = {}
    body['location'] = location  # str
    body['availability_zone_id'] = availability_zone_id  # str
    body['nodes_count'] = nodes_count  # number
    body['placement_group_id'] = placement_group_id  # str
    body['purchase_id'] = purchase_id  # unknown-primary[uuid]
    body['sku_description'] = json.loads(sku_description) if isinstance(sku_description, str) else sku_description
    body.setdefault('sku', {})['capacity'] = sku_capacity  # str
    body.setdefault('sku', {})['family'] = sku_family  # str
    body.setdefault('sku', {})['name'] = sku_name  # str
    body.setdefault('sku', {})['tier'] = sku_tier  # str
    body['tags'] = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, referer=referer, dedicated_cloud_node_name=name, dedicated_cloud_node_request=body)


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
    body = client.get(resource_group_name=resource_group, dedicated_cloud_node_name=name).as_dict()
    body.location = location  # str
    body.availability_zone_id = availability_zone_id  # str
    body.nodes_count = nodes_count  # number
    body.placement_group_id = placement_group_id  # str
    body.purchase_id = purchase_id  # unknown-primary[uuid]
    body.sku_description = json.loads(sku_description) if isinstance(sku_description, str) else sku_description
    body.sku.capacity = sku_capacity  # str
    body.sku.family = sku_family  # str
    body.sku.name = sku_name  # str
    body.sku.tier = sku_tier  # str
    body.tags = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, referer=referer, dedicated_cloud_node_name=name, dedicated_cloud_node_request=body)


def list_vmwarecs(cmd, client,
                  resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_vmwarecs(cmd, client,
                    resource_group,
                    name,
                    location,
                    gateway_subnet,
                    nodes=None,
                    service_url=None,
                    tags=None):
    body = {}
    body['location'] = location  # str
    body['gateway_subnet'] = gateway_subnet  # str
    body['nodes'] = nodes  # number
    body['service_url'] = service_url  # str
    body['tags'] = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, dedicated_cloud_service_name=name, dedicated_cloud_service_request=body)


def update_vmwarecs(cmd, client, body,
                    resource_group,
                    name,
                    location,
                    gateway_subnet,
                    nodes=None,
                    service_url=None,
                    tags=None):
    body = client.get(resource_group_name=resource_group, dedicated_cloud_service_name=name).as_dict()
    body.location = location  # str
    body.gateway_subnet = gateway_subnet  # str
    body.nodes = nodes  # number
    body.service_url = service_url  # str
    body.tags = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, dedicated_cloud_service_name=name, dedicated_cloud_service_request=body)


def list_vmwarecs(cmd, client,
                  resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_vmwarecs(cmd, client,
                    resource_group,
                    name,
                    location,
                    amount_of_ram,
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
    body = {}
    body['location'] = location  # str
    body['amount_of_ram'] = amount_of_ram  # number
    body['disks'] = json.loads(disks) if isinstance(disks, str) else disks
    body['expose_to_guest_vm'] = expose_to_guest_vm  # boolean
    body['nics'] = json.loads(nics) if isinstance(nics, str) else nics
    body['number_of_cores'] = number_of_cores  # number
    body['password'] = password  # str
    body['private_cloud_id'] = private_cloud_id  # str
    body['resource_pool'] = json.loads(resource_pool) if isinstance(resource_pool, str) else resource_pool
    body['template_id'] = template_id  # str
    body['username'] = username  # str
    body['v_sphere_networks'] = json.loads(v_sphere_networks) if isinstance(v_sphere_networks, str) else v_sphere_networks
    body['tags'] = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, referer=referer, virtual_machine_name=name, virtual_machine_request=body)


def update_vmwarecs(cmd, client, body,
                    resource_group,
                    name,
                    location,
                    amount_of_ram,
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
    body = client.get(resource_group_name=resource_group, virtual_machine_name=name).as_dict()
    body.location = location  # str
    body.amount_of_ram = amount_of_ram  # number
    body.disks = json.loads(disks) if isinstance(disks, str) else disks
    body.expose_to_guest_vm = expose_to_guest_vm  # boolean
    body.nics = json.loads(nics) if isinstance(nics, str) else nics
    body.number_of_cores = number_of_cores  # number
    body.password = password  # str
    body.private_cloud_id = private_cloud_id  # str
    body.resource_pool = json.loads(resource_pool) if isinstance(resource_pool, str) else resource_pool
    body.template_id = template_id  # str
    body.username = username  # str
    body.v_sphere_networks = json.loads(v_sphere_networks) if isinstance(v_sphere_networks, str) else v_sphere_networks
    body.tags = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, referer=referer, virtual_machine_name=name, virtual_machine_request=body)


def list_vmwarecs(cmd, client,
                  resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()
