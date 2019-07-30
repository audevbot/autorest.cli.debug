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
module: azure_rm_webapplicationfirewallpolicy_info
version_added: '2.9'
short_description: Get WebApplicationFirewallPolicy info.
description:
  - Get info of WebApplicationFirewallPolicy.
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
  policy_settings:
    description:
      - Describes policySettings for policy.
    type: dict
    suboptions:
      enabled_state:
        description:
          - Describes if the policy is in enabled state or disabled state.
        type: str
      mode:
        description:
          - >-
            Describes if it is in detection mode or prevention mode at policy
            level.
        type: str
  custom_rules:
    description:
      - Describes custom rules inside the policy.
    type: list
    suboptions:
      name:
        description:
          - >-
            Gets name of the resource that is unique within a policy. This name
            can be used to access the resource.
        type: str
      etag:
        description:
          - >-
            Gets a unique read-only string that changes whenever the resource is
            updated.
        type: str
      priority:
        description:
          - >-
            Describes priority of the rule. Rules with a lower value will be
            evaluated before rules with a higher value.
        required: true
        type: number
      rule_type:
        description:
          - Describes type of rule.
        required: true
        type: str
      match_conditions:
        description:
          - List of match conditions.
        required: true
        type: list
        suboptions:
          match_variables:
            description:
              - List of match variables.
            required: true
            type: list
            suboptions:
              variable_name:
                description:
                  - Match Variable.
                required: true
                type: str
              selector:
                description:
                  - Describes field of the matchVariable collection.
                type: str
          operator:
            description:
              - Describes operator to be matched.
            required: true
            type: str
          negation_conditon:
            description:
              - Describes if this is negate condition or not.
            type: boolean
          match_values:
            description:
              - Match value.
            required: true
            type: list
          transforms:
            description:
              - List of transforms.
            type: list
      action:
        description:
          - Type of Actions.
        required: true
        type: str
  application_gateways:
    description:
      - A collection of references to application gateways.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type.
        type: str
      location:
        description:
          - Resource location.
        type: str
      sku:
        description:
          - SKU of the application gateway resource.
        type: dict
        suboptions:
          name:
            description:
              - Name of an application gateway SKU.
            type: str
          tier:
            description:
              - Tier of an application gateway.
            type: str
          capacity:
            description:
              - Capacity (instance count) of an application gateway.
            type: number
      ssl_policy:
        description:
          - SSL policy of the application gateway resource.
        type: dict
        suboptions:
          disabled_ssl_protocols:
            description:
              - Ssl protocols to be disabled on application gateway.
            type: list
          policy_type:
            description:
              - Type of Ssl Policy.
            type: str
          policy_name:
            description:
              - Name of Ssl predefined policy.
            type: str
          cipher_suites:
            description:
              - >-
                Ssl cipher suites to be enabled in the specified order to
                application gateway.
            type: list
          min_protocol_version:
            description:
              - >-
                Minimum version of Ssl protocol to be supported on application
                gateway.
            type: str
      operational_state:
        description:
          - Operational state of the application gateway resource.
        type: str
      gateway_ipconfigurations:
        description:
          - >-
            Subnets of the application gateway resource. For default limits, see
            [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the IP configuration that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      authentication_certificates:
        description:
          - >-
            Authentication certificates of the application gateway resource. For
            default limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the authentication certificate that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      trusted_root_certificates:
        description:
          - >-
            Trusted Root certificates of the application gateway resource. For
            default limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the trusted root certificate that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      ssl_certificates:
        description:
          - >-
            SSL certificates of the application gateway resource. For default
            limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the SSL certificate that is unique within an Application
                Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      frontend_ipconfigurations:
        description:
          - >-
            Frontend IP addresses of the application gateway resource. For
            default limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the frontend IP configuration that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      frontend_ports:
        description:
          - >-
            Frontend ports of the application gateway resource. For default
            limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the frontend port that is unique within an Application
                Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      probes:
        description:
          - Probes of the application gateway resource.
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - Name of the probe that is unique within an Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      backend_address_pools:
        description:
          - >-
            Backend address pool of the application gateway resource. For
            default limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the backend address pool that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      backend_http_settings_collection:
        description:
          - >-
            Backend http settings of the application gateway resource. For
            default limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the backend http settings that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      http_listeners:
        description:
          - >-
            Http listeners of the application gateway resource. For default
            limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the HTTP listener that is unique within an Application
                Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      url_path_maps:
        description:
          - >-
            URL path map of the application gateway resource. For default
            limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the URL path map that is unique within an Application
                Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      request_routing_rules:
        description:
          - Request routing rules of the application gateway resource.
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the request routing rule that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      rewrite_rule_sets:
        description:
          - Rewrite rules for the application gateway resource.
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the rewrite rule set that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
      redirect_configurations:
        description:
          - >-
            Redirect configurations of the application gateway resource. For
            default limits, see [Application Gateway
            limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
        type: list
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
          name:
            description:
              - >-
                Name of the redirect configuration that is unique within an
                Application Gateway.
            type: str
          etag:
            description:
              - >-
                A unique read-only string that changes whenever the resource is
                updated.
            type: str
          type:
            description:
              - Type of the resource.
            type: str
      web_application_firewall_configuration:
        description:
          - Web application firewall configuration.
        type: dict
        suboptions:
          enabled:
            description:
              - Whether the web application firewall is enabled or not.
            required: true
            type: boolean
          firewall_mode:
            description:
              - Web application firewall mode.
            required: true
            type: str
          rule_set_type:
            description:
              - >-
                The type of the web application firewall rule set. Possible
                values are: 'OWASP'.
            required: true
            type: str
          rule_set_version:
            description:
              - The version of the rule set type.
            required: true
            type: str
          disabled_rule_groups:
            description:
              - The disabled rule groups.
            type: list
          request_body_check:
            description:
              - Whether allow WAF to check request Body.
            type: boolean
          max_request_body_size:
            description:
              - Maximum request body size for WAF.
            type: number
          max_request_body_size_in_kb:
            description:
              - Maximum request body size in Kb for WAF.
            type: number
          file_upload_limit_in_mb:
            description:
              - Maximum file upload size in Mb for WAF.
            type: number
          exclusions:
            description:
              - The exclusion list.
            type: list
      firewall_policy:
        description:
          - Reference of the FirewallPolicy resource.
        type: dict
        suboptions:
          id:
            description:
              - Resource ID.
            type: str
      enable_http2:
        description:
          - Whether HTTP2 is enabled on the application gateway resource.
        type: boolean
      enable_fips:
        description:
          - Whether FIPS is enabled on the application gateway resource.
        type: boolean
      autoscale_configuration:
        description:
          - Autoscale Configuration.
        type: dict
        suboptions:
          min_capacity:
            description:
              - Lower bound on number of Application Gateway capacity.
            required: true
            type: number
          max_capacity:
            description:
              - Upper bound on number of Application Gateway capacity.
            type: number
      resource_guid:
        description:
          - Resource GUID property of the application gateway resource.
        type: str
      provisioning_state:
        description:
          - >-
            Provisioning state of the application gateway resource. Possible
            values are: 'Updating', 'Deleting', and 'Failed'.
        type: str
      custom_error_configurations:
        description:
          - Custom error configurations of the application gateway resource.
        type: list
        suboptions:
          status_code:
            description:
              - Status code of the application gateway customer error.
            type: str
          custom_error_page_url:
            description:
              - Error page URL of the application gateway customer error.
            type: str
      etag:
        description:
          - >-
            A unique read-only string that changes whenever the resource is
            updated.
        type: str
      zones:
        description:
          - >-
            A list of availability zones denoting where the resource needs to
            come from.
        type: list
      identity:
        description:
          - 'The identity of the application gateway, if configured.'
        type: dict
        suboptions:
          principal_id:
            description:
              - >-
                The principal id of the system assigned identity. This property
                will only be provided for a system assigned identity.
            type: str
          tenant_id:
            description:
              - >-
                The tenant id of the system assigned identity. This property
                will only be provided for a system assigned identity.
            type: str
          type:
            description:
              - >-
                The type of identity used for the resource. The type
                'SystemAssigned, UserAssigned' includes both an implicitly
                created identity and a set of user assigned identities. The type
                'None' will remove any identities from the virtual machine.
            type: str
          user_assigned_identities:
            description:
              - >-
                The list of user identities associated with resource. The user
                identity dictionary key references will be ARM resource ids in
                the form:
                '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
            type: >-
              unknown[DictionaryType
              {"$id":"3130","$type":"DictionaryType","valueType":{"$ref":"3087"},"supportsAdditionalProperties":false,"name":{"$id":"3131","fixed":false},"deprecated":false}]
  provisioning_state:
    description:
      - Provisioning state of the WebApplicationFirewallPolicy.
    type: str
  resource_state:
    description:
      - Resource status of the policy.
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
- name: Lists all WAF policies in a subscription
  azure_rm_webapplicationfirewallpolicy_info: {}
- name: Lists all WAF policies in a resource group
  azure_rm_webapplicationfirewallpolicy_info:
    resource_group: myResourceGroup
- name: Gets a WAF policy within a resource group
  azure_rm_webapplicationfirewallpolicy_info:
    resource_group: myResourceGroup
    name: myApplicationGatewayWebApplicationFirewallPolicy

'''

RETURN = '''
web_application_firewall_policies:
  description: >-
    A list of dict results where the key is the name of the
    WebApplicationFirewallPolicy and the values are the facts for that
    WebApplicationFirewallPolicy.
  returned: always
  type: complex
  contains:
    webapplicationfirewallpolicy_name:
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
            {"$id":"1099","$type":"DictionaryType","valueType":{"$id":"1100","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"1101","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"1102","fixed":false},"deprecated":false}]
          sample: null
        properties:
          description:
            - Properties of the web application firewall policy.
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


class AzureRMWebApplicationFirewallPoliciesInfo(AzureRMModuleBase):
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
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMWebApplicationFirewallPoliciesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['web_application_firewall_policies'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['web_application_firewall_policies'] = self.format_item(self.list())
        else:
            self.results['web_application_firewall_policies'] = [self.format_item(self.listall())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.web_application_firewall_policies.get(resource_group_name=self.resource_group,
                                                                              policy_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.web_application_firewall_policies.list(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.web_application_firewall_policies.list_all()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMWebApplicationFirewallPoliciesInfo()


if __name__ == '__main__':
    main()
