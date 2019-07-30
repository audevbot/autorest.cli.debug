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
module: azure_rm_webapplicationfirewallpolicy
version_added: '2.9'
short_description: Manage Azure WebApplicationFirewallPolicy instance.
description:
  - 'Create, update and delete instance of Azure WebApplicationFirewallPolicy.'
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
      etag:
        description:
          - >-
            Gets a unique read-only string that changes whenever the resource is
            updated.
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
  type:
    description:
      - Resource type.
    type: str
  state:
    description:
      - Assert the state of the WebApplicationFirewallPolicy.
      - >-
        Use C(present) to create or update an WebApplicationFirewallPolicy and
        C(absent) to delete it.
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
- name: Creates or updates a WAF policy within a resource group
  azure_rm_webapplicationfirewallpolicy:
    resource_group: myResourceGroup
    name: myApplicationGatewayWebApplicationFirewallPolicy
    location: WestUs
    custom_rules:
      - name: Rule1
        priority: '1'
        rule_type: MatchRule
        match_conditions:
          - match_variables:
              - variable_name: RemoteAddr
            operator: IPMatch
            match_values:
              - 192.168.1.0/24
              - 10.0.0.0/24
        action: Block
      - name: Rule2
        priority: '2'
        rule_type: MatchRule
        match_conditions:
          - match_variables:
              - variable_name: RemoteAddr
            operator: IPMatch
            match_values:
              - 192.168.1.0/24
          - match_variables:
              - variable_name: RequestHeaders
                selector: UserAgent
            operator: Contains
            match_values:
              - Windows
        action: Block
- name: Deletes a WAF policy within a resource group
  azure_rm_webapplicationfirewallpolicy:
    resource_group: myResourceGroup
    name: myApplicationGatewayWebApplicationFirewallPolicy
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
    {"$id":"1099","$type":"DictionaryType","valueType":{"$id":"1100","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"1101","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"1102","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - Properties of the web application firewall policy.
  returned: always
  type: dict
  sample: null
  contains:
    policy_settings:
      description:
        - Describes policySettings for policy.
      returned: always
      type: dict
      sample: null
      contains:
        enabled_state:
          description:
            - Describes if the policy is in enabled state or disabled state.
          returned: always
          type: str
          sample: null
        mode:
          description:
            - >-
              Describes if it is in detection mode or prevention mode at policy
              level.
          returned: always
          type: str
          sample: null
    custom_rules:
      description:
        - Describes custom rules inside the policy.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              Gets name of the resource that is unique within a policy. This
              name can be used to access the resource.
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
        priority:
          description:
            - >-
              Describes priority of the rule. Rules with a lower value will be
              evaluated before rules with a higher value.
          returned: always
          type: number
          sample: null
        rule_type:
          description:
            - Describes type of rule.
          returned: always
          type: str
          sample: null
        match_conditions:
          description:
            - List of match conditions.
          returned: always
          type: dict
          sample: null
          contains:
            match_variables:
              description:
                - List of match variables.
              returned: always
              type: dict
              sample: null
              contains:
                variable_name:
                  description:
                    - Match Variable.
                  returned: always
                  type: str
                  sample: null
                selector:
                  description:
                    - Describes field of the matchVariable collection.
                  returned: always
                  type: str
                  sample: null
            operator:
              description:
                - Describes operator to be matched.
              returned: always
              type: str
              sample: null
            negation_conditon:
              description:
                - Describes if this is negate condition or not.
              returned: always
              type: boolean
              sample: null
            match_values:
              description:
                - Match value.
              returned: always
              type: str
              sample: null
            transforms:
              description:
                - List of transforms.
              returned: always
              type: str
              sample: null
        action:
          description:
            - Type of Actions.
          returned: always
          type: str
          sample: null
    application_gateways:
      description:
        - A collection of references to application gateways.
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
            - Properties of the application gateway.
          returned: always
          type: dict
          sample: null
        sku:
          description:
            - SKU of the application gateway resource.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of an application gateway SKU.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - Tier of an application gateway.
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - Capacity (instance count) of an application gateway.
              returned: always
              type: number
              sample: null
        ssl_policy:
          description:
            - SSL policy of the application gateway resource.
          returned: always
          type: dict
          sample: null
          contains:
            disabled_ssl_protocols:
              description:
                - Ssl protocols to be disabled on application gateway.
              returned: always
              type: str
              sample: null
            policy_type:
              description:
                - Type of Ssl Policy.
              returned: always
              type: str
              sample: null
            policy_name:
              description:
                - Name of Ssl predefined policy.
              returned: always
              type: str
              sample: null
            cipher_suites:
              description:
                - >-
                  Ssl cipher suites to be enabled in the specified order to
                  application gateway.
              returned: always
              type: str
              sample: null
            min_protocol_version:
              description:
                - >-
                  Minimum version of Ssl protocol to be supported on application
                  gateway.
              returned: always
              type: str
              sample: null
        operational_state:
          description:
            - Operational state of the application gateway resource.
          returned: always
          type: str
          sample: null
        gateway_ipconfigurations:
          description:
            - >-
              Subnets of the application gateway resource. For default limits,
              see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway IP configuration.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the IP configuration that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        authentication_certificates:
          description:
            - >-
              Authentication certificates of the application gateway resource.
              For default limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - >-
                  Properties of the application gateway authentication
                  certificate.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the authentication certificate that is unique within
                  an Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        trusted_root_certificates:
          description:
            - >-
              Trusted Root certificates of the application gateway resource. For
              default limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - >-
                  Properties of the application gateway trusted root
                  certificate.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the trusted root certificate that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        ssl_certificates:
          description:
            - >-
              SSL certificates of the application gateway resource. For default
              limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway SSL certificate.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the SSL certificate that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        frontend_ipconfigurations:
          description:
            - >-
              Frontend IP addresses of the application gateway resource. For
              default limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - >-
                  Properties of the application gateway frontend IP
                  configuration.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the frontend IP configuration that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        frontend_ports:
          description:
            - >-
              Frontend ports of the application gateway resource. For default
              limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway frontend port.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the frontend port that is unique within an Application
                  Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        probes:
          description:
            - Probes of the application gateway resource.
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
                - Properties of the application gateway probe.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the probe that is unique within an Application
                  Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        backend_address_pools:
          description:
            - >-
              Backend address pool of the application gateway resource. For
              default limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway backend address pool.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the backend address pool that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        backend_http_settings_collection:
          description:
            - >-
              Backend http settings of the application gateway resource. For
              default limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway backend HTTP settings.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the backend http settings that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        http_listeners:
          description:
            - >-
              Http listeners of the application gateway resource. For default
              limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway HTTP listener.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the HTTP listener that is unique within an Application
                  Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        url_path_maps:
          description:
            - >-
              URL path map of the application gateway resource. For default
              limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway URL path map.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the URL path map that is unique within an Application
                  Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        request_routing_rules:
          description:
            - Request routing rules of the application gateway resource.
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
                - Properties of the application gateway request routing rule.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the request routing rule that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        rewrite_rule_sets:
          description:
            - Rewrite rules for the application gateway resource.
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
                - Properties of the application gateway rewrite rule set.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the rewrite rule set that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
        redirect_configurations:
          description:
            - >-
              Redirect configurations of the application gateway resource. For
              default limits, see [Application Gateway
              limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).
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
                - Properties of the application gateway redirect configuration.
              returned: always
              type: dict
              sample: null
            name:
              description:
                - >-
                  Name of the redirect configuration that is unique within an
                  Application Gateway.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  A unique read-only string that changes whenever the resource
                  is updated.
              returned: always
              type: str
              sample: null
            type:
              description:
                - Type of the resource.
              returned: always
              type: str
              sample: null
        web_application_firewall_configuration:
          description:
            - Web application firewall configuration.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - Whether the web application firewall is enabled or not.
              returned: always
              type: boolean
              sample: null
            firewall_mode:
              description:
                - Web application firewall mode.
              returned: always
              type: str
              sample: null
            rule_set_type:
              description:
                - >-
                  The type of the web application firewall rule set. Possible
                  values are: 'OWASP'.
              returned: always
              type: str
              sample: null
            rule_set_version:
              description:
                - The version of the rule set type.
              returned: always
              type: str
              sample: null
            disabled_rule_groups:
              description:
                - The disabled rule groups.
              returned: always
              type: dict
              sample: null
            request_body_check:
              description:
                - Whether allow WAF to check request Body.
              returned: always
              type: boolean
              sample: null
            max_request_body_size:
              description:
                - Maximum request body size for WAF.
              returned: always
              type: number
              sample: null
            max_request_body_size_in_kb:
              description:
                - Maximum request body size in Kb for WAF.
              returned: always
              type: number
              sample: null
            file_upload_limit_in_mb:
              description:
                - Maximum file upload size in Mb for WAF.
              returned: always
              type: number
              sample: null
            exclusions:
              description:
                - The exclusion list.
              returned: always
              type: dict
              sample: null
        firewall_policy:
          description:
            - Reference of the FirewallPolicy resource.
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
        enable_http2:
          description:
            - Whether HTTP2 is enabled on the application gateway resource.
          returned: always
          type: boolean
          sample: null
        enable_fips:
          description:
            - Whether FIPS is enabled on the application gateway resource.
          returned: always
          type: boolean
          sample: null
        autoscale_configuration:
          description:
            - Autoscale Configuration.
          returned: always
          type: dict
          sample: null
          contains:
            min_capacity:
              description:
                - Lower bound on number of Application Gateway capacity.
              returned: always
              type: number
              sample: null
            max_capacity:
              description:
                - Upper bound on number of Application Gateway capacity.
              returned: always
              type: number
              sample: null
        resource_guid:
          description:
            - Resource GUID property of the application gateway resource.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              Provisioning state of the application gateway resource. Possible
              values are: 'Updating', 'Deleting', and 'Failed'.
          returned: always
          type: str
          sample: null
        custom_error_configurations:
          description:
            - Custom error configurations of the application gateway resource.
          returned: always
          type: dict
          sample: null
          contains:
            status_code:
              description:
                - Status code of the application gateway customer error.
              returned: always
              type: str
              sample: null
            custom_error_page_url:
              description:
                - Error page URL of the application gateway customer error.
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
        zones:
          description:
            - >-
              A list of availability zones denoting where the resource needs to
              come from.
          returned: always
          type: str
          sample: null
        identity:
          description:
            - 'The identity of the application gateway, if configured.'
          returned: always
          type: dict
          sample: null
          contains:
            principal_id:
              description:
                - >-
                  The principal id of the system assigned identity. This
                  property will only be provided for a system assigned identity.
              returned: always
              type: str
              sample: null
            tenant_id:
              description:
                - >-
                  The tenant id of the system assigned identity. This property
                  will only be provided for a system assigned identity.
              returned: always
              type: str
              sample: null
            type:
              description:
                - >-
                  The type of identity used for the resource. The type
                  'SystemAssigned, UserAssigned' includes both an implicitly
                  created identity and a set of user assigned identities. The
                  type 'None' will remove any identities from the virtual
                  machine.
              returned: always
              type: str
              sample: null
            user_assigned_identities:
              description:
                - >-
                  The list of user identities associated with resource. The user
                  identity dictionary key references will be ARM resource ids in
                  the form:
                  '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
              returned: always
              type: >-
                unknown[DictionaryType
                {"$id":"3130","$type":"DictionaryType","valueType":{"$ref":"3087"},"supportsAdditionalProperties":false,"name":{"$id":"3131","fixed":false},"deprecated":false}]
              sample: null
    provisioning_state:
      description:
        - Provisioning state of the WebApplicationFirewallPolicy.
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status of the policy.
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


class AzureRMWebApplicationFirewallPolicies(AzureRMModuleBaseExt):
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
                disposition='policyName',
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
            policy_settings=dict(
                type='dict',
                disposition='/properties/policySettings',
                options=dict(
                    enabled_state=dict(
                        type='str',
                        disposition='enabledState',
                        choices=['Disabled',
                                 'Enabled']
                    ),
                    mode=dict(
                        type='str',
                        choices=['Prevention',
                                 'Detection']
                    )
                )
            ),
            custom_rules=dict(
                type='list',
                disposition='/properties/customRules',
                options=dict(
                    name=dict(
                        type='str'
                    ),
                    priority=dict(
                        type='number',
                        required=true
                    ),
                    rule_type=dict(
                        type='str',
                        disposition='ruleType',
                        choices=['MatchRule',
                                 'Invalid'],
                        required=true
                    ),
                    match_conditions=dict(
                        type='list',
                        disposition='matchConditions',
                        required=true,
                        options=dict(
                            match_variables=dict(
                                type='list',
                                disposition='matchVariables',
                                required=true,
                                options=dict(
                                    variable_name=dict(
                                        type='str',
                                        disposition='variableName',
                                        choices=['RemoteAddr',
                                                 'RequestMethod',
                                                 'QueryString',
                                                 'PostArgs',
                                                 'RequestUri',
                                                 'RequestHeaders',
                                                 'RequestBody',
                                                 'RequestCookies'],
                                        required=true
                                    ),
                                    selector=dict(
                                        type='str'
                                    )
                                )
                            ),
                            operator=dict(
                                type='str',
                                choices=['IPMatch',
                                         'Equal',
                                         'Contains',
                                         'LessThan',
                                         'GreaterThan',
                                         'LessThanOrEqual',
                                         'GreaterThanOrEqual',
                                         'BeginsWith',
                                         'EndsWith',
                                         'Regex'],
                                required=true
                            ),
                            negation_conditon=dict(
                                type='boolean',
                                disposition='negationConditon'
                            ),
                            match_values=dict(
                                type='list',
                                disposition='matchValues',
                                required=true
                            ),
                            transforms=dict(
                                type='list',
                                choices=['Lowercase',
                                         'Trim',
                                         'UrlDecode',
                                         'UrlEncode',
                                         'RemoveNulls',
                                         'HtmlEntityDecode']
                            )
                        )
                    ),
                    action=dict(
                        type='str',
                        choices=['Allow',
                                 'Block',
                                 'Log'],
                        required=true
                    )
                )
            ),
            etag=dict(
                type='str',
                updatable=False,
                disposition='/'
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

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMWebApplicationFirewallPolicies, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/ApplicationGatewayWebApplicationFirewallPolicies' +
                    '/{{ application_gateway_web_application_firewall_policy_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ application_gateway_web_application_firewall_policy_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("WebApplicationFirewallPolicy instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('WebApplicationFirewallPolicy instance already exists')

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
            self.log('Need to Create / Update the WebApplicationFirewallPolicy instance')

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
            self.log('WebApplicationFirewallPolicy instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('WebApplicationFirewallPolicy instance unchanged')
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
        # self.log('Creating / Updating the WebApplicationFirewallPolicy instance {0}'.format(self.))

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
            self.log('Error attempting to create the WebApplicationFirewallPolicy instance.')
            self.fail('Error creating the WebApplicationFirewallPolicy instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the WebApplicationFirewallPolicy instance {0}'.format(self.))
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
            self.log('Error attempting to delete the WebApplicationFirewallPolicy instance.')
            self.fail('Error deleting the WebApplicationFirewallPolicy instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the WebApplicationFirewallPolicy instance {0} is present'.format(self.))
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
            # self.log("WebApplicationFirewallPolicy instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the WebApplicationFirewallPolicy instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMWebApplicationFirewallPolicies()


if __name__ == '__main__':
    main()
