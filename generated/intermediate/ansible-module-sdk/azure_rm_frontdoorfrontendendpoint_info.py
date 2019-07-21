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
module: azure_rm_frontdoorfrontendendpoint_info
version_added: '2.9'
short_description: Get FrontendEndpoint info.
description:
  - Get info of FrontendEndpoint.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
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
          - Defines the TLS extension protocol that is used for secure delivery
        type: str
      key_vault_certificate_source_parameters:
        description:
          - >-
            KeyVault certificate source parameters (if
            certificateSource=AzureKeyVault)
        type: dict
        suboptions:
          vault:
            description:
              - The Key Vault containing the SSL certificate
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          secret_name:
            description:
              - >-
                The name of the Key Vault secret representing the full
                certificate PFX
            type: str
          secret_version:
            description:
              - >-
                The version of the Key Vault secret representing the full
                certificate PFX
            type: str
      front_door_certificate_source_parameters:
        description:
          - >-
            Parameters required for enabling SSL with Front Door-managed
            certificates (if certificateSource=FrontDoor)
        type: dict
        suboptions:
          certificate_type:
            description:
              - >-
                Defines the type of the certificate used for secure connections
                to a frontendEndpoint
            type: str
  type:
    description:
      - Resource type.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List Frontend endpoints in a Front Door
  azure_rm_frontdoorfrontendendpoint_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
- name: Get Frontend Endpoint
  azure_rm_frontdoorfrontendendpoint_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myFrontendEndpoint

'''

RETURN = '''
frontend_endpoints:
  description: >-
    A list of dict results where the key is the name of the FrontendEndpoint and
    the values are the facts for that FrontendEndpoint.
  returned: always
  type: complex
  contains:
    frontendendpoint_name:
      description: The key is the name of the server that the values relate to.
      type: complex
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


class AzureRMFrontendEndpointsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            front_door_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.front_door_name = None
        self.name = None
        self.id = None
        self.properties = None
        self.name = None
        self.type = None

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
        super(AzureRMFrontendEndpointsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontdoorClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.front_door_name is not None and
            self.name is not None):
            self.results['frontend_endpoints'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.front_door_name is not None):
            self.results['frontend_endpoints'] = self.format_item(self.listbyfrontdoor())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.frontend_endpoints.get(resource_group_name=self.resource_group,
                                                               front_door_name=self.front_door_name,
                                                               frontend_endpoint_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyfrontdoor(self):
        response = None

        try:
            response = self.mgmt_client.frontend_endpoints.list_by_front_door(resource_group_name=self.resource_group,
                                                                              front_door_name=self.front_door_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMFrontendEndpointsInfo()


if __name__ == '__main__':
    main()
