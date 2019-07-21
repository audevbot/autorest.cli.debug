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
module: azure_rm_frontdoor_info
version_added: '2.9'
short_description: Get FrontDoor info.
description:
  - Get info of FrontDoor.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    type: str
  name:
    description:
      - Resource name.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Resource type.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List all Front Doors
  azure_rm_frontdoor_info: {}
- name: List Front Doors in a Resource Group
  azure_rm_frontdoor_info:
    resource_group: myResourceGroup
- name: Get Front Door
  azure_rm_frontdoor_info:
    resource_group: myResourceGroup
    name: myFrontDoor

'''

RETURN = '''
front_doors:
  description: >-
    A list of dict results where the key is the name of the FrontDoor and the
    values are the facts for that FrontDoor.
  returned: always
  type: complex
  contains:
    frontdoor_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMFrontDoorsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.tags = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMFrontDoorsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['front_doors'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['front_doors'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['front_doors'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
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

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbyresourcegroup(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMFrontDoorsInfo()


if __name__ == '__main__':
    main()
