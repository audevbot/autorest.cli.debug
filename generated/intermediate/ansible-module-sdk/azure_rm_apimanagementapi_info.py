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
module: azure_rm_apimanagementapi_info
version_added: '2.9'
short_description: Get Api info.
description:
  - Get info of Api.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  expand_api_version_set:
    description:
      - Include full ApiVersionSet resource in response
  include_not_tagged_apis:
    description:
      - Include not tagged APIs.
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApis
  azure_rm_apimanagementapi_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementListApisByTags
  azure_rm_apimanagementapi_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetApiContract
  azure_rm_apimanagementapi_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
- name: ApiManagementGetApiRevisionContract
  azure_rm_apimanagementapi_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi

'''

RETURN = '''
api:
  description: >-
    A list of dict results where the key is the name of the Api and the values
    are the facts for that Api.
  returned: always
  type: complex
  contains:
    api_name:
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


class AzureRMApiInfo(AzureRMModuleBase):
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
            expand_api_version_set=dict(
                type='boolean'
            ),
            include_not_tagged_apis=dict(
                type='boolean'
            ),
            api_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.tags = None
        self.expand_api_version_set = None
        self.include_not_tagged_apis = None
        self.api_id = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None

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
        super(AzureRMApiInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None):
            self.results['api'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['api'] = self.format_item(self.listbytags())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['api'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api.get(resource_group_name=self.resource_group,
                                                service_name=self.service_name,
                                                api_id=self.api_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbytags(self):
        response = None

        try:
            response = self.mgmt_client.api.list_by_tags(resource_group_name=self.resource_group,
                                                         service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.api.list_by_service(resource_group_name=self.resource_group,
                                                            service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiInfo()


if __name__ == '__main__':
    main()
