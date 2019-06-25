# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_frontdoor
def create_frontdoor(cmd, client,
                     resource_group,
                     name):
    body={}
    return client.front_doors.create_or_update(resource_group_name=resource_group, front_door_name=name)

# module equivalent: azure_rm_frontdoor
def update_frontdoor(cmd, client,
                     resource_group,
                     name):
    body={}
    return client.front_doors.create_or_update(resource_group_name=resource_group, front_door_name=name)

# module equivalent: azure_rm_frontdoor
def delete_frontdoor(cmd, client,
                     resource_group,
                     name):
    return client.front_doors.delete(resource_group_name=resource_group, front_door_name=name)

# module equivalent: azure_rm_frontdoor
def list_frontdoor(cmd, client,
                   resource_group):
    if resource_group is not None:
        return client.front_doors.list_by_resource_group(resource_group_name=resource_group)
    else:
        return client.front_doors.list()

# module equivalent: azure_rm_frontdoor
def show_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.get(resource_group_name=resource_group, front_door_name=name)

# module equivalent: azure_rm_frontdoorroutingrule
def create_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    body={}
    return client.routing_rules.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, routing_rule_name=name)

# module equivalent: azure_rm_frontdoorroutingrule
def update_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    body={}
    return client.routing_rules.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, routing_rule_name=name)

# module equivalent: azure_rm_frontdoorroutingrule
def delete_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    return client.routing_rules.delete(resource_group_name=resource_group, front_door_name=front_door_name, routing_rule_name=name)

# module equivalent: azure_rm_frontdoorroutingrule
def list_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name):
    return client.routing_rules.list_by_front_door(resource_group_name=resource_group, front_door_name=front_door_name)

# module equivalent: azure_rm_frontdoorroutingrule
def show_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.get(resource_group_name=resource_group, front_door_name=front_door_name, routing_rule_name=name)

# module equivalent: azure_rm_frontdoorhealthprobesetting
def create_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    body={}
    return client.health_probe_settings.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, health_probe_settings_name=name)

# module equivalent: azure_rm_frontdoorhealthprobesetting
def update_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    body={}
    return client.health_probe_settings.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, health_probe_settings_name=name)

# module equivalent: azure_rm_frontdoorhealthprobesetting
def delete_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.health_probe_settings.delete(resource_group_name=resource_group, front_door_name=front_door_name, health_probe_settings_name=name)

# module equivalent: azure_rm_frontdoorhealthprobesetting
def list_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name):
    return client.health_probe_settings.list_by_front_door(resource_group_name=resource_group, front_door_name=front_door_name)

# module equivalent: azure_rm_frontdoorhealthprobesetting
def show_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.get(resource_group_name=resource_group, front_door_name=front_door_name, health_probe_settings_name=name)

# module equivalent: azure_rm_frontdoorloadbalancingsetting
def create_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name):
    body={}
    return client.load_balancing_settings.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, load_balancing_settings_name=name)

# module equivalent: azure_rm_frontdoorloadbalancingsetting
def update_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name):
    body={}
    return client.load_balancing_settings.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, load_balancing_settings_name=name)

# module equivalent: azure_rm_frontdoorloadbalancingsetting
def delete_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name):
    return client.load_balancing_settings.delete(resource_group_name=resource_group, front_door_name=front_door_name, load_balancing_settings_name=name)

# module equivalent: azure_rm_frontdoorloadbalancingsetting
def list_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name):
    return client.load_balancing_settings.list_by_front_door(resource_group_name=resource_group, front_door_name=front_door_name)

# module equivalent: azure_rm_frontdoorloadbalancingsetting
def show_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.get(resource_group_name=resource_group, front_door_name=front_door_name, load_balancing_settings_name=name)

# module equivalent: azure_rm_frontdoorbackendpool
def create_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    body={}
    return client.backend_pools.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, backend_pool_name=name)

# module equivalent: azure_rm_frontdoorbackendpool
def update_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    body={}
    return client.backend_pools.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, backend_pool_name=name)

# module equivalent: azure_rm_frontdoorbackendpool
def delete_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    return client.backend_pools.delete(resource_group_name=resource_group, front_door_name=front_door_name, backend_pool_name=name)

# module equivalent: azure_rm_frontdoorbackendpool
def list_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name):
    return client.backend_pools.list_by_front_door(resource_group_name=resource_group, front_door_name=front_door_name)

# module equivalent: azure_rm_frontdoorbackendpool
def show_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.get(resource_group_name=resource_group, front_door_name=front_door_name, backend_pool_name=name)

# module equivalent: azure_rm_frontdoorfrontendendpoint
def create_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    body={}
    return client.frontend_endpoints.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, frontend_endpoint_name=name)

# module equivalent: azure_rm_frontdoorfrontendendpoint
def update_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    body={}
    return client.frontend_endpoints.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, frontend_endpoint_name=name)

# module equivalent: azure_rm_frontdoorfrontendendpoint
def delete_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.frontend_endpoints.delete(resource_group_name=resource_group, front_door_name=front_door_name, frontend_endpoint_name=name)

# module equivalent: azure_rm_frontdoorfrontendendpoint
def list_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name):
    return client.frontend_endpoints.list_by_front_door(resource_group_name=resource_group, front_door_name=front_door_name)

# module equivalent: azure_rm_frontdoorfrontendendpoint
def show_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.get(resource_group_name=resource_group, front_door_name=front_door_name, frontend_endpoint_name=name)