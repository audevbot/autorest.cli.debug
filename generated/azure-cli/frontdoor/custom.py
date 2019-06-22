# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_frontdoor(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None,
                     properties=None,
                     friendly_name=None,
                     routing_rules=None,
                     load_balancing_settings=None,
                     health_probe_settings=None,
                     backend_pools=None,
                     frontend_endpoints=None,
                     backend_pools_settings=None,
                     enabled_state=None,
                     resource_state=None,
                     provisioning_state=None,
                     cname=None,
                     id=None,
                     type=None):
    return client.front_doors.create(resource_group, name, frontDoorParameters)


def delete_frontdoor(cmd, client,
                     resource_group,
                     name):
    return client.front_doors.delete(resource_group, name)


def list_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.list(resource_group, name)


def show_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.show(resource_group, name)


def show_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.show(resource_group, name)


def list_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.list(resource_group, name)


def create_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name,
                                 id=None,
                                 properties=None,
                                 frontend_endpoints=None,
                                 accepted_protocols=None,
                                 patterns_to_match=None,
                                 enabled_state=None,
                                 route_configuration=None,
                                 resource_state=None,
                                 type=None):
    return client.routing_rules.create(resource_group, front_door_name, name, routingRuleParameters)


def delete_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    return client.routing_rules.delete(resource_group, front_door_name, name)


def list_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.list(resource_group, front_door_name, name)


def show_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.show(resource_group, front_door_name, name)


def show_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.show(resource_group, front_door_name, name)


def list_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.list(resource_group, front_door_name, name)


def create_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name,
                                        id=None,
                                        properties=None,
                                        path=None,
                                        protocol=None,
                                        interval_in_seconds=None,
                                        resource_state=None,
                                        type=None):
    return client.health_probe_settings.create(resource_group, front_door_name, name, healthProbeSettingsParameters)


def delete_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.health_probe_settings.delete(resource_group, front_door_name, name)


def list_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.list(resource_group, front_door_name, name)


def show_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.show(resource_group, front_door_name, name)


def show_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.show(resource_group, front_door_name, name)


def list_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.list(resource_group, front_door_name, name)


def create_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name,
                                          id=None,
                                          properties=None,
                                          sample_size=None,
                                          successful_samples_required=None,
                                          additional_latency_milliseconds=None,
                                          resource_state=None,
                                          type=None):
    return client.load_balancing_settings.create(resource_group, front_door_name, name, loadBalancingSettingsParameters)


def delete_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name):
    return client.load_balancing_settings.delete(resource_group, front_door_name, name)


def list_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.list(resource_group, front_door_name, name)


def show_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.show(resource_group, front_door_name, name)


def show_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.show(resource_group, front_door_name, name)


def list_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.list(resource_group, front_door_name, name)


def create_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name,
                                 id=None,
                                 properties=None,
                                 backends=None,
                                 load_balancing_settings=None,
                                 health_probe_settings=None,
                                 resource_state=None,
                                 type=None):
    return client.backend_pools.create(resource_group, front_door_name, name, backendPoolParameters)


def delete_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    return client.backend_pools.delete(resource_group, front_door_name, name)


def list_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.list(resource_group, front_door_name, name)


def show_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.show(resource_group, front_door_name, name)


def show_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.show(resource_group, front_door_name, name)


def list_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.list(resource_group, front_door_name, name)


def create_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name,
                                      id=None,
                                      properties=None,
                                      host_name=None,
                                      session_affinity_enabled_state=None,
                                      session_affinity_ttl_seconds=None,
                                      web_application_firewall_policy_link=None,
                                      resource_state=None,
                                      custom_https_provisioning_state=None,
                                      custom_https_provisioning_substate=None,
                                      custom_https_configuration=None,
                                      type=None):
    return client.frontend_endpoints.create(resource_group, front_door_name, name, frontendEndpointParameters)


def delete_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.frontend_endpoints.delete(resource_group, front_door_name, name)


def list_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.list(resource_group, front_door_name, name)


def show_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.show(resource_group, front_door_name, name)


def show_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.show(resource_group, front_door_name, name)


def list_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.list(resource_group, front_door_name, name)