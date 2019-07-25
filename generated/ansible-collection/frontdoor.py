#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: frontdoor
version_added: '2.9'
short_description: Manage Azure FrontDoor instance.
description:
  - 'Create, update and delete instance of Azure FrontDoor.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  location:
    description:
      - Resource location.
    type: str
  friendly_name:
    description:
      - A friendly name for the frontDoor
    type: str
  routing_rules:
    description:
      - Routing rules associated with this Front Door.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      frontend_endpoints:
        description:
          - Frontend endpoints associated with this rule
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      accepted_protocols:
        description:
          - Protocol schemes to match for this rule
        type: list
      patterns_to_match:
        description:
          - The route patterns of the rule.
        type: list
      enabled_state:
        description:
          - >-
            Whether to enable use of this rule. Permitted values are 'Enabled'
            or 'Disabled'
        type: str
      route_configuration:
        description:
          - A reference to the routing configuration.
        type: dict
      resource_state:
        description:
          - Resource status.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
  load_balancing_settings:
    description:
      - Load balancing settings associated with this Front Door instance.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      sample_size:
        description:
          - The number of samples to consider for load balancing decisions
        type: number
      successful_samples_required:
        description:
          - The number of samples within the sample period that must succeed
        type: number
      additional_latency_milliseconds:
        description:
          - >-
            The additional latency in milliseconds for probes to fall into the
            lowest latency bucket
        type: number
      resource_state:
        description:
          - Resource status.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
  health_probe_settings:
    description:
      - Health probe settings associated with this Front Door instance.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      path:
        description:
          - The path to use for the health probe. Default is /
        type: str
      protocol:
        description:
          - Protocol scheme to use for this probe
        type: str
      interval_in_seconds:
        description:
          - The number of seconds between health probes.
        type: number
      resource_state:
        description:
          - Resource status.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
  backend_pools:
    description:
      - Backend pools available to routing rules.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      backends:
        description:
          - The set of backends for this pool
        type: list
        suboptions:
          address:
            description:
              - Location of the backend (IP address or FQDN)
            type: str
          http_port:
            description:
              - The HTTP TCP port number. Must be between 1 and 65535.
            type: number
          https_port:
            description:
              - The HTTPS TCP port number. Must be between 1 and 65535.
            type: number
          enabled_state:
            description:
              - >-
                Whether to enable use of this backend. Permitted values are
                'Enabled' or 'Disabled'
            type: str
          priority:
            description:
              - >-
                Priority to use for load balancing. Higher priorities will not
                be used for load balancing if any lower priority backend is
                healthy.
            type: number
          weight:
            description:
              - Weight of this endpoint for load balancing purposes.
            type: number
          backend_host_header:
            description:
              - >-
                The value to use as the host header sent to the backend. If
                blank or unspecified, this defaults to the incoming host.
            type: str
      load_balancing_settings:
        description:
          - Load balancing settings for a backend pool
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      health_probe_settings:
        description:
          - L7 health probe settings for a backend pool
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      resource_state:
        description:
          - Resource status.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
  frontend_endpoints:
    description:
      - Frontend endpoints available to routing rules.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      host_name:
        description:
          - The host name of the frontendEndpoint. Must be a domain name.
        type: str
      session_affinity_enabled_state:
        description:
          - >-
            Whether to allow session affinity on this host. Valid options are
            'Enabled' or 'Disabled'
        type: str
      session_affinity_ttl_seconds:
        description:
          - >-
            UNUSED. This field will be ignored. The TTL to use in seconds for
            session affinity, if applicable.
        type: number
      web_application_firewall_policy_link:
        description:
          - >-
            Defines the Web Application Firewall policy for each host (if
            applicable)
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      resource_state:
        description:
          - Resource status.
        type: str
      custom_https_provisioning_state:
        description:
          - Provisioning status of Custom Https of the frontendEndpoint.
        type: str
      custom_https_provisioning_substate:
        description:
          - >-
            Provisioning substate shows the progress of custom HTTPS
            enabling/disabling process step by step.
        type: str
      custom_https_configuration:
        description:
          - The configuration specifying how to enable HTTPS
        type: dict
        suboptions:
          certificate_source:
            description:
              - Defines the source of the SSL certificate
            type: str
          protocol_type:
            description:
              - >-
                Defines the TLS extension protocol that is used for secure
                delivery
            type: str
          key_vault_certificate_source_parameters:
            description:
              - >-
                KeyVault certificate source parameters (if
                certificateSource=AzureKeyVault)
            type: dict
          front_door_certificate_source_parameters:
            description:
              - >-
                Parameters required for enabling SSL with Front Door-managed
                certificates (if certificateSource=FrontDoor)
            type: dict
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
  backend_pools_settings:
    description:
      - Settings for all backendPools
    type: dict
    suboptions:
      enforce_certificate_name_check:
        description:
          - >-
            Whether to enforce certificate name check on HTTPS requests to all
            backend pools. No effect on non-HTTPS requests.
        type: str
  enabled_state:
    description:
      - >-
        Operational status of the Front Door load balancer. Permitted values are
        'Enabled' or 'Disabled'
    type: str
  resource_state:
    description:
      - Resource status of the Front Door.
    type: str
  provisioning_state:
    description:
      - Provisioning state of the Front Door.
    type: str
  cname:
    description:
      - The host that each frontendEndpoint must CNAME to.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Resource type.
    type: str
  state:
    description:
      - Assert the state of the FrontDoor.
      - >-
        Use C(present) to create or update an FrontDoor and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Create or update specific Front Door
  azure.rm.frontdoor:
    resource_group: myResourceGroup
    name: myFrontDoor
    front_door_parameters:
      id: >-
        /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
        }}/providers/Microsoft.Network/frontDoors/{{ front_door_name }}
      location: westus
      tags:
        tag1: value1
        tag2: value2
      properties:
        routingRules:
          - name: routingRule1
            properties:
              frontendEndpoints:
                - id: >-
                    /subscriptions/{{ subscription_id }}/resourceGroups/{{
                    resource_group }}/providers/Microsoft.Network/frontDoors/{{
                    front_door_name }}/frontendEndpoints/{{
                    frontend_endpoint_name }}
                - id: >-
                    /subscriptions/{{ subscription_id }}/resourceGroups/{{
                    resource_group }}/providers/Microsoft.Network/frontDoors/{{
                    front_door_name }}/frontendEndpoints/{{
                    frontend_endpoint_name }}
              acceptedProtocols:
                - Http
              patternsToMatch:
                - /*
              routeConfiguration:
                '@odata.type': >-
                  #Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration
                backendPool:
                  id: >-
                    /subscriptions/{{ subscription_id }}/resourceGroups/{{
                    resource_group }}/providers/Microsoft.Network/frontDoors/{{
                    front_door_name }}/backendPools/{{ backend_pool_name }}
              enabledState: Enabled
        healthProbeSettings:
          - name: healthProbeSettings1
            properties:
              path: /
              protocol: Http
              intervalInSeconds: '120'
        loadBalancingSettings:
          - name: loadBalancingSettings1
            properties:
              sampleSize: '4'
              successfulSamplesRequired: '2'
        backendPools:
          - name: backendPool1
            properties:
              backends:
                - address: w3.contoso.com
                  httpPort: '80'
                  httpsPort: '443'
                  weight: '1'
                  priority: '2'
                - address: contoso.com.website-us-west-2.othercloud.net
                  httpPort: '80'
                  httpsPort: '443'
                  weight: '2'
                  priority: '1'
                - address: contoso1.azurewebsites.net
                  httpPort: '80'
                  httpsPort: '443'
                  weight: '1'
                  priority: '1'
              loadBalancingSettings:
                id: >-
                  /subscriptions/{{ subscription_id }}/resourceGroups/{{
                  resource_group }}/providers/Microsoft.Network/frontDoors/{{
                  front_door_name }}/loadBalancingSettings/{{
                  load_balancing_setting_name }}
              healthProbeSettings:
                id: >-
                  /subscriptions/{{ subscription_id }}/resourceGroups/{{
                  resource_group }}/providers/Microsoft.Network/frontDoors/{{
                  front_door_name }}/healthProbeSettings/{{
                  health_probe_setting_name }}
        frontendEndpoints:
          - name: frontendEndpoint1
            properties:
              hostName: www.contoso.com
              sessionAffinityEnabledState: Enabled
              sessionAffinityTtlSeconds: '60'
              webApplicationFirewallPolicyLink:
                id: >-
                  /subscriptions/{{ subscription_id }}/resourceGroups/{{
                  resource_group
                  }}/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/{{
                  front_door_web_application_firewall_policy_name }}
          - name: default
            properties:
              hostName: frontDoor1.azurefd.net
        backendPoolsSettings:
          enforceCertificateNameCheck: Enabled
        enabledState: Enabled
- name: Delete Front Door
  azure.rm.frontdoor:
    resource_group: myResourceGroup
    name: myFrontDoor
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"539","$type":"DictionaryType","valueType":{"$id":"540","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"541","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"542","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - Properties of the Front Door Load Balancer
  returned: always
  type: dict
  sample: null
  contains:
    friendly_name:
      description:
        - A friendly name for the frontDoor
      returned: always
      type: str
      sample: null
    routing_rules:
      description:
        - Routing rules associated with this Front Door.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the Front Door Routing Rule
          returned: always
          type: dict
          sample: null
          contains:
            frontend_endpoints:
              description:
                - Frontend endpoints associated with this rule
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            accepted_protocols:
              description:
                - Protocol schemes to match for this rule
              returned: always
              type: str
              sample: null
            patterns_to_match:
              description:
                - The route patterns of the rule.
              returned: always
              type: str
              sample: null
            enabled_state:
              description:
                - >-
                  Whether to enable use of this rule. Permitted values are
                  'Enabled' or 'Disabled'
              returned: always
              type: str
              sample: null
            route_configuration:
              description:
                - A reference to the routing configuration.
              returned: always
              type: dict
              sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
    load_balancing_settings:
      description:
        - Load balancing settings associated with this Front Door instance.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the load balancing settings
          returned: always
          type: dict
          sample: null
          contains:
            sample_size:
              description:
                - The number of samples to consider for load balancing decisions
              returned: always
              type: number
              sample: null
            successful_samples_required:
              description:
                - >-
                  The number of samples within the sample period that must
                  succeed
              returned: always
              type: number
              sample: null
            additional_latency_milliseconds:
              description:
                - >-
                  The additional latency in milliseconds for probes to fall into
                  the lowest latency bucket
              returned: always
              type: number
              sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
    health_probe_settings:
      description:
        - Health probe settings associated with this Front Door instance.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the health probe settings
          returned: always
          type: dict
          sample: null
          contains:
            path:
              description:
                - The path to use for the health probe. Default is /
              returned: always
              type: str
              sample: null
            protocol:
              description:
                - Protocol scheme to use for this probe
              returned: always
              type: str
              sample: null
            interval_in_seconds:
              description:
                - The number of seconds between health probes.
              returned: always
              type: number
              sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
    backend_pools:
      description:
        - Backend pools available to routing rules.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the Front Door Backend Pool
          returned: always
          type: dict
          sample: null
          contains:
            backends:
              description:
                - The set of backends for this pool
              returned: always
              type: dict
              sample: null
              contains:
                address:
                  description:
                    - Location of the backend (IP address or FQDN)
                  returned: always
                  type: str
                  sample: null
                http_port:
                  description:
                    - The HTTP TCP port number. Must be between 1 and 65535.
                  returned: always
                  type: number
                  sample: null
                https_port:
                  description:
                    - The HTTPS TCP port number. Must be between 1 and 65535.
                  returned: always
                  type: number
                  sample: null
                enabled_state:
                  description:
                    - >-
                      Whether to enable use of this backend. Permitted values
                      are 'Enabled' or 'Disabled'
                  returned: always
                  type: str
                  sample: null
                priority:
                  description:
                    - >-
                      Priority to use for load balancing. Higher priorities will
                      not be used for load balancing if any lower priority
                      backend is healthy.
                  returned: always
                  type: number
                  sample: null
                weight:
                  description:
                    - Weight of this endpoint for load balancing purposes.
                  returned: always
                  type: number
                  sample: null
                backend_host_header:
                  description:
                    - >-
                      The value to use as the host header sent to the backend.
                      If blank or unspecified, this defaults to the incoming
                      host.
                  returned: always
                  type: str
                  sample: null
            load_balancing_settings:
              description:
                - Load balancing settings for a backend pool
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            health_probe_settings:
              description:
                - L7 health probe settings for a backend pool
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
    frontend_endpoints:
      description:
        - Frontend endpoints available to routing rules.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the Frontend endpoint
          returned: always
          type: dict
          sample: null
          contains:
            host_name:
              description:
                - The host name of the frontendEndpoint. Must be a domain name.
              returned: always
              type: str
              sample: null
            session_affinity_enabled_state:
              description:
                - >-
                  Whether to allow session affinity on this host. Valid options
                  are 'Enabled' or 'Disabled'
              returned: always
              type: str
              sample: null
            session_affinity_ttl_seconds:
              description:
                - >-
                  UNUSED. This field will be ignored. The TTL to use in seconds
                  for session affinity, if applicable.
              returned: always
              type: number
              sample: null
            web_application_firewall_policy_link:
              description:
                - >-
                  Defines the Web Application Firewall policy for each host (if
                  applicable)
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource ID.
                  returned: always
                  type: str
                  sample: null
            resource_state:
              description:
                - Resource status.
              returned: always
              type: str
              sample: null
            custom_https_provisioning_state:
              description:
                - Provisioning status of Custom Https of the frontendEndpoint.
              returned: always
              type: str
              sample: null
            custom_https_provisioning_substate:
              description:
                - >-
                  Provisioning substate shows the progress of custom HTTPS
                  enabling/disabling process step by step.
              returned: always
              type: str
              sample: null
            custom_https_configuration:
              description:
                - The configuration specifying how to enable HTTPS
              returned: always
              type: dict
              sample: null
              contains:
                certificate_source:
                  description:
                    - Defines the source of the SSL certificate
                  returned: always
                  type: str
                  sample: null
                protocol_type:
                  description:
                    - >-
                      Defines the TLS extension protocol that is used for secure
                      delivery
                  returned: always
                  type: str
                  sample: null
                key_vault_certificate_source_parameters:
                  description:
                    - >-
                      KeyVault certificate source parameters (if
                      certificateSource=AzureKeyVault)
                  returned: always
                  type: dict
                  sample: null
                front_door_certificate_source_parameters:
                  description:
                    - >-
                      Parameters required for enabling SSL with Front
                      Door-managed certificates (if certificateSource=FrontDoor)
                  returned: always
                  type: dict
                  sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
          returned: always
          type: str
          sample: null
    backend_pools_settings:
      description:
        - Settings for all backendPools
      returned: always
      type: dict
      sample: null
      contains:
        enforce_certificate_name_check:
          description:
            - >-
              Whether to enforce certificate name check on HTTPS requests to all
              backend pools. No effect on non-HTTPS requests.
          returned: always
          type: str
          sample: null
    enabled_state:
      description:
        - >-
          Operational status of the Front Door load balancer. Permitted values
          are 'Enabled' or 'Disabled'
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status of the Front Door.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the Front Door.
      returned: always
      type: str
      sample: null
    cname:
      description:
        - The host that each frontendEndpoint must CNAME to.
      returned: always
      type: str
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFrontDoors(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='frontDoorName',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            friendly_name=dict(
                type='str',
                disposition='/properties/friendlyName'
            ),
            routing_rules=dict(
                type='list',
                disposition='/properties/routingRules',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    frontend_endpoints=dict(
                        type='list',
                        disposition='properties/frontendEndpoints',
                        options=dict(
                            id=dict(
                                type='str'
                            )
                        )
                    ),
                    accepted_protocols=dict(
                        type='list',
                        disposition='properties/acceptedProtocols',
                        choices=['Http',
                                 'Https']
                    ),
                    patterns_to_match=dict(
                        type='list',
                        disposition='properties/patternsToMatch'
                    ),
                    enabled_state=dict(
                        type='str',
                        disposition='properties/enabledState',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    route_configuration=dict(
                        type='dict',
                        disposition='properties/routeConfiguration'
                    ),
                    resource_state=dict(
                        type='str',
                        disposition='properties/resourceState',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            load_balancing_settings=dict(
                type='list',
                disposition='/properties/loadBalancingSettings',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    sample_size=dict(
                        type='number',
                        disposition='properties/sampleSize'
                    ),
                    successful_samples_required=dict(
                        type='number',
                        disposition='properties/successfulSamplesRequired'
                    ),
                    additional_latency_milliseconds=dict(
                        type='number',
                        disposition='properties/additionalLatencyMilliseconds'
                    ),
                    resource_state=dict(
                        type='str',
                        disposition='properties/resourceState',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            health_probe_settings=dict(
                type='list',
                disposition='/properties/healthProbeSettings',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    path=dict(
                        type='str',
                        disposition='properties/*'
                    ),
                    protocol=dict(
                        type='str',
                        disposition='properties/*',
                        choices=['Http',
                                 'Https']
                    ),
                    interval_in_seconds=dict(
                        type='number',
                        disposition='properties/intervalInSeconds'
                    ),
                    resource_state=dict(
                        type='str',
                        disposition='properties/resourceState',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            backend_pools=dict(
                type='list',
                disposition='/properties/backendPools',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    backends=dict(
                        type='list',
                        disposition='properties/*',
                        options=dict(
                            address=dict(
                                type='str'
                            ),
                            http_port=dict(
                                type='number',
                                disposition='httpPort'
                            ),
                            https_port=dict(
                                type='number',
                                disposition='httpsPort'
                            ),
                            enabled_state=dict(
                                type='str',
                                disposition='enabledState',
                                choices=['Enabled',
                                         'Disabled']
                            ),
                            priority=dict(
                                type='number'
                            ),
                            weight=dict(
                                type='number'
                            ),
                            backend_host_header=dict(
                                type='str',
                                disposition='backendHostHeader'
                            )
                        )
                    ),
                    load_balancing_settings=dict(
                        type='dict',
                        disposition='properties/loadBalancingSettings',
                        options=dict(
                            id=dict(
                                type='str'
                            )
                        )
                    ),
                    health_probe_settings=dict(
                        type='dict',
                        disposition='properties/healthProbeSettings',
                        options=dict(
                            id=dict(
                                type='str'
                            )
                        )
                    ),
                    resource_state=dict(
                        type='str',
                        disposition='properties/resourceState',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            frontend_endpoints=dict(
                type='list',
                disposition='/properties/frontendEndpoints',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    host_name=dict(
                        type='str',
                        disposition='properties/hostName'
                    ),
                    session_affinity_enabled_state=dict(
                        type='str',
                        disposition='properties/sessionAffinityEnabledState',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    session_affinity_ttl_seconds=dict(
                        type='number',
                        disposition='properties/sessionAffinityTtlSeconds'
                    ),
                    web_application_firewall_policy_link=dict(
                        type='dict',
                        disposition='properties/webApplicationFirewallPolicyLink',
                        options=dict(
                            id=dict(
                                type='str'
                            )
                        )
                    ),
                    resource_state=dict(
                        type='str',
                        disposition='properties/resourceState',
                        choices=['Creating',
                                 'Enabling',
                                 'Enabled',
                                 'Disabling',
                                 'Disabled',
                                 'Deleting']
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            backend_pools_settings=dict(
                type='dict',
                disposition='/properties/backendPoolsSettings',
                options=dict(
                    enforce_certificate_name_check=dict(
                        type='str',
                        disposition='enforceCertificateNameCheck',
                        choices=['Enabled',
                                 'Disabled']
                    )
                )
            ),
            enabled_state=dict(
                type='str',
                disposition='/properties/enabledState',
                choices=['Enabled',
                         'Disabled']
            ),
            resource_state=dict(
                type='str',
                disposition='/properties/resourceState',
                choices=['Creating',
                         'Enabling',
                         'Enabled',
                         'Disabling',
                         'Disabled',
                         'Deleting']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMFrontDoors, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                supports_check_mode=True,
                                                supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors' +
                    '/{{ front_door_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("FrontDoor instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('FrontDoor instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the FrontDoor instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('FrontDoor instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('FrontDoor instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the FrontDoor instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the FrontDoor instance.')
            self.fail('Error creating the FrontDoor instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the FrontDoor instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the FrontDoor instance.')
            self.fail('Error deleting the FrontDoor instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the FrontDoor instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("FrontDoor instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the FrontDoor instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMFrontDoors()


if __name__ == '__main__':
    main()
