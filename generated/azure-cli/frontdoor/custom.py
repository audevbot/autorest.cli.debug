# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_frontdoor
def create_frontdoor(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None,
                     friendly_name=None,
                     routing_rules=None,
                     load_balancing_settings=None,
                     health_probe_settings=None,
                     backend_pools=None,
                     frontend_endpoints=None,
                     backend_pools_settings=None,
                     enabled_state=None,
                     resource_state=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['friendly_name'] = friendly_name
    body['routing_rules'] = routing_rules
    body['load_balancing_settings'] = load_balancing_settings
    body['health_probe_settings'] = health_probe_settings
    body['backend_pools'] = backend_pools
    body['frontend_endpoints'] = frontend_endpoints
    body['backend_pools_settings'] = backend_pools_settings
    body['enabled_state'] = enabled_state
    body['resource_state'] = resource_state
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
                                 name,
                                 id=None,
                                 frontend_endpoints=None,
                                 accepted_protocols=None,
                                 patterns_to_match=None,
                                 enabled_state=None,
                                 resource_state=None,
                                 name=None):
    body={}
    body['id'] = id
    body['frontend_endpoints'] = frontend_endpoints
    body['accepted_protocols'] = accepted_protocols
    body['patterns_to_match'] = patterns_to_match
    body['enabled_state'] = enabled_state
    body['resource_state'] = resource_state
    body['name'] = name
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
                                        name,
                                        id=None,
                                        path=None,
                                        protocol=None,
                                        interval_in_seconds=None,
                                        resource_state=None,
                                        name=None):
    body={}
    body['id'] = id
    body['path'] = path
    body['protocol'] = protocol
    body['interval_in_seconds'] = interval_in_seconds
    body['resource_state'] = resource_state
    body['name'] = name
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
                                          name,
                                          id=None,
                                          sample_size=None,
                                          successful_samples_required=None,
                                          additional_latency_milliseconds=None,
                                          resource_state=None,
                                          name=None):
    body={}
    body['id'] = id
    body['sample_size'] = sample_size
    body['successful_samples_required'] = successful_samples_required
    body['additional_latency_milliseconds'] = additional_latency_milliseconds
    body['resource_state'] = resource_state
    body['name'] = name
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
                                 name,
                                 id=None,
                                 backends=None,
                                 load_balancing_settings=None,
                                 health_probe_settings=None,
                                 resource_state=None,
                                 name=None):
    body={}
    body['id'] = id
    body['backends'] = backends
    body['load_balancing_settings'] = load_balancing_settings
    body['health_probe_settings'] = health_probe_settings
    body['resource_state'] = resource_state
    body['name'] = name
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
                                      name,
                                      id=None,
                                      host_name=None,
                                      session_affinity_enabled_state=None,
                                      session_affinity_ttl_seconds=None,
                                      web_application_firewall_policy_link=None,
                                      resource_state=None,
                                      name=None):
    body={}
    body['id'] = id
    body['host_name'] = host_name
    body['session_affinity_enabled_state'] = session_affinity_enabled_state
    body['session_affinity_ttl_seconds'] = session_affinity_ttl_seconds
    body['web_application_firewall_policy_link'] = web_application_firewall_policy_link
    body['resource_state'] = resource_state
    body['name'] = name
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