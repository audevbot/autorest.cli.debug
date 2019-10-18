# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)


def load_arguments(self, _):

    with self.argument_context('vmwarecs create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('referer', id_part=None, help='referer url')
        c.argument('name', id_part=None, help='dedicated cloud node name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('availability_zone_id', id_part=None, help='Availability Zone id, e.g. "az1"')
        c.argument('nodes_count', id_part=None, help='count of nodes to create')
        c.argument('placement_group_id', id_part=None, help='Placement Group id, e.g. "n1"')
        c.argument('purchase_id', id_part=None, help='purchase id')
        c.argument('sku_description', id_part=None, help='Dedicated Cloud Nodes SKU\'s description')
        c.argument('sku_capacity', id_part=None, help='The capacity of the SKU')
        c.argument('sku_family', id_part=None, help='If the service has different generations of hardware, for the same SKU, then that can be captured here')
        c.argument('sku_name', id_part=None, help='The name of the SKU for VMWare CloudSimple Node')
        c.argument('sku_tier', id_part=None, help='The tier of the SKU')
        c.argument('tags', tags_type)

    with self.argument_context('vmwarecs update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('referer', id_part=None, help='referer url')
        c.argument('name', id_part=None, help='dedicated cloud node name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('availability_zone_id', id_part=None, help='Availability Zone id, e.g. "az1"')
        c.argument('nodes_count', id_part=None, help='count of nodes to create')
        c.argument('placement_group_id', id_part=None, help='Placement Group id, e.g. "n1"')
        c.argument('purchase_id', id_part=None, help='purchase id')
        c.argument('sku_description', id_part=None, help='Dedicated Cloud Nodes SKU\'s description')
        c.argument('sku_capacity', id_part=None, help='The capacity of the SKU')
        c.argument('sku_family', id_part=None, help='If the service has different generations of hardware, for the same SKU, then that can be captured here')
        c.argument('sku_name', id_part=None, help='The name of the SKU for VMWare CloudSimple Node')
        c.argument('sku_tier', id_part=None, help='The tier of the SKU')
        c.argument('tags', tags_type)

    with self.argument_context('vmwarecs delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='dedicated cloud node name')

    with self.argument_context('vmwarecs list') as c:
        c.argument('resource_group', resource_group_name_type)

    with self.argument_context('vmwarecs show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='dedicated cloud node name')

    with self.argument_context('vmwarecs create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='dedicated cloud Service name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('gateway_subnet', id_part=None, help='gateway Subnet for the account. It will collect the subnet address and always treat it as /28')
        c.argument('nodes', id_part=None, help='total nodes purchased')
        c.argument('service_url', id_part=None, help='link to a service management web portal')
        c.argument('tags', tags_type)

    with self.argument_context('vmwarecs update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='dedicated cloud Service name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('gateway_subnet', id_part=None, help='gateway Subnet for the account. It will collect the subnet address and always treat it as /28')
        c.argument('nodes', id_part=None, help='total nodes purchased')
        c.argument('service_url', id_part=None, help='link to a service management web portal')
        c.argument('tags', tags_type)

    with self.argument_context('vmwarecs delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='dedicated cloud Service name')

    with self.argument_context('vmwarecs list') as c:
        c.argument('resource_group', resource_group_name_type)

    with self.argument_context('vmwarecs show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='dedicated cloud Service name')

    with self.argument_context('vmwarecs create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('referer', id_part=None, help='referer url')
        c.argument('name', id_part=None, help='virtual machine name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('amount_of_ram', id_part=None, help='The amount of memory')
        c.argument('disks', id_part=None, help='The list of Virtual Disks')
        c.argument('expose_to_guest_vm', arg_type=get_three_state_flag(), id_part=None, help='Expose Guest OS or not')
        c.argument('nics', id_part=None, help='The list of Virtual NICs')
        c.argument('number_of_cores', id_part=None, help='The number of CPU cores')
        c.argument('password', id_part=None, help='Password for login')
        c.argument('private_cloud_id', id_part=None, help='Private Cloud Id')
        c.argument('resource_pool', id_part=None, help='Virtual Machines Resource Pool')
        c.argument('template_id', id_part=None, help='Virtual Machine Template Id')
        c.argument('username', id_part=None, help='Username for login')
        c.argument('v_sphere_networks', id_part=None, help='The list of Virtual VSphere Networks')
        c.argument('tags', tags_type)

    with self.argument_context('vmwarecs update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('referer', id_part=None, help='referer url')
        c.argument('name', id_part=None, help='virtual machine name')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('amount_of_ram', id_part=None, help='The amount of memory')
        c.argument('disks', id_part=None, help='The list of Virtual Disks')
        c.argument('expose_to_guest_vm', arg_type=get_three_state_flag(), id_part=None, help='Expose Guest OS or not')
        c.argument('nics', id_part=None, help='The list of Virtual NICs')
        c.argument('number_of_cores', id_part=None, help='The number of CPU cores')
        c.argument('password', id_part=None, help='Password for login')
        c.argument('private_cloud_id', id_part=None, help='Private Cloud Id')
        c.argument('resource_pool', id_part=None, help='Virtual Machines Resource Pool')
        c.argument('template_id', id_part=None, help='Virtual Machine Template Id')
        c.argument('username', id_part=None, help='Username for login')
        c.argument('v_sphere_networks', id_part=None, help='The list of Virtual VSphere Networks')
        c.argument('tags', tags_type)

    with self.argument_context('vmwarecs delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('referer', id_part=None, help='referer url')
        c.argument('name', id_part=None, help='virtual machine name')

    with self.argument_context('vmwarecs list') as c:
        c.argument('resource_group', resource_group_name_type)

    with self.argument_context('vmwarecs show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='virtual machine name')
