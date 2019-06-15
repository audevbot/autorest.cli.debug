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
module: azure_rm_apimanagementapi
version_added: '2.9'
short_description: Manage Azure Api instance.
description:
  - 'Create, update and delete instance of Azure Api.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
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
            Specifies whether subscription key is required during call to this
            API, true - API is included into closed products only, false - API
            is included into open products alone, null - there is a mix of
            products.
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
  type:
    description:
      - Resource type for API Management resource.
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
        Relative URL uniquely identifying this API and all of its resource paths
        within the API Management service instance. It is appended to the API
        endpoint base URL specified during the service instance creation to form
        a public URL for this API.
    required: true
  protocols:
    description:
      - Describes on which protocols the operations in this API can be invoked.
    type: list
  api_version_set:
    description:
      - Version set details
    suboptions:
      id:
        description:
          - >-
            Identifier for existing API Version Set. Omit this value to create a
            new Version Set.
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
  value:
    description:
      - Content value when Importing an API.
  format:
    description:
      - Format of the Content in which the API is getting imported.
  wsdl_selector:
    description:
      - Criteria to limit import of WSDL to a subset of the document.
    suboptions:
      wsdl_service_name:
        description:
          - Name of service to import from WSDL
      wsdl_endpoint_name:
        description:
          - Name of endpoint(port) to import from WSDL
  api_type:
    description:
      - 'Type of Api to create. '
      - ' * `http` creates a SOAP to REST API '
      - ' * `soap` creates a SOAP pass-through API .'
  is_online:
    description:
      - Indicates if API revision is accessible via the gateway.
  id:
    description:
      - Resource ID.
  state:
    description:
      - Assert the state of the Api.
      - Use C(present) to create or update an Api and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateApiUsingOai3Import
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    path: petstore
    value: >-
      https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml
    format: openapi-link
- name: ApiManagementCreateApiUsingSwaggerImport
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    path: petstore
    value: 'http://petstore.swagger.io/v2/swagger.json'
    format: swagger-link-json
- name: ApiManagementCreateApiUsingWadlImport
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    path: collector
    value: >-
      https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl
    format: wadl-link-json
- name: ApiManagementCreateSoapToRestApiUsingWsdlImport
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    path: currency
    value: 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
    format: wsdl-link
    wsdl_selector:
      wsdl_service_name: CurrencyConvertor
      wsdl_endpoint_name: CurrencyConvertorSoap
- name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    path: currency
    value: 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
    format: wsdl-link
    wsdl_selector:
      wsdl_service_name: CurrencyConvertor
      wsdl_endpoint_name: CurrencyConvertorSoap
    api_type: soap
- name: ApiManagementCreateApi
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    description: apidescription5200
    authentication_settings:
      o_auth2:
        authorization_server_id: authorizationServerId2283
        scope: oauth2scope2580
    subscription_key_parameter_names:
      header: header4520
      query: query3037
    display_name: apiname1463
    service_url: 'http://newechoapi.cloudapp.net/api'
    path: newapiPath
    protocols:
      - https
      - http
- name: ApiManagementCreateApiRevisionFromExistingApi
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    api_revision_description: Creating a Revision of an existing API
    source_api_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{
      apis_name }}
    service_url: 'http://echoapi.cloudapp.net/apiv3'
    path: echo
- name: ApiManagementCreateApiNewVersionUsingExistingApi
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    description: >-
      Create Echo API into a new Version using Existing Version Set and Copy all
      Operations.
    api_version: v4
    is_current: true
    api_version_set_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name
      }}/apiVersionSets/{{ api_version_set_name }}
    subscription_required: true
    source_api_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{
      apis_name }}
    display_name: Echo API2
    service_url: 'http://echoapi.cloudapp.net/api'
    path: echo2
    protocols:
      - http
      - https
- name: ApiManagementCreateApiClone
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    description: Copy of Existing Echo Api including Operations.
    is_current: true
    subscription_required: true
    source_api_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{
      apis_name }}
    display_name: Echo API2
    service_url: 'http://echoapi.cloudapp.net/api'
    path: echo2
    protocols:
      - http
      - https
- name: ApiManagementCreateApiWithOpenIdConnect
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    description: >-
      This is a sample server Petstore server.  You can find out more about
      Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net,
      #swagger](http://swagger.io/irc/).  For this sample, you can use the api
      key `special-key` to test the authorization filters.
    authentication_settings:
      openid:
        openid_provider_id: testopenid
        bearer_token_sending_methods:
          - authorizationHeader
    subscription_key_parameter_names:
      header: Ocp-Apim-Subscription-Key
      query: subscription-key
    display_name: Swagger Petstore
    service_url: 'http://petstore.swagger.io/v2'
    path: petstore
    protocols:
      - https
- name: ApiManagementUpdateApi
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    display_name: Echo API New
    service_url: 'http://echoapi.cloudapp.net/api2'
    path: newecho
- name: ApiManagementDeleteApi
  azure_rm_apimanagementapi:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
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
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Api entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
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
              Specifies whether subscription key is required during call to this
              API, true - API is included into closed products only, false - API
              is included into open products alone, null - there is a mix of
              products.
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
    type:
      description:
        - Type of API.
      returned: always
      type: str
      sample: null
    api_revision:
      description:
        - >-
          Describes the Revision of the Api. If no value is provided, default
          revision 1 is created
      returned: always
      type: str
      sample: null
    api_version:
      description:
        - Indicates the Version identifier of the API if the API is versioned
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
          Specifies whether an API or Product subscription is required for
          accessing the API.
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
          Absolute URL of the backend service implementing this API. Cannot be
          more than 2000 characters long.
      returned: always
      type: str
      sample: null
    path:
      description:
        - >-
          Relative URL uniquely identifying this API and all of its resource
          paths within the API Management service instance. It is appended to
          the API endpoint base URL specified during the service instance
          creation to form a public URL for this API.
      returned: always
      type: str
      sample: null
    protocols:
      description:
        - >-
          Describes on which protocols the operations in this API can be
          invoked.
      returned: always
      type: 'unknown[undefined {"$ref":"350"}]'
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
              Identifier for existing API Version Set. Omit this value to create
              a new Version Set.
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
              An value that determines where the API Version identifer will be
              located in a HTTP request.
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
              Name of HTTP header parameter that indicates the API Version if
              versioningScheme is set to `header`.
          returned: always
          type: str
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApi(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='service_name',
                required=true
            ),
            api_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            authentication_settings=dict(
                type='dict',
                disposition='/',
                options=dict(
                    o_auth2=dict(
                        type='dict',
                        options=dict(
                            authorization_server_id=dict(
                                type='str'
                            ),
                            scope=dict(
                                type='str'
                            )
                        )
                    ),
                    openid=dict(
                        type='dict',
                        options=dict(
                            openid_provider_id=dict(
                                type='str'
                            ),
                            bearer_token_sending_methods=dict(
                                type='list'
                            )
                        )
                    ),
                    subscription_key_required=dict(
                        type='boolean'
                    )
                )
            ),
            subscription_key_parameter_names=dict(
                type='dict',
                disposition='/',
                options=dict(
                    header=dict(
                        type='str'
                    ),
                    query=dict(
                        type='str'
                    )
                )
            ),
            type=dict(
                type='str',
                disposition='/',
                choices=['http',
                         'soap']
            ),
            api_revision=dict(
                type='str',
                disposition='/'
            ),
            api_version=dict(
                type='str',
                disposition='/'
            ),
            is_current=dict(
                type='boolean',
                disposition='/'
            ),
            api_revision_description=dict(
                type='str',
                disposition='/'
            ),
            api_version_description=dict(
                type='str',
                disposition='/'
            ),
            api_version_set_id=dict(
                type='raw',
                disposition='/',
                pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                         '/{{ resource_group }}/providers/Microsoft.ApiManagement/service'
                         '/{{ service_name }}/apiVersionSets/{{ name }}')
            ),
            subscription_required=dict(
                type='boolean',
                disposition='/'
            ),
            source_api_id=dict(
                type='raw',
                disposition='/',
                pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                         '/{{ resource_group }}/providers/Microsoft.ApiManagement/service'
                         '/{{ service_name }}/apis/{{ name }}')
            ),
            display_name=dict(
                type='str',
                disposition='/'
            ),
            service_url=dict(
                type='str',
                disposition='/'
            ),
            path=dict(
                type='str',
                disposition='/',
                required=true
            ),
            protocols=dict(
                type='list',
                disposition='/'
            ),
            api_version_set=dict(
                type='dict',
                disposition='/',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    name=dict(
                        type='str'
                    ),
                    description=dict(
                        type='str'
                    ),
                    versioning_scheme=dict(
                        type='str',
                        choices=['Segment',
                                 'Query',
                                 'Header']
                    ),
                    version_query_name=dict(
                        type='str'
                    ),
                    version_header_name=dict(
                        type='str'
                    )
                )
            ),
            value=dict(
                type='str',
                disposition='/'
            ),
            format=dict(
                type='str',
                disposition='/',
                choices=['wadl-xml',
                         'wadl-link-json',
                         'swagger-json',
                         'swagger-link-json',
                         'wsdl',
                         'wsdl-link',
                         'openapi',
                         'openapi+json',
                         'openapi-link']
            ),
            wsdl_selector=dict(
                type='dict',
                disposition='/',
                options=dict(
                    wsdl_service_name=dict(
                        type='str'
                    ),
                    wsdl_endpoint_name=dict(
                        type='str'
                    )
                )
            ),
            api_type=dict(
                type='str',
                disposition='/',
                choices=['SoapToRest',
                         'SoapPassThrough']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.api_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApi, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if self.location is None:
            self.location = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.api.create_or_update(resource_group_name=self.resource_group,
                                                             service_name=self.name,
                                                             api_id=self.api_id,
                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Api instance.')
            self.fail('Error creating the Api instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Api instance {0}'.format(self.))
        try:
            response = self.mgmt_client.api.delete(resource_group_name=self.resource_group,
                                                   service_name=self.name,
                                                   api_id=self.api_id,
                                                   if-match=self.If-Match)
        except CloudError as e:
            self.log('Error attempting to delete the Api instance.')
            self.fail('Error deleting the Api instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Api instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.api.get(resource_group_name=self.resource_group,
                                                service_name=self.name,
                                                api_id=self.api_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApi()


if __name__ == '__main__':
    main()
