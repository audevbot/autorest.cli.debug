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
module: azure_rm_apimanagementproductapi_info
version_added: '2.9'
short_description: Get ProductApi info.
description:
  - Get info of ProductApi.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
  value:
    description:
      - Page values.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      name:
        description:
          - Resource name.
      type:
        description:
          - Type of API.
      description:
        description:
          - Description of the API. May include HTML formatting tags.
      authentication_settings:
        description:
          - Collection of authentication settings included into this API.
        suboptions:
          o_auth2:
            description:
              - OAuth2 Authentication settings
            suboptions:
              authorization_server_id:
                description:
                  - OAuth authorization server identifier.
              scope:
                description:
                  - operations scope.
          openid:
            description:
              - OpenID Connect Authentication Settings
            suboptions:
              openid_provider_id:
                description:
                  - OAuth authorization server identifier.
              bearer_token_sending_methods:
                description:
                  - How to send token to the server.
                type: list
          subscription_key_required:
            description:
              - >-
                Specifies whether subscription key is required during call to
                this API, true - API is included into closed products only,
                false - API is included into open products alone, null - there
                is a mix of products.
      subscription_key_parameter_names:
        description:
          - Protocols over which API is made available.
        suboptions:
          header:
            description:
              - Subscription key header name.
          query:
            description:
              - Subscription key query string parameter name.
      api_revision:
        description:
          - >-
            Describes the Revision of the Api. If no value is provided, default
            revision 1 is created
      api_version:
        description:
          - Indicates the Version identifier of the API if the API is versioned
      is_current:
        description:
          - Indicates if API revision is current api revision.
      is_online:
        description:
          - Indicates if API revision is accessible via the gateway.
      api_revision_description:
        description:
          - Description of the Api Revision.
      api_version_description:
        description:
          - Description of the Api Version.
      api_version_set_id:
        description:
          - A resource identifier for the related ApiVersionSet.
      subscription_required:
        description:
          - >-
            Specifies whether an API or Product subscription is required for
            accessing the API.
      source_api_id:
        description:
          - API identifier of the source API.
      display_name:
        description:
          - API name. Must be 1 to 300 characters long.
      service_url:
        description:
          - >-
            Absolute URL of the backend service implementing this API. Cannot be
            more than 2000 characters long.
      path:
        description:
          - >-
            Relative URL uniquely identifying this API and all of its resource
            paths within the API Management service instance. It is appended to
            the API endpoint base URL specified during the service instance
            creation to form a public URL for this API.
        required: true
      protocols:
        description:
          - >-
            Describes on which protocols the operations in this API can be
            invoked.
        type: list
      api_version_set:
        description:
          - Version set details
        suboptions:
          id:
            description:
              - >-
                Identifier for existing API Version Set. Omit this value to
                create a new Version Set.
          name:
            description:
              - The display Name of the API Version Set.
          description:
            description:
              - Description of API Version Set.
          versioning_scheme:
            description:
              - >-
                An value that determines where the API Version identifer will be
                located in a HTTP request.
          version_query_name:
            description:
              - >-
                Name of query parameter that indicates the API Version if
                versioningScheme is set to `query`.
          version_header_name:
            description:
              - >-
                Name of HTTP header parameter that indicates the API Version if
                versioningScheme is set to `header`.
  next_link:
    description:
      - Next page link if any.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListProductApis
  azure_rm_apimanagementproductapi_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct

'''

RETURN = '''
product_api:
  description: >-
    A list of dict results where the key is the name of the ProductApi and the
    values are the facts for that ProductApi.
  returned: always
  type: complex
  contains:
    productapi_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Page values.
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
                - Type of API.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Api entity contract properties.
              returned: always
              type: dict
              sample: null
            description:
              description:
                - Description of the API. May include HTML formatting tags.
              returned: always
              type: str
              sample: null
            authentication_settings:
              description:
                - Collection of authentication settings included into this API.
              returned: always
              type: dict
              sample: null
              contains:
                o_auth2:
                  description:
                    - OAuth2 Authentication settings
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    authorization_server_id:
                      description:
                        - OAuth authorization server identifier.
                      returned: always
                      type: str
                      sample: null
                    scope:
                      description:
                        - operations scope.
                      returned: always
                      type: str
                      sample: null
                openid:
                  description:
                    - OpenID Connect Authentication Settings
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    openid_provider_id:
                      description:
                        - OAuth authorization server identifier.
                      returned: always
                      type: str
                      sample: null
                    bearer_token_sending_methods:
                      description:
                        - How to send token to the server.
                      returned: always
                      type: str
                      sample: null
                subscription_key_required:
                  description:
                    - >-
                      Specifies whether subscription key is required during call
                      to this API, true - API is included into closed products
                      only, false - API is included into open products alone,
                      null - there is a mix of products.
                  returned: always
                  type: boolean
                  sample: null
            subscription_key_parameter_names:
              description:
                - Protocols over which API is made available.
              returned: always
              type: dict
              sample: null
              contains:
                header:
                  description:
                    - Subscription key header name.
                  returned: always
                  type: str
                  sample: null
                query:
                  description:
                    - Subscription key query string parameter name.
                  returned: always
                  type: str
                  sample: null
            api_revision:
              description:
                - >-
                  Describes the Revision of the Api. If no value is provided,
                  default revision 1 is created
              returned: always
              type: str
              sample: null
            api_version:
              description:
                - >-
                  Indicates the Version identifier of the API if the API is
                  versioned
              returned: always
              type: str
              sample: null
            is_current:
              description:
                - Indicates if API revision is current api revision.
              returned: always
              type: boolean
              sample: null
            is_online:
              description:
                - Indicates if API revision is accessible via the gateway.
              returned: always
              type: boolean
              sample: null
            api_revision_description:
              description:
                - Description of the Api Revision.
              returned: always
              type: str
              sample: null
            api_version_description:
              description:
                - Description of the Api Version.
              returned: always
              type: str
              sample: null
            api_version_set_id:
              description:
                - A resource identifier for the related ApiVersionSet.
              returned: always
              type: str
              sample: null
            subscription_required:
              description:
                - >-
                  Specifies whether an API or Product subscription is required
                  for accessing the API.
              returned: always
              type: boolean
              sample: null
            source_api_id:
              description:
                - API identifier of the source API.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - API name. Must be 1 to 300 characters long.
              returned: always
              type: str
              sample: null
            service_url:
              description:
                - >-
                  Absolute URL of the backend service implementing this API.
                  Cannot be more than 2000 characters long.
              returned: always
              type: str
              sample: null
            path:
              description:
                - >-
                  Relative URL uniquely identifying this API and all of its
                  resource paths within the API Management service instance. It
                  is appended to the API endpoint base URL specified during the
                  service instance creation to form a public URL for this API.
              returned: always
              type: str
              sample: null
            protocols:
              description:
                - >-
                  Describes on which protocols the operations in this API can be
                  invoked.
              returned: always
              type: str
              sample: null
            api_version_set:
              description:
                - Version set details
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - >-
                      Identifier for existing API Version Set. Omit this value
                      to create a new Version Set.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The display Name of the API Version Set.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of API Version Set.
                  returned: always
                  type: str
                  sample: null
                versioning_scheme:
                  description:
                    - >-
                      An value that determines where the API Version identifer
                      will be located in a HTTP request.
                  returned: always
                  type: str
                  sample: null
                version_query_name:
                  description:
                    - >-
                      Name of query parameter that indicates the API Version if
                      versioningScheme is set to `query`.
                  returned: always
                  type: str
                  sample: null
                version_header_name:
                  description:
                    - >-
                      Name of HTTP header parameter that indicates the API
                      Version if versioningScheme is set to `header`.
                  returned: always
                  type: str
                  sample: null
        next_link:
          description:
            - Next page link if any.
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMProductApiInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            service_name=dict(
                type='str',
                required=true
            ),
            product_id=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.product_id = None
        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMProductApiInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.product_id is not None):
            self.results['product_api'] = self.format_item(self.listbyproduct())
        return self.results

    def listbyproduct(self):
        response = None

        try:
            response = self.mgmt_client.product_api.list_by_product(resource_group_name=self.resource_group,
                                                                    service_name=self.service_name,
                                                                    product_id=self.product_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMProductApiInfo()


if __name__ == '__main__':
    main()
