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


# module equivalent: azure_rm_openshiftmanagedcluster
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ContainerService/openShiftManagedClusters/{{ open_shift_managed_cluster_name }}
def create_aro(cmd, client,
               resource_group,
               name,
               location,
               open_shift_version,
               tags=None,
               plan=None,
               network_profile=None,
               router_profiles=None,
               master_pool_profile=None,
               agent_pool_profiles=None,
               auth_profile=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['plan'] = json.loads(plan) if isinstance(plan, str) else plan
    body['open_shift_version'] = open_shift_version  # str
    body['network_profile'] = json.loads(network_profile) if isinstance(network_profile, str) else network_profile
    body['router_profiles'] = json.loads(router_profiles) if isinstance(router_profiles, str) else router_profiles
    body['master_pool_profile'] = json.loads(master_pool_profile) if isinstance(master_pool_profile, str) else master_pool_profile
    body['agent_pool_profiles'] = json.loads(agent_pool_profiles) if isinstance(agent_pool_profiles, str) else agent_pool_profiles
    body['auth_profile'] = json.loads(auth_profile) if isinstance(auth_profile, str) else auth_profile
    return client.create_or_update(resource_group_name=resource_group, resource_name=name, parameters=body)


# module equivalent: azure_rm_openshiftmanagedcluster
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ContainerService/openShiftManagedClusters/{{ open_shift_managed_cluster_name }}
def update_aro(cmd, client, body,
               resource_group,
               name,
               location,
               open_shift_version,
               tags=None,
               plan=None,
               network_profile=None,
               router_profiles=None,
               master_pool_profile=None,
               agent_pool_profiles=None,
               auth_profile=None):
    body = client.get(resource_group_name=resource_group, resource_name=name).as_dict()
    body.location = location  # str
    body.tags = tags  # dictionary
    body.plan = json.loads(plan) if isinstance(plan, str) else plan
    body.open_shift_version = open_shift_version  # str
    body.network_profile = json.loads(network_profile) if isinstance(network_profile, str) else network_profile
    body.router_profiles = json.loads(router_profiles) if isinstance(router_profiles, str) else router_profiles
    body.master_pool_profile = json.loads(master_pool_profile) if isinstance(master_pool_profile, str) else master_pool_profile
    body.agent_pool_profiles = json.loads(agent_pool_profiles) if isinstance(agent_pool_profiles, str) else agent_pool_profiles
    body.auth_profile = json.loads(auth_profile) if isinstance(auth_profile, str) else auth_profile
    return client.create_or_update(resource_group_name=resource_group, resource_name=name, parameters=body)


# module equivalent: azure_rm_openshiftmanagedcluster
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ContainerService/openShiftManagedClusters/{{ open_shift_managed_cluster_name }}
def list_aro(cmd, client,
             resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list()
