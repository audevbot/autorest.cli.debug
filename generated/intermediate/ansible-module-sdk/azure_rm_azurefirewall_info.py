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
module: azure_rm_azurefirewall_info
version_added: '2.9'
short_description: Get AzureFirewall info.
description:
  - Get info of AzureFirewall.
options:
  resource_group:
    description:
      - The name of the resource group.
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
  application_rule_collections:
    description:
      - Collection of application rule collections used by Azure Firewall.
    type: list
    suboptions:
      priority:
        description:
          - Priority of the application rule collection resource.
        type: number
      action:
        description:
          - The action type of a rule collection
        type: dict
      rules:
        description:
          - Collection of rules used by a application rule collection.
        type: list
        suboptions:
          name:
            description:
              - Name of the application rule.
            type: str
          description:
            description:
              - Description of the rule.
            type: str
          source_addresses:
            description:
              - List of source IP addresses for this rule.
            type: list
          protocols:
            description:
              - Array of ApplicationRuleProtocols.
            type: list
          target_fqdns:
            description:
              - List of FQDNs for this rule.
            type: list
          fqdn_tags:
            description:
              - List of FQDN Tags for this rule.
            type: list
      provisioning_state:
        description:
          - The provisioning state of the resource.
        type: str
      name:
        description:
          - >-
            Gets name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      etag:
        description:
          - >-
            Gets a unique read-only string that changes whenever the resource is
            updated.
        type: str
  nat_rule_collections:
    description:
      - Collection of NAT rule collections used by Azure Firewall.
    type: list
    suboptions:
      priority:
        description:
          - Priority of the NAT rule collection resource.
        type: number
      action:
        description:
          - The action type of a NAT rule collection
        type: dict
        suboptions:
          type:
            description:
              - The type of action.
            type: str
      rules:
        description:
          - Collection of rules used by a NAT rule collection.
        type: list
        suboptions:
          name:
            description:
              - Name of the NAT rule.
            type: str
          description:
            description:
              - Description of the rule.
            type: str
          source_addresses:
            description:
              - List of source IP addresses for this rule.
            type: list
          destination_addresses:
            description:
              - List of destination IP addresses for this rule.
            type: list
          destination_ports:
            description:
              - List of destination ports.
            type: list
          protocols:
            description:
              - >-
                Array of AzureFirewallNetworkRuleProtocols applicable to this
                NAT rule.
            type: list
          translated_address:
            description:
              - The translated address for this NAT rule.
            type: str
          translated_port:
            description:
              - The translated port for this NAT rule.
            type: str
      provisioning_state:
        description:
          - The provisioning state of the resource.
        type: str
      name:
        description:
          - >-
            Gets name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      etag:
        description:
          - >-
            Gets a unique read-only string that changes whenever the resource is
            updated.
        type: str
  network_rule_collections:
    description:
      - Collection of network rule collections used by Azure Firewall.
    type: list
    suboptions:
      priority:
        description:
          - Priority of the network rule collection resource.
        type: number
      action:
        description:
          - The action type of a rule collection
        type: dict
        suboptions:
          type:
            description:
              - The type of action.
            type: str
      rules:
        description:
          - Collection of rules used by a network rule collection.
        type: list
        suboptions:
          name:
            description:
              - Name of the network rule.
            type: str
          description:
            description:
              - Description of the rule.
            type: str
          protocols:
            description:
              - Array of AzureFirewallNetworkRuleProtocols.
            type: list
          source_addresses:
            description:
              - List of source IP addresses for this rule.
            type: list
          destination_addresses:
            description:
              - List of destination IP addresses.
            type: list
          destination_ports:
            description:
              - List of destination ports.
            type: list
      provisioning_state:
        description:
          - The provisioning state of the resource.
        type: str
      name:
        description:
          - >-
            Gets name of the resource that is unique within a resource group.
            This name can be used to access the resource.
        type: str
      etag:
        description:
          - >-
            Gets a unique read-only string that changes whenever the resource is
            updated.
        type: str
  ip_configurations:
    description:
      - IP configuration of the Azure Firewall resource.
    type: list
    suboptions:
      private_ip_address:
        description:
          - >-
            The Firewall Internal Load Balancer IP to be used as the next hop in
            User Defined Routes.
        type: str
      id:
        description:
          - Resource ID.
        type: str
      provisioning_state:
        description:
          - The provisioning state of the resource.
        type: str
      name:
        description:
          - >-
            Name of the resource that is unique within a resource group. This
            name can be used to access the resource.
        type: str
      etag:
        description:
          - >-
            A unique read-only string that changes whenever the resource is
            updated.
        type: str
  provisioning_state:
    description:
      - The provisioning state of the resource.
    type: str
  etag:
    description:
      - >-
        Gets a unique read-only string that changes whenever the resource is
        updated.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List all Azure Firewalls for a given subscription
  azure_rm_azurefirewall_info: {}
- name: List all Azure Firewalls for a given resource group
  azure_rm_azurefirewall_info:
    resource_group: myResourceGroup
- name: Get Azure Firewall
  azure_rm_azurefirewall_info:
    resource_group: myResourceGroup
    name: myAzureFirewall

'''

RETURN = '''
azure_firewalls:
  description: >-
    A list of dict results where the key is the name of the AzureFirewall and
    the values are the facts for that AzureFirewall.
  returned: always
  type: complex
  contains:
    azurefirewall_name:
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
            {"$id":"440","$type":"DictionaryType","valueType":{"$id":"441","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"442","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"443","fixed":false},"deprecated":false}]
          sample: null
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null
        etag:
          description:
            - >-
              Gets a unique read-only string that changes whenever the resource
              is updated.
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
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAzureFirewallsInfo(AzureRMModuleBase):
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
        self.etag = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAzureFirewallsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['azure_firewalls'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['azure_firewalls'] = self.format_item(self.list())
        else:
            self.results['azure_firewalls'] = [self.format_item(self.listall())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.azure_firewalls.get(resource_group_name=self.resource_group,
                                                            azure_firewall_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.azure_firewalls.list(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.azure_firewalls.list_all()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMAzureFirewallsInfo()


if __name__ == '__main__':
    main()
