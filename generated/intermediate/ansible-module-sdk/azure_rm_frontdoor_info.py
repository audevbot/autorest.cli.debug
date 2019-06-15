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
  name:
    description:
      - Resource name.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type.
  location:
    description:
      - Resource location.
  friendly_name:
    description:
      - A friendly name for the frontDoor
  routing_rules:
    description:
      - Routing rules associated with this Front Door.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      frontend_endpoints:
        description:
          - Frontend endpoints associated with this rule
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
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
      route_configuration:
        description:
          - A reference to the routing configuration.
      resource_state:
        description:
          - Resource status.
      name:
        description:
          - Resource name.
      type:
        description:
          - Resource type.
  load_balancing_settings:
    description:
      - Load balancing settings associated with this Front Door instance.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      sample_size:
        description:
          - The number of samples to consider for load balancing decisions
      successful_samples_required:
        description:
          - The number of samples within the sample period that must succeed
      additional_latency_milliseconds:
        description:
          - >-
            The additional latency in milliseconds for probes to fall into the
            lowest latency bucket
      resource_state:
        description:
          - Resource status.
      name:
        description:
          - Resource name.
      type:
        description:
          - Resource type.
  health_probe_settings:
    description:
      - Health probe settings associated with this Front Door instance.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      path:
        description:
          - The path to use for the health probe. Default is /
      protocol:
        description:
          - Protocol scheme to use for this probe
      interval_in_seconds:
        description:
          - The number of seconds between health probes.
      resource_state:
        description:
          - Resource status.
      name:
        description:
          - Resource name.
      type:
        description:
          - Resource type.
  backend_pools:
    description:
      - Backend pools available to routing rules.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      backends:
        description:
          - The set of backends for this pool
        type: list
        suboptions:
          address:
            description:
              - Location of the backend (IP address or FQDN)
          http_port:
            description:
              - The HTTP TCP port number. Must be between 1 and 65535.
          https_port:
            description:
              - The HTTPS TCP port number. Must be between 1 and 65535.
          enabled_state:
            description:
              - >-
                Whether to enable use of this backend. Permitted values are
                'Enabled' or 'Disabled'
          priority:
            description:
              - >-
                Priority to use for load balancing. Higher priorities will not
                be used for load balancing if any lower priority backend is
                healthy.
          weight:
            description:
              - Weight of this endpoint for load balancing purposes.
          backend_host_header:
            description:
              - >-
                The value to use as the host header sent to the backend. If
                blank or unspecified, this defaults to the incoming host.
      load_balancing_settings:
        description:
          - Load balancing settings for a backend pool
        suboptions:
          id:
            description:
              - Resource ID.
      health_probe_settings:
        description:
          - L7 health probe settings for a backend pool
        suboptions:
          id:
            description:
              - Resource ID.
      resource_state:
        description:
          - Resource status.
      name:
        description:
          - Resource name.
      type:
        description:
          - Resource type.
  frontend_endpoints:
    description:
      - Frontend endpoints available to routing rules.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      host_name:
        description:
          - The host name of the frontendEndpoint. Must be a domain name.
      session_affinity_enabled_state:
        description:
          - >-
            Whether to allow session affinity on this host. Valid options are
            'Enabled' or 'Disabled'
      session_affinity_ttl_seconds:
        description:
          - >-
            UNUSED. This field will be ignored. The TTL to use in seconds for
            session affinity, if applicable.
      web_application_firewall_policy_link:
        description:
          - >-
            Defines the Web Application Firewall policy for each host (if
            applicable)
        suboptions:
          id:
            description:
              - Resource ID.
      resource_state:
        description:
          - Resource status.
      custom_https_provisioning_state:
        description:
          - Provisioning status of Custom Https of the frontendEndpoint.
      custom_https_provisioning_substate:
        description:
          - >-
            Provisioning substate shows the progress of custom HTTPS
            enabling/disabling process step by step.
      custom_https_configuration:
        description:
          - The configuration specifying how to enable HTTPS
        suboptions:
          certificate_source:
            description:
              - Defines the source of the SSL certificate
          protocol_type:
            description:
              - >-
                Defines the TLS extension protocol that is used for secure
                delivery
          key_vault_certificate_source_parameters:
            description:
              - >-
                KeyVault certificate source parameters (if
                certificateSource=AzureKeyVault)
          front_door_certificate_source_parameters:
            description:
              - >-
                Parameters required for enabling SSL with Front Door-managed
                certificates (if certificateSource=FrontDoor)
      name:
        description:
          - Resource name.
      type:
        description:
          - Resource type.
  backend_pools_settings:
    description:
      - Settings for all backendPools
    suboptions:
      enforce_certificate_name_check:
        description:
          - >-
            Whether to enforce certificate name check on HTTPS requests to all
            backend pools. No effect on non-HTTPS requests.
  enabled_state:
    description:
      - >-
        Operational status of the Front Door load balancer. Permitted values are
        'Enabled' or 'Disabled'
  resource_state:
    description:
      - Resource status of the Front Door.
  provisioning_state:
    description:
      - Provisioning state of the Front Door.
  cname:
    description:
      - The host that each frontendEndpoint must CNAME to.
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
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.frontdoor import FrontdoorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


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

        self.mgmt_client = self.get_mgmt_svc_client(FrontdoorClientClient,
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

        try:
            response = self.mgmt_client.front_doors.get(resource_group_name=self.resource_group,
                                                        front_door_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.front_doors.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.front_doors.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMFrontDoorsInfo()


if __name__ == '__main__':
    main()
