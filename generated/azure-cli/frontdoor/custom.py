# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_frontdoor(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.front_doors.create()


def delete_frontdoor(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.front_doors.delete()


def list_frontdoor(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.front_doors.list()


def show_frontdoor(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.front_doors.show()


def show_frontdoor(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.front_doors.show()


def list_frontdoor(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.front_doors.list()


def create_frontdoor_routingrule(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.routing_rules.create()


def delete_frontdoor_routingrule(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.routing_rules.delete()


def list_frontdoor_routingrule(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.routing_rules.list()


def show_frontdoor_routingrule(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.routing_rules.show()


def show_frontdoor_routingrule(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.routing_rules.show()


def list_frontdoor_routingrule(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.routing_rules.list()


def create_frontdoor_healthprobesetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.health_probe_settings.create()


def delete_frontdoor_healthprobesetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.health_probe_settings.delete()


def list_frontdoor_healthprobesetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.health_probe_settings.list()


def show_frontdoor_healthprobesetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.health_probe_settings.show()


def show_frontdoor_healthprobesetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.health_probe_settings.show()


def list_frontdoor_healthprobesetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.health_probe_settings.list()


def create_frontdoor_loadbalancingsetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.load_balancing_settings.create()


def delete_frontdoor_loadbalancingsetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.load_balancing_settings.delete()


def list_frontdoor_loadbalancingsetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.load_balancing_settings.list()


def show_frontdoor_loadbalancingsetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.load_balancing_settings.show()


def show_frontdoor_loadbalancingsetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.load_balancing_settings.show()


def list_frontdoor_loadbalancingsetting(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.load_balancing_settings.list()


def create_frontdoor_backendpool(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend_pools.create()


def delete_frontdoor_backendpool(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend_pools.delete()


def list_frontdoor_backendpool(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend_pools.list()


def show_frontdoor_backendpool(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend_pools.show()


def show_frontdoor_backendpool(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend_pools.show()


def list_frontdoor_backendpool(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.backend_pools.list()


def create_frontdoor_frontendendpoint(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.frontend_endpoints.create()


def delete_frontdoor_frontendendpoint(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.frontend_endpoints.delete()


def list_frontdoor_frontendendpoint(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.frontend_endpoints.list()


def show_frontdoor_frontendendpoint(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.frontend_endpoints.show()


def show_frontdoor_frontendendpoint(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.frontend_endpoints.show()


def list_frontdoor_frontendendpoint(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.frontend_endpoints.list()