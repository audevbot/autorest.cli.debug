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
module: azurefirewall
version_added: '2.9'
short_description: Manage Azure AzureFirewall instance.
description:
  - 'Create, update and delete instance of Azure AzureFirewall.'
options:
  resource_group:
    description:
      - The name of the resource group.
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
      id:
        description:
          - Resource ID.
        type: str
      private_ip_address:
        description:
          - >-
            The Firewall Internal Load Balancer IP to be used as the next hop in
            User Defined Routes.
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
  type:
    description:
      - Resource type.
    type: str
  etag:
    description:
      - >-
        Gets a unique read-only string that changes whenever the resource is
        updated.
    type: str
  state:
    description:
      - Assert the state of the AzureFirewall.
      - >-
        Use C(present) to create or update an AzureFirewall and C(absent) to
        delete it.
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
- name: Create Azure Firewall
  azure.rm.azurefirewall:
    resource_group: myResourceGroup
    name: myAzureFirewall
    tags:
      key1: value1
    application_rule_collections:
      - priority: '110'
        action: {}
        rules:
          - name: rule1
            description: Deny inbound rule
            protocols:
              - protocol_type: Https
                port: '443'
        name: apprulecoll
    nat_rule_collections:
      - priority: '112'
        action:
          type: Dnat
        rules:
          - name: DNAT-HTTPS-traffic
            description: D-NAT all outbound web traffic for inspection
            protocols:
              - TCP
        name: natrulecoll
    network_rule_collections:
      - priority: '112'
        action:
          type: Deny
        rules:
          - name: L4-traffic
            description: Block traffic based on source IPs and ports
            protocols:
              - TCP
        name: netrulecoll
    ip_configurations:
      - id: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Network/virtualNetworks/{{ virtual_network_name
          }}/subnets/{{ subnet_name }}
        name: azureFirewallIpConfiguration
- name: Delete Azure Firewall
  azure.rm.azurefirewall:
    resource_group: myResourceGroup
    name: myAzureFirewall
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
    {"$id":"440","$type":"DictionaryType","valueType":{"$id":"441","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"442","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"443","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - ''
  returned: always
  type: dict
  sample: null
  contains:
    application_rule_collections:
      description:
        - Collection of application rule collections used by Azure Firewall.
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
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            priority:
              description:
                - Priority of the application rule collection resource.
              returned: always
              type: number
              sample: null
            action:
              description:
                - The action type of a rule collection
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of action.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - Collection of rules used by a application rule collection.
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the application rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the rule.
                  returned: always
                  type: str
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses for this rule.
                  returned: always
                  type: str
                  sample: null
                protocols:
                  description:
                    - Array of ApplicationRuleProtocols.
                  returned: always
                  type: dict
                  sample: null
                target_fqdns:
                  description:
                    - List of FQDNs for this rule.
                  returned: always
                  type: str
                  sample: null
                fqdn_tags:
                  description:
                    - List of FQDN Tags for this rule.
                  returned: always
                  type: str
                  sample: null
            provisioning_state:
              description:
                - The provisioning state of the resource.
              returned: always
              type: str
              sample: null
        name:
          description:
            - >-
              Gets name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              Gets a unique read-only string that changes whenever the resource
              is updated.
          returned: always
          type: str
          sample: null
    nat_rule_collections:
      description:
        - Collection of NAT rule collections used by Azure Firewall.
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
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            priority:
              description:
                - Priority of the NAT rule collection resource.
              returned: always
              type: number
              sample: null
            action:
              description:
                - The action type of a NAT rule collection
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of action.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - Collection of rules used by a NAT rule collection.
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the NAT rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the rule.
                  returned: always
                  type: str
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses for this rule.
                  returned: always
                  type: str
                  sample: null
                destination_addresses:
                  description:
                    - List of destination IP addresses for this rule.
                  returned: always
                  type: str
                  sample: null
                destination_ports:
                  description:
                    - List of destination ports.
                  returned: always
                  type: str
                  sample: null
                protocols:
                  description:
                    - >-
                      Array of AzureFirewallNetworkRuleProtocols applicable to
                      this NAT rule.
                  returned: always
                  type: str
                  sample: null
                translated_address:
                  description:
                    - The translated address for this NAT rule.
                  returned: always
                  type: str
                  sample: null
                translated_port:
                  description:
                    - The translated port for this NAT rule.
                  returned: always
                  type: str
                  sample: null
            provisioning_state:
              description:
                - The provisioning state of the resource.
              returned: always
              type: str
              sample: null
        name:
          description:
            - >-
              Gets name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              Gets a unique read-only string that changes whenever the resource
              is updated.
          returned: always
          type: str
          sample: null
    network_rule_collections:
      description:
        - Collection of network rule collections used by Azure Firewall.
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
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            priority:
              description:
                - Priority of the network rule collection resource.
              returned: always
              type: number
              sample: null
            action:
              description:
                - The action type of a rule collection
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of action.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - Collection of rules used by a network rule collection.
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name of the network rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the rule.
                  returned: always
                  type: str
                  sample: null
                protocols:
                  description:
                    - Array of AzureFirewallNetworkRuleProtocols.
                  returned: always
                  type: str
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses for this rule.
                  returned: always
                  type: str
                  sample: null
                destination_addresses:
                  description:
                    - List of destination IP addresses.
                  returned: always
                  type: str
                  sample: null
                destination_ports:
                  description:
                    - List of destination ports.
                  returned: always
                  type: str
                  sample: null
            provisioning_state:
              description:
                - The provisioning state of the resource.
              returned: always
              type: str
              sample: null
        name:
          description:
            - >-
              Gets name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              Gets a unique read-only string that changes whenever the resource
              is updated.
          returned: always
          type: str
          sample: null
    ip_configurations:
      description:
        - IP configuration of the Azure Firewall resource.
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
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            private_ip_address:
              description:
                - >-
                  The Firewall Internal Load Balancer IP to be used as the next
                  hop in User Defined Routes.
              returned: always
              type: str
              sample: null
            subnet:
              description:
                - >-
                  Reference of the subnet resource. This resource must be named
                  'AzureFirewallSubnet'.
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
            public_ip_address:
              description:
                - >-
                  Reference of the PublicIP resource. This field is a mandatory
                  input if subnet is not null.
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
            provisioning_state:
              description:
                - The provisioning state of the resource.
              returned: always
              type: str
              sample: null
        name:
          description:
            - >-
              Name of the resource that is unique within a resource group. This
              name can be used to access the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              A unique read-only string that changes whenever the resource is
              updated.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the resource.
      returned: always
      type: str
      sample: null
etag:
  description:
    - >-
      Gets a unique read-only string that changes whenever the resource is
      updated.
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


class AzureRMAzureFirewalls(AzureRMModuleBaseExt):
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
                disposition='azureFirewallName',
                required=true
            ),
            id=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            application_rule_collections=dict(
                type='list',
                disposition='/properties/applicationRuleCollections',
                options=dict(
                    priority=dict(
                        type='number',
                        disposition='properties/*'
                    ),
                    action=dict(
                        type='dict',
                        disposition='properties/*'
                    ),
                    rules=dict(
                        type='list',
                        disposition='properties/*',
                        options=dict(
                            name=dict(
                                type='str'
                            ),
                            description=dict(
                                type='str'
                            ),
                            source_addresses=dict(
                                type='list',
                                disposition='sourceAddresses'
                            ),
                            protocols=dict(
                                type='list'
                            ),
                            target_fqdns=dict(
                                type='list',
                                disposition='targetFqdns'
                            ),
                            fqdn_tags=dict(
                                type='list',
                                disposition='fqdnTags'
                            )
                        )
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            nat_rule_collections=dict(
                type='list',
                disposition='/properties/natRuleCollections',
                options=dict(
                    priority=dict(
                        type='number',
                        disposition='properties/*'
                    ),
                    action=dict(
                        type='dict',
                        disposition='properties/*',
                        options=dict(
                            type=dict(
                                type='str',
                                choices=['Snat',
                                         'Dnat']
                            )
                        )
                    ),
                    rules=dict(
                        type='list',
                        disposition='properties/*',
                        options=dict(
                            name=dict(
                                type='str'
                            ),
                            description=dict(
                                type='str'
                            ),
                            source_addresses=dict(
                                type='list',
                                disposition='sourceAddresses'
                            ),
                            destination_addresses=dict(
                                type='list',
                                disposition='destinationAddresses'
                            ),
                            destination_ports=dict(
                                type='list',
                                disposition='destinationPorts'
                            ),
                            protocols=dict(
                                type='list',
                                choices=['TCP',
                                         'UDP',
                                         'Any',
                                         'ICMP']
                            ),
                            translated_address=dict(
                                type='str',
                                disposition='translatedAddress'
                            ),
                            translated_port=dict(
                                type='str',
                                disposition='translatedPort'
                            )
                        )
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            network_rule_collections=dict(
                type='list',
                disposition='/properties/networkRuleCollections',
                options=dict(
                    priority=dict(
                        type='number',
                        disposition='properties/*'
                    ),
                    action=dict(
                        type='dict',
                        disposition='properties/*',
                        options=dict(
                            type=dict(
                                type='str',
                                choices=['Allow',
                                         'Deny']
                            )
                        )
                    ),
                    rules=dict(
                        type='list',
                        disposition='properties/*',
                        options=dict(
                            name=dict(
                                type='str'
                            ),
                            description=dict(
                                type='str'
                            ),
                            protocols=dict(
                                type='list',
                                choices=['TCP',
                                         'UDP',
                                         'Any',
                                         'ICMP']
                            ),
                            source_addresses=dict(
                                type='list',
                                disposition='sourceAddresses'
                            ),
                            destination_addresses=dict(
                                type='list',
                                disposition='destinationAddresses'
                            ),
                            destination_ports=dict(
                                type='list',
                                disposition='destinationPorts'
                            )
                        )
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            ip_configurations=dict(
                type='list',
                disposition='/properties/ipConfigurations',
                options=dict(
                    id=dict(
                        type='raw',
                        disposition='properties/subnet/id',
                        pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                                 '/{{ resource_group }}/providers/Microsoft.Network'
                                 '/virtualNetworks/{{ virtual_network_name }}/subnets'
                                 '/{{ name }}')
                    ),
                    id=dict(
                        type='str',
                        disposition='properties/publicIPAddress/id'
                    ),
                    name=dict(
                        type='str'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.name = None
        self.type = None
        self.etag = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMAzureFirewalls, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/azureFirewalls' +
                    '/{{ azure_firewall_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ azure_firewall_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("AzureFirewall instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('AzureFirewall instance already exists')

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
            self.log('Need to Create / Update the AzureFirewall instance')

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
            self.log('AzureFirewall instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('AzureFirewall instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]
           self.results["etag"] = response["etag"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the AzureFirewall instance {0}'.format(self.))

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
            self.log('Error attempting to create the AzureFirewall instance.')
            self.fail('Error creating the AzureFirewall instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the AzureFirewall instance {0}'.format(self.))
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
            self.log('Error attempting to delete the AzureFirewall instance.')
            self.fail('Error deleting the AzureFirewall instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the AzureFirewall instance {0} is present'.format(self.))
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
            # self.log("AzureFirewall instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AzureFirewall instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMAzureFirewalls()


if __name__ == '__main__':
    main()
