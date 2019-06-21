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
module: azure_rm_apimanagementservice
version_added: '2.9'
short_description: Manage Azure ApiManagementService instance.
description:
  - 'Create, update and delete instance of Azure ApiManagementService.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  notification_sender_email:
    description:
      - Email address from which the notification will be sent.
  hostname_configurations:
    description:
      - Custom hostname configuration of the API Management service.
    type: list
    suboptions:
      type:
        description:
          - Hostname type.
        required: true
      host_name:
        description:
          - Hostname to configure on the Api Management service.
        required: true
      key_vault_id:
        description:
          - >-
            Url to the KeyVault Secret containing the Ssl Certificate. If
            absolute Url containing version is provided, auto-update of ssl
            certificate will not work. This requires Api Management service to
            be configured with MSI. The secret should be of type
            *application/x-pkcs12*
      encoded_certificate:
        description:
          - Base64 Encoded certificate.
      certificate_password:
        description:
          - Certificate Password.
      default_ssl_binding:
        description:
          - >-
            Specify true to setup the certificate associated with this Hostname
            as the Default SSL Certificate. If a client does not send the SNI
            header, then this will be the certificate that will be challenged.
            The property is useful if a service has multiple custom hostname
            enabled and it needs to decide on the default ssl certificate. The
            setting only applied to Proxy Hostname Type.
      negotiate_client_certificate:
        description:
          - >-
            Specify true to always negotiate client certificate on the hostname.
            Default Value is false.
      certificate:
        description:
          - Certificate information.
        suboptions:
          expiry:
            description:
              - >-
                Expiration date of the certificate. The date conforms to the
                following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
                8601 standard.
            required: true
          thumbprint:
            description:
              - Thumbprint of the certificate.
            required: true
          subject:
            description:
              - Subject of the certificate.
            required: true
  virtual_network_configuration:
    description:
      - Virtual network configuration of the API Management service.
    suboptions:
      subnet_resource_id:
        description:
          - >-
            The full resource ID of a subnet in a virtual network to deploy the
            API Management service in.
      vnetid:
        description:
          - >-
            The virtual network ID. This is typically a GUID. Expect a null GUID
            by default.
      subnetname:
        description:
          - The name of the subnet.
  additional_locations:
    description:
      - Additional datacenter locations of the API Management service.
    type: list
    suboptions:
      location:
        description:
          - >-
            The location name of the additional region among Azure Data center
            regions.
        required: true
      sku:
        description:
          - SKU properties of the API Management service.
        required: true
        suboptions:
          name:
            description:
              - Name of the Sku.
            required: true
          capacity:
            description:
              - Capacity of the SKU (number of deployed units of the SKU).
      virtual_network_configuration:
        description:
          - Virtual network configuration for the location.
        suboptions:
          subnet_resource_id:
            description:
              - >-
                The full resource ID of a subnet in a virtual network to deploy
                the API Management service in.
          vnetid:
            description:
              - >-
                The virtual network ID. This is typically a GUID. Expect a null
                GUID by default.
          subnetname:
            description:
              - The name of the subnet.
      public_ip_addresses:
        description:
          - >-
            Public Static Load Balanced IP addresses of the API Management
            service in the additional location. Available only for Basic,
            Standard and Premium SKU.
        type: list
      private_ip_addresses:
        description:
          - >-
            Private Static Load Balanced IP addresses of the API Management
            service which is deployed in an Internal Virtual Network in a
            particular additional location. Available only for Basic, Standard
            and Premium SKU.
        type: list
      gateway_regional_url:
        description:
          - Gateway URL of the API Management service in the Region.
  custom_properties:
    description:
      - >-
        Custom properties of the API Management service.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168`
        will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0,
        1.1 and 1.2).</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11`
        can be used to disable just TLS 1.1.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10`
        can be used to disable TLS 1.0 on an API Management service.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11`
        can be used to disable just TLS 1.1 for communications with
        backends.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10`
        can be used to disable TLS 1.0 for communications with
        backends.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2`
        can be used to enable HTTP2 protocol on an API Management
        service.</br>Not specifying any of these properties on PATCH operation
        will reset omitted properties' values to their defaults. For all the
        settings except Http2 the default value is `True` if the service was
        created on or before April 1st 2018 and `False` otherwise. Http2
        setting's default value is `False`.
  certificates:
    description:
      - >-
        List of Certificates that need to be installed in the API Management
        service. Max supported certificates that can be installed is 10.
    type: list
    suboptions:
      encoded_certificate:
        description:
          - Base64 Encoded certificate.
      certificate_password:
        description:
          - Certificate Password.
      store_name:
        description:
          - >-
            The System.Security.Cryptography.x509certificates.StoreName
            certificate store location. Only Root and CertificateAuthority are
            valid locations.
        required: true
      certificate:
        description:
          - Certificate information.
        suboptions:
          expiry:
            description:
              - >-
                Expiration date of the certificate. The date conforms to the
                following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
                8601 standard.
            required: true
          thumbprint:
            description:
              - Thumbprint of the certificate.
            required: true
          subject:
            description:
              - Subject of the certificate.
            required: true
  enable_client_certificate:
    description:
      - >-
        Property only meant to be used for Consumption SKU Service. This
        enforces a client certificate to be presented on each request to the
        gateway. This also enables the ability to authenticate the certificate
        in the policy on the gateway.
  virtual_network_type:
    description:
      - >-
        The type of VPN in which API Management service needs to be configured
        in. None (Default Value) means the API Management service is not part of
        any Virtual Network, External means the API Management deployment is set
        up inside a Virtual Network having an Internet Facing Endpoint, and
        Internal means that API Management deployment is setup inside a Virtual
        Network having an Intranet Facing Endpoint only.
  publisher_email:
    description:
      - Publisher email.
    required: true
  publisher_name:
    description:
      - Publisher name.
    required: true
  provisioning_state:
    description:
      - >-
        The current provisioning state of the API Management service which can
        be one of the following:
        Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.
  target_provisioning_state:
    description:
      - >-
        The provisioning state of the API Management service, which is targeted
        by the long running operation started on the service.
  created_at_utc:
    description:
      - >-
        Creation UTC date of the API Management service.The date conforms to the
        following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.
  gateway_url:
    description:
      - Gateway URL of the API Management service.
  gateway_regional_url:
    description:
      - Gateway URL of the API Management service in the Default Region.
  portal_url:
    description:
      - Publisher portal endpoint Url of the API Management service.
  management_api_url:
    description:
      - Management API endpoint URL of the API Management service.
  scm_url:
    description:
      - SCM endpoint URL of the API Management service.
  public_ip_addresses:
    description:
      - >-
        Public Static Load Balanced IP addresses of the API Management service
        in Primary region. Available only for Basic, Standard and Premium SKU.
    type: list
  private_ip_addresses:
    description:
      - >-
        Private Static Load Balanced IP addresses of the API Management service
        in Primary region which is deployed in an Internal Virtual Network.
        Available only for Basic, Standard and Premium SKU.
    type: list
  sku:
    description:
      - SKU properties of the API Management service.
    required: true
    suboptions:
      name:
        description:
          - Name of the Sku.
        required: true
      capacity:
        description:
          - Capacity of the SKU (number of deployed units of the SKU).
  identity:
    description:
      - Managed service identity of the Api Management service.
    suboptions:
      type:
        description:
          - >-
            The identity type. Currently the only supported type is
            'SystemAssigned'.
        required: true
      principal_id:
        description:
          - The principal id of the identity.
      tenant_id:
        description:
          - The client tenant id of the identity.
  location:
    description:
      - Resource location.
    required: true
  id:
    description:
      - Resource ID.
  type:
    description:
      - >-
        Resource type for API Management resource is set to
        Microsoft.ApiManagement.
  etag:
    description:
      - ETag of the resource.
  state:
    description:
      - Assert the state of the ApiManagementService.
      - >-
        Use C(present) to create or update an ApiManagementService and C(absent)
        to delete it.
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
- name: ApiManagementCreateService
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
    tags:
      tag1: value1
      tag2: value2
      tag3: value3
    publisher_email: apim@autorestsdk.com
    publisher_name: autorestsdk
    sku:
      name: Developer
      capacity: '1'
    location: Central US
- name: ApiManagementCreateMultiRegionServiceWithCustomHostname
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
    hostname_configurations:
      - type: Proxy
        host_name: proxyhostname1.contoso.com
        encoded_certificate: '************Base 64 Encoded Pfx Certificate************************'
        certificate_password: >-
          **************Password of the
          Certificate************************************************
      - type: Proxy
        host_name: proxyhostname2.contoso.com
        encoded_certificate: '************Base 64 Encoded Pfx Certificate************************'
        certificate_password: >-
          **************Password of the
          Certificate************************************************
        negotiate_client_certificate: true
      - type: Portal
        host_name: portalhostname1.contoso.com
        encoded_certificate: '************Base 64 Encoded Pfx Certificate************************'
        certificate_password: >-
          **************Password of the
          Certificate************************************************
    virtual_network_configuration:
      subnet_resource_id: >-
        /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
        }}/providers/Microsoft.Network/virtualNetworks/{{ virtual_network_name
        }}/subnets/{{ subnet_name }}
    additional_locations:
      - location: North Europe
        sku:
          name: Premium
          capacity: '1'
        virtual_network_configuration:
          subnet_resource_id: >-
            /subscriptions/{{ subscription_id }}/resourceGroups/{{
            resource_group }}/providers/Microsoft.Network/virtualNetworks/{{
            virtual_network_name }}/subnets/{{ subnet_name }}
    virtual_network_type: External
    publisher_email: admin@live.com
    publisher_name: contoso
    sku:
      name: Premium
      capacity: '1'
    location: Central US
- name: ApiManagementCreateServiceHavingMsi
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
    tags:
      tag1: value1
      tag2: value2
      tag3: value3
    publisher_email: apim@autorestsdk.com
    publisher_name: autorestsdk
    sku:
      name: Consumption
    identity:
      type: SystemAssigned
    location: West US
- name: ApiManagementCreateServiceWithSystemCertificates
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
    tags:
      tag1: value1
      tag2: value2
      tag3: value3
    certificates:
      - encoded_certificate: '*******Base64 encoded Certificate******************'
        certificate_password: Password
        store_name: CertificateAuthority
    publisher_email: apim@autorestsdk.com
    publisher_name: autorestsdk
    sku:
      name: Basic
      capacity: '1'
    location: Central US
- name: ApiManagementUpdateServiceDisableTls10
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
    custom_properties:
      Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10: 'false'
- name: ApiManagementUpdateServicePublisherDetails
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
    publisher_email: foobar@live.com
    publisher_name: Contoso Vnext
- name: ApiManagementServiceDeleteService
  azure_rm_apimanagementservice:
    resource_group: myResourceGroup
    name: myService
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
    - >-
      Resource type for API Management resource is set to
      Microsoft.ApiManagement.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - Properties of the API Management service.
  returned: always
  type: dict
  sample: null
  contains:
    notification_sender_email:
      description:
        - Email address from which the notification will be sent.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          The current provisioning state of the API Management service which can
          be one of the following:
          Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.
      returned: always
      type: str
      sample: null
    target_provisioning_state:
      description:
        - >-
          The provisioning state of the API Management service, which is
          targeted by the long running operation started on the service.
      returned: always
      type: str
      sample: null
    created_at_utc:
      description:
        - >-
          Creation UTC date of the API Management service.The date conforms to
          the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
          8601 standard.
      returned: always
      type: datetime
      sample: null
    gateway_url:
      description:
        - Gateway URL of the API Management service.
      returned: always
      type: str
      sample: null
    gateway_regional_url:
      description:
        - Gateway URL of the API Management service in the Default Region.
      returned: always
      type: str
      sample: null
    portal_url:
      description:
        - Publisher portal endpoint Url of the API Management service.
      returned: always
      type: str
      sample: null
    management_api_url:
      description:
        - Management API endpoint URL of the API Management service.
      returned: always
      type: str
      sample: null
    scm_url:
      description:
        - SCM endpoint URL of the API Management service.
      returned: always
      type: str
      sample: null
    hostname_configurations:
      description:
        - Custom hostname configuration of the API Management service.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - Hostname type.
          returned: always
          type: str
          sample: null
        host_name:
          description:
            - Hostname to configure on the Api Management service.
          returned: always
          type: str
          sample: null
        key_vault_id:
          description:
            - >-
              Url to the KeyVault Secret containing the Ssl Certificate. If
              absolute Url containing version is provided, auto-update of ssl
              certificate will not work. This requires Api Management service to
              be configured with MSI. The secret should be of type
              *application/x-pkcs12*
          returned: always
          type: str
          sample: null
        encoded_certificate:
          description:
            - Base64 Encoded certificate.
          returned: always
          type: str
          sample: null
        certificate_password:
          description:
            - Certificate Password.
          returned: always
          type: str
          sample: null
        default_ssl_binding:
          description:
            - >-
              Specify true to setup the certificate associated with this
              Hostname as the Default SSL Certificate. If a client does not send
              the SNI header, then this will be the certificate that will be
              challenged. The property is useful if a service has multiple
              custom hostname enabled and it needs to decide on the default ssl
              certificate. The setting only applied to Proxy Hostname Type.
          returned: always
          type: boolean
          sample: null
        negotiate_client_certificate:
          description:
            - >-
              Specify true to always negotiate client certificate on the
              hostname. Default Value is false.
          returned: always
          type: boolean
          sample: null
        certificate:
          description:
            - Certificate information.
          returned: always
          type: dict
          sample: null
          contains:
            expiry:
              description:
                - >-
                  Expiration date of the certificate. The date conforms to the
                  following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the
                  ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            thumbprint:
              description:
                - Thumbprint of the certificate.
              returned: always
              type: str
              sample: null
            subject:
              description:
                - Subject of the certificate.
              returned: always
              type: str
              sample: null
    public_ip_addresses:
      description:
        - >-
          Public Static Load Balanced IP addresses of the API Management service
          in Primary region. Available only for Basic, Standard and Premium SKU.
      returned: always
      type: str
      sample: null
    private_ip_addresses:
      description:
        - >-
          Private Static Load Balanced IP addresses of the API Management
          service in Primary region which is deployed in an Internal Virtual
          Network. Available only for Basic, Standard and Premium SKU.
      returned: always
      type: str
      sample: null
    virtual_network_configuration:
      description:
        - Virtual network configuration of the API Management service.
      returned: always
      type: dict
      sample: null
      contains:
        vnetid:
          description:
            - >-
              The virtual network ID. This is typically a GUID. Expect a null
              GUID by default.
          returned: always
          type: str
          sample: null
        subnetname:
          description:
            - The name of the subnet.
          returned: always
          type: str
          sample: null
        subnet_resource_id:
          description:
            - >-
              The full resource ID of a subnet in a virtual network to deploy
              the API Management service in.
          returned: always
          type: str
          sample: null
    additional_locations:
      description:
        - Additional datacenter locations of the API Management service.
      returned: always
      type: dict
      sample: null
      contains:
        location:
          description:
            - >-
              The location name of the additional region among Azure Data center
              regions.
          returned: always
          type: str
          sample: null
        sku:
          description:
            - SKU properties of the API Management service.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the Sku.
              returned: always
              type: str
              sample: null
            capacity:
              description:
                - Capacity of the SKU (number of deployed units of the SKU).
              returned: always
              type: number
              sample: null
        public_ip_addresses:
          description:
            - >-
              Public Static Load Balanced IP addresses of the API Management
              service in the additional location. Available only for Basic,
              Standard and Premium SKU.
          returned: always
          type: str
          sample: null
        private_ip_addresses:
          description:
            - >-
              Private Static Load Balanced IP addresses of the API Management
              service which is deployed in an Internal Virtual Network in a
              particular additional location. Available only for Basic, Standard
              and Premium SKU.
          returned: always
          type: str
          sample: null
        virtual_network_configuration:
          description:
            - Virtual network configuration for the location.
          returned: always
          type: dict
          sample: null
          contains:
            vnetid:
              description:
                - >-
                  The virtual network ID. This is typically a GUID. Expect a
                  null GUID by default.
              returned: always
              type: str
              sample: null
            subnetname:
              description:
                - The name of the subnet.
              returned: always
              type: str
              sample: null
            subnet_resource_id:
              description:
                - >-
                  The full resource ID of a subnet in a virtual network to
                  deploy the API Management service in.
              returned: always
              type: str
              sample: null
        gateway_regional_url:
          description:
            - Gateway URL of the API Management service in the Region.
          returned: always
          type: str
          sample: null
    custom_properties:
      description:
        - >-
          Custom properties of the API Management service.</br>Setting
          `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168`
          will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0,
          1.1 and 1.2).</br>Setting
          `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11`
          can be used to disable just TLS 1.1.</br>Setting
          `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10`
          can be used to disable TLS 1.0 on an API Management
          service.</br>Setting
          `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11`
          can be used to disable just TLS 1.1 for communications with
          backends.</br>Setting
          `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10`
          can be used to disable TLS 1.0 for communications with
          backends.</br>Setting
          `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2`
          can be used to enable HTTP2 protocol on an API Management
          service.</br>Not specifying any of these properties on PATCH operation
          will reset omitted properties' values to their defaults. For all the
          settings except Http2 the default value is `True` if the service was
          created on or before April 1st 2018 and `False` otherwise. Http2
          setting's default value is `False`.
      returned: always
      type: >-
        unknown[DictionaryType
        {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]
      sample: null
    certificates:
      description:
        - >-
          List of Certificates that need to be installed in the API Management
          service. Max supported certificates that can be installed is 10.
      returned: always
      type: dict
      sample: null
      contains:
        encoded_certificate:
          description:
            - Base64 Encoded certificate.
          returned: always
          type: str
          sample: null
        certificate_password:
          description:
            - Certificate Password.
          returned: always
          type: str
          sample: null
        store_name:
          description:
            - >-
              The System.Security.Cryptography.x509certificates.StoreName
              certificate store location. Only Root and CertificateAuthority are
              valid locations.
          returned: always
          type: str
          sample: null
        certificate:
          description:
            - Certificate information.
          returned: always
          type: dict
          sample: null
          contains:
            expiry:
              description:
                - >-
                  Expiration date of the certificate. The date conforms to the
                  following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the
                  ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            thumbprint:
              description:
                - Thumbprint of the certificate.
              returned: always
              type: str
              sample: null
            subject:
              description:
                - Subject of the certificate.
              returned: always
              type: str
              sample: null
    enable_client_certificate:
      description:
        - >-
          Property only meant to be used for Consumption SKU Service. This
          enforces a client certificate to be presented on each request to the
          gateway. This also enables the ability to authenticate the certificate
          in the policy on the gateway.
      returned: always
      type: boolean
      sample: null
    virtual_network_type:
      description:
        - >-
          The type of VPN in which API Management service needs to be configured
          in. None (Default Value) means the API Management service is not part
          of any Virtual Network, External means the API Management deployment
          is set up inside a Virtual Network having an Internet Facing Endpoint,
          and Internal means that API Management deployment is setup inside a
          Virtual Network having an Intranet Facing Endpoint only.
      returned: always
      type: str
      sample: null
    publisher_email:
      description:
        - Publisher email.
      returned: always
      type: str
      sample: null
    publisher_name:
      description:
        - Publisher name.
      returned: always
      type: str
      sample: null
sku:
  description:
    - SKU properties of the API Management service.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of the Sku.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - Capacity of the SKU (number of deployed units of the SKU).
      returned: always
      type: number
      sample: null
identity:
  description:
    - Managed service identity of the Api Management service.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - >-
          The identity type. Currently the only supported type is
          'SystemAssigned'.
      returned: always
      type: str
      sample: null
    principal_id:
      description:
        - The principal id of the identity.
      returned: always
      type: 'unknown-primary[uuid]'
      sample: null
    tenant_id:
      description:
        - The client tenant id of the identity.
      returned: always
      type: 'unknown-primary[uuid]'
      sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
etag:
  description:
    - ETag of the resource.
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
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApiManagementService(AzureRMModuleBaseExt):
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
                disposition='serviceName',
                required=true
            ),
            notification_sender_email=dict(
                type='str',
                disposition='/properties/notificationSenderEmail'
            ),
            hostname_configurations=dict(
                type='list',
                disposition='/properties/hostnameConfigurations',
                options=dict(
                    type=dict(
                        type='str',
                        choices=['Proxy',
                                 'Portal',
                                 'Management',
                                 'Scm',
                                 'DeveloperPortal'],
                        required=true
                    ),
                    host_name=dict(
                        type='str',
                        disposition='hostName',
                        required=true
                    ),
                    key_vault_id=dict(
                        type='str',
                        disposition='keyVaultId'
                    ),
                    encoded_certificate=dict(
                        type='str',
                        disposition='encodedCertificate'
                    ),
                    certificate_password=dict(
                        type='str',
                        disposition='certificatePassword'
                    ),
                    default_ssl_binding=dict(
                        type='boolean',
                        disposition='defaultSslBinding'
                    ),
                    negotiate_client_certificate=dict(
                        type='boolean',
                        disposition='negotiateClientCertificate'
                    ),
                    certificate=dict(
                        type='dict',
                        options=dict(
                            expiry=dict(
                                type='datetime',
                                required=true
                            ),
                            thumbprint=dict(
                                type='str',
                                required=true
                            ),
                            subject=dict(
                                type='str',
                                required=true
                            )
                        )
                    )
                )
            ),
            virtual_network_configuration=dict(
                type='dict',
                disposition='/properties/virtualNetworkConfiguration',
                options=dict(
                    subnet_resource_id=dict(
                        type='raw',
                        disposition='subnetResourceId',
                        pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                                 '/{{ resource_group }}/providers/Microsoft.Network'
                                 '/virtualNetworks/{{ virtual_network_name }}/subnets'
                                 '/{{ name }}')
                    )
                )
            ),
            additional_locations=dict(
                type='list',
                disposition='/properties/additionalLocations',
                options=dict(
                    location=dict(
                        type='str',
                        updatable=False,
                        required=true
                    ),
                    sku=dict(
                        type='dict',
                        required=true,
                        options=dict(
                            name=dict(
                                type='str',
                                choices=['Developer',
                                         'Standard',
                                         'Premium',
                                         'Basic',
                                         'Consumption'],
                                required=true
                            ),
                            capacity=dict(
                                type='number'
                            )
                        )
                    ),
                    virtual_network_configuration=dict(
                        type='dict',
                        disposition='virtualNetworkConfiguration',
                        options=dict(
                            subnet_resource_id=dict(
                                type='raw',
                                disposition='subnetResourceId',
                                pattern=('//subscriptions/{{ subscription_id }}'
                                         '/resourceGroups/{{ resource_group }}/providers'
                                         '/Microsoft.Network/virtualNetworks'
                                         '/{{ virtual_network_name }}/subnets/{{ name }}')
                            )
                        )
                    )
                )
            ),
            custom_properties=dict(
                type='unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]',
                disposition='/properties/customProperties'
            ),
            certificates=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    encoded_certificate=dict(
                        type='str',
                        disposition='encodedCertificate'
                    ),
                    certificate_password=dict(
                        type='str',
                        disposition='certificatePassword'
                    ),
                    store_name=dict(
                        type='str',
                        disposition='storeName',
                        choices=['CertificateAuthority',
                                 'Root'],
                        required=true
                    ),
                    certificate=dict(
                        type='dict',
                        options=dict(
                            expiry=dict(
                                type='datetime',
                                required=true
                            ),
                            thumbprint=dict(
                                type='str',
                                required=true
                            ),
                            subject=dict(
                                type='str',
                                required=true
                            )
                        )
                    )
                )
            ),
            enable_client_certificate=dict(
                type='boolean',
                disposition='/properties/enableClientCertificate'
            ),
            virtual_network_type=dict(
                type='str',
                disposition='/properties/virtualNetworkType',
                choices=['None',
                         'External',
                         'Internal']
            ),
            publisher_email=dict(
                type='str',
                disposition='/properties/publisherEmail',
                required=true
            ),
            publisher_name=dict(
                type='str',
                disposition='/properties/publisherName',
                required=true
            ),
            sku=dict(
                type='dict',
                disposition='/',
                required=true,
                options=dict(
                    name=dict(
                        type='str',
                        choices=['Developer',
                                 'Standard',
                                 'Premium',
                                 'Basic',
                                 'Consumption'],
                        required=true
                    ),
                    capacity=dict(
                        type='number'
                    )
                )
            ),
            identity=dict(
                type='dict',
                disposition='/',
                options=dict(
                    type=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
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
        self.etag = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMApiManagementService, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ApiManagementService instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ApiManagementService instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ApiManagementService instance')

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
            self.log('ApiManagementService instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ApiManagementService instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]
           self.results["sku"] = response["sku"]
           self.results["identity"] = response["identity"]
           self.results["location"] = response["location"]
           self.results["etag"] = response["etag"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ApiManagementService instance {0}'.format(self.))

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
            self.log('Error attempting to create the ApiManagementService instance.')
            self.fail('Error creating the ApiManagementService instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ApiManagementService instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ApiManagementService instance.')
            self.fail('Error deleting the ApiManagementService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiManagementService instance {0} is present'.format(self.))
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
            # self.log("ApiManagementService instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApiManagementService instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMApiManagementService()


if __name__ == '__main__':
    main()
