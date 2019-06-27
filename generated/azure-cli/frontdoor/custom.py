# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import json

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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"539","$type":"DictionaryType","valueType":{"$id":"540","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"541","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"542","fixed":false},"deprecated":false}]
    body['friendly_name'] = friendly_name # str
    body['routing_rules'] = json.loads(routing_rules) if isinstance(routing_rules, str) else routing_rules
    body['load_balancing_settings'] = json.loads(load_balancing_settings) if isinstance(load_balancing_settings, str) else load_balancing_settings
    body['health_probe_settings'] = json.loads(health_probe_settings) if isinstance(health_probe_settings, str) else health_probe_settings
    body['backend_pools'] = json.loads(backend_pools) if isinstance(backend_pools, str) else backend_pools
    body['frontend_endpoints'] = json.loads(frontend_endpoints) if isinstance(frontend_endpoints, str) else frontend_endpoints
    body['backend_pools_settings'] = json.loads(backend_pools_settings) if isinstance(backend_pools_settings, str) else backend_pools_settings
    body['enabled_state'] = enabled_state # str
    body['resource_state'] = resource_state # str
    return client.front_doors.create_or_update(resource_group_name=resource_group, front_door_name=name)

# module equivalent: azure_rm_frontdoor
def update_frontdoor(cmd, client,
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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"539","$type":"DictionaryType","valueType":{"$id":"540","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"541","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"542","fixed":false},"deprecated":false}]
    body['friendly_name'] = friendly_name # str
    body['routing_rules'] = json.loads(routing_rules) if isinstance(routing_rules, str) else routing_rules
    body['load_balancing_settings'] = json.loads(load_balancing_settings) if isinstance(load_balancing_settings, str) else load_balancing_settings
    body['health_probe_settings'] = json.loads(health_probe_settings) if isinstance(health_probe_settings, str) else health_probe_settings
    body['backend_pools'] = json.loads(backend_pools) if isinstance(backend_pools, str) else backend_pools
    body['frontend_endpoints'] = json.loads(frontend_endpoints) if isinstance(frontend_endpoints, str) else frontend_endpoints
    body['backend_pools_settings'] = json.loads(backend_pools_settings) if isinstance(backend_pools_settings, str) else backend_pools_settings
    body['enabled_state'] = enabled_state # str
    body['resource_state'] = resource_state # str
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
                                 resource_state=None):
    body={}
    body['id'] = id # str
    body['frontend_endpoints'] = json.loads(frontend_endpoints) if isinstance(frontend_endpoints, str) else frontend_endpoints
    body['accepted_protocols'] = json.loads(accepted_protocols) if isinstance(accepted_protocols, str) else accepted_protocols
    body['patterns_to_match'] = json.loads(patterns_to_match) if isinstance(patterns_to_match, str) else patterns_to_match
    body['enabled_state'] = enabled_state # str
    body['resource_state'] = resource_state # str
    return client.routing_rules.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, routing_rule_name=name)

# module equivalent: azure_rm_frontdoorroutingrule
def update_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name,
                                 id=None,
                                 frontend_endpoints=None,
                                 accepted_protocols=None,
                                 patterns_to_match=None,
                                 enabled_state=None,
                                 resource_state=None):
    body={}
    body['id'] = id # str
    body['frontend_endpoints'] = json.loads(frontend_endpoints) if isinstance(frontend_endpoints, str) else frontend_endpoints
    body['accepted_protocols'] = json.loads(accepted_protocols) if isinstance(accepted_protocols, str) else accepted_protocols
    body['patterns_to_match'] = json.loads(patterns_to_match) if isinstance(patterns_to_match, str) else patterns_to_match
    body['enabled_state'] = enabled_state # str
    body['resource_state'] = resource_state # str
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
                                        resource_state=None):
    body={}
    body['id'] = id # str
    body['path'] = path # str
    body['protocol'] = protocol # str
    body['interval_in_seconds'] = interval_in_seconds # number
    body['resource_state'] = resource_state # str
    return client.health_probe_settings.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, health_probe_settings_name=name)

# module equivalent: azure_rm_frontdoorhealthprobesetting
def update_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name,
                                        id=None,
                                        path=None,
                                        protocol=None,
                                        interval_in_seconds=None,
                                        resource_state=None):
    body={}
    body['id'] = id # str
    body['path'] = path # str
    body['protocol'] = protocol # str
    body['interval_in_seconds'] = interval_in_seconds # number
    body['resource_state'] = resource_state # str
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
                                          resource_state=None):
    body={}
    body['id'] = id # str
    body['sample_size'] = sample_size # number
    body['successful_samples_required'] = successful_samples_required # number
    body['additional_latency_milliseconds'] = additional_latency_milliseconds # number
    body['resource_state'] = resource_state # str
    return client.load_balancing_settings.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, load_balancing_settings_name=name)

# module equivalent: azure_rm_frontdoorloadbalancingsetting
def update_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name,
                                          id=None,
                                          sample_size=None,
                                          successful_samples_required=None,
                                          additional_latency_milliseconds=None,
                                          resource_state=None):
    body={}
    body['id'] = id # str
    body['sample_size'] = sample_size # number
    body['successful_samples_required'] = successful_samples_required # number
    body['additional_latency_milliseconds'] = additional_latency_milliseconds # number
    body['resource_state'] = resource_state # str
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
                                 resource_state=None):
    body={}
    body['id'] = id # str
    body['backends'] = json.loads(backends) if isinstance(backends, str) else backends
    body['load_balancing_settings'] = json.loads(load_balancing_settings) if isinstance(load_balancing_settings, str) else load_balancing_settings
    body['health_probe_settings'] = json.loads(health_probe_settings) if isinstance(health_probe_settings, str) else health_probe_settings
    body['resource_state'] = resource_state # str
    return client.backend_pools.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, backend_pool_name=name)

# module equivalent: azure_rm_frontdoorbackendpool
def update_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name,
                                 id=None,
                                 backends=None,
                                 load_balancing_settings=None,
                                 health_probe_settings=None,
                                 resource_state=None):
    body={}
    body['id'] = id # str
    body['backends'] = json.loads(backends) if isinstance(backends, str) else backends
    body['load_balancing_settings'] = json.loads(load_balancing_settings) if isinstance(load_balancing_settings, str) else load_balancing_settings
    body['health_probe_settings'] = json.loads(health_probe_settings) if isinstance(health_probe_settings, str) else health_probe_settings
    body['resource_state'] = resource_state # str
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
                                      resource_state=None):
    body={}
    body['id'] = id # str
    body['host_name'] = host_name # str
    body['session_affinity_enabled_state'] = session_affinity_enabled_state # str
    body['session_affinity_ttl_seconds'] = session_affinity_ttl_seconds # number
    body['web_application_firewall_policy_link'] = json.loads(web_application_firewall_policy_link) if isinstance(web_application_firewall_policy_link, str) else web_application_firewall_policy_link
    body['resource_state'] = resource_state # str
    return client.frontend_endpoints.create_or_update(resource_group_name=resource_group, front_door_name=front_door_name, frontend_endpoint_name=name)

# module equivalent: azure_rm_frontdoorfrontendendpoint
def update_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name,
                                      id=None,
                                      host_name=None,
                                      session_affinity_enabled_state=None,
                                      session_affinity_ttl_seconds=None,
                                      web_application_firewall_policy_link=None,
                                      resource_state=None):
    body={}
    body['id'] = id # str
    body['host_name'] = host_name # str
    body['session_affinity_enabled_state'] = session_affinity_enabled_state # str
    body['session_affinity_ttl_seconds'] = session_affinity_ttl_seconds # number
    body['web_application_firewall_policy_link'] = json.loads(web_application_firewall_policy_link) if isinstance(web_application_firewall_policy_link, str) else web_application_firewall_policy_link
    body['resource_state'] = resource_state # str
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