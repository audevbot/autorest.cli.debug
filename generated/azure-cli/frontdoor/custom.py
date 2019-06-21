# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_frontdoor(cmd, client,
                     resource_group,
                     name,
                     location,
                     tags,
                     properties,
                     friendly_name,
                     routing_rules,
                     load_balancing_settings,
                     health_probe_settings,
                     backend_pools,
                     frontend_endpoints,
                     backend_pools_settings,
                     enabled_state,
                     resource_state,
                     provisioning_state,
                     cname,
                     id,
                     type):
    return client.front_doors.create()


def delete_frontdoor(cmd, client,
                     resource_group,
                     name):
    return client.front_doors.delete()


def list_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.list()


def show_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.show()


def show_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.show()


def list_frontdoor(cmd, client,
                   resource_group,
                   name):
    return client.front_doors.list()


def create_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name,
                                 id,
                                 properties,
                                 frontend_endpoints,
                                 accepted_protocols,
                                 patterns_to_match,
                                 enabled_state,
                                 route_configuration,
                                 resource_state,
                                 type):
    return client.routing_rules.create()


def delete_frontdoor_routingrule(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    return client.routing_rules.delete()


def list_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.list()


def show_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.show()


def show_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.show()


def list_frontdoor_routingrule(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.routing_rules.list()


def create_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name,
                                        id,
                                        properties,
                                        path,
                                        protocol,
                                        interval_in_seconds,
                                        resource_state,
                                        type):
    return client.health_probe_settings.create()


def delete_frontdoor_healthprobesetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.health_probe_settings.delete()


def list_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.list()


def show_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.show()


def show_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.show()


def list_frontdoor_healthprobesetting(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.health_probe_settings.list()


def create_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name,
                                          id,
                                          properties,
                                          sample_size,
                                          successful_samples_required,
                                          additional_latency_milliseconds,
                                          resource_state,
                                          type):
    return client.load_balancing_settings.create()


def delete_frontdoor_loadbalancingsetting(cmd, client,
                                          resource_group,
                                          front_door_name,
                                          name):
    return client.load_balancing_settings.delete()


def list_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.list()


def show_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.show()


def show_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.show()


def list_frontdoor_loadbalancingsetting(cmd, client,
                                        resource_group,
                                        front_door_name,
                                        name):
    return client.load_balancing_settings.list()


def create_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name,
                                 id,
                                 properties,
                                 backends,
                                 load_balancing_settings,
                                 health_probe_settings,
                                 resource_state,
                                 type):
    return client.backend_pools.create()


def delete_frontdoor_backendpool(cmd, client,
                                 resource_group,
                                 front_door_name,
                                 name):
    return client.backend_pools.delete()


def list_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.list()


def show_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.show()


def show_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.show()


def list_frontdoor_backendpool(cmd, client,
                               resource_group,
                               front_door_name,
                               name):
    return client.backend_pools.list()


def create_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name,
                                      id,
                                      properties,
                                      host_name,
                                      session_affinity_enabled_state,
                                      session_affinity_ttl_seconds,
                                      web_application_firewall_policy_link,
                                      resource_state,
                                      custom_https_provisioning_state,
                                      custom_https_provisioning_substate,
                                      custom_https_configuration,
                                      type):
    return client.frontend_endpoints.create()


def delete_frontdoor_frontendendpoint(cmd, client,
                                      resource_group,
                                      front_door_name,
                                      name):
    return client.frontend_endpoints.delete()


def list_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.list()


def show_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.show()


def show_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.show()


def list_frontdoor_frontendendpoint(cmd, client,
                                    resource_group,
                                    front_door_name,
                                    name):
    return client.frontend_endpoints.list()