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
module: azure_rm_apimanagementproductapi
version_added: '2.9'
short_description: Manage Azure ProductApi instance.
description:
  - 'Create, update and delete instance of Azure ProductApi.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
    type: str
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
      - Type of API.
    type: str
  description:
    description:
      - Description of the API. May include HTML formatting tags.
    type: str
  authentication_settings:
    description:
      - Collection of authentication settings included into this API.
    type: dict
    suboptions:
      o_auth2:
        description:
          - OAuth2 Authentication settings
        type: dict
        suboptions:
          authorization_server_id:
            description:
              - OAuth authorization server identifier.
            type: str
          scope:
            description:
              - operations scope.
            type: str
      openid:
        description:
          - OpenID Connect Authentication Settings
        type: dict
        suboptions:
          openid_provider_id:
            description:
              - OAuth authorization server identifier.
            type: str
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
        type: boolean
  subscription_key_parameter_names:
    description:
      - Protocols over which API is made available.
    type: dict
    suboptions:
      header:
        description:
          - Subscription key header name.
        type: str
      query:
        description:
          - Subscription key query string parameter name.
        type: str
  api_revision:
    description:
      - >-
        Describes the Revision of the Api. If no value is provided, default
        revision 1 is created
    type: str
  api_version:
    description:
      - Indicates the Version identifier of the API if the API is versioned
    type: str
  is_current:
    description:
      - Indicates if API revision is current api revision.
    type: boolean
  is_online:
    description:
      - Indicates if API revision is accessible via the gateway.
    type: boolean
  api_revision_description:
    description:
      - Description of the Api Revision.
    type: str
  api_version_description:
    description:
      - Description of the Api Version.
    type: str
  api_version_set_id:
    description:
      - A resource identifier for the related ApiVersionSet.
    type: str
  subscription_required:
    description:
      - >-
        Specifies whether an API or Product subscription is required for
        accessing the API.
    type: boolean
  source_api_id:
    description:
      - API identifier of the source API.
    type: str
  display_name:
    description:
      - API name. Must be 1 to 300 characters long.
    type: str
  service_url:
    description:
      - >-
        Absolute URL of the backend service implementing this API. Cannot be
        more than 2000 characters long.
    type: str
  path:
    description:
      - >-
        Relative URL uniquely identifying this API and all of its resource paths
        within the API Management service instance. It is appended to the API
        endpoint base URL specified during the service instance creation to form
        a public URL for this API.
    required: true
    type: str
  protocols:
    description:
      - Describes on which protocols the operations in this API can be invoked.
    type: list
  api_version_set:
    description:
      - Version set details
    type: dict
    suboptions:
      id:
        description:
          - >-
            Identifier for existing API Version Set. Omit this value to create a
            new Version Set.
        type: str
      name:
        description:
          - The display Name of the API Version Set.
        type: str
      description:
        description:
          - Description of API Version Set.
        type: str
      versioning_scheme:
        description:
          - >-
            An value that determines where the API Version identifer will be
            located in a HTTP request.
        type: str
      version_query_name:
        description:
          - >-
            Name of query parameter that indicates the API Version if
            versioningScheme is set to `query`.
        type: str
      version_header_name:
        description:
          - >-
            Name of HTTP header parameter that indicates the API Version if
            versioningScheme is set to `header`.
        type: str
  state:
    description:
      - Assert the state of the ProductApi.
      - >-
        Use C(present) to create or update an ProductApi and C(absent) to delete
        it.
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
- name: ApiManagementCreateProductApi
  azure_rm_apimanagementproductapi:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct
    api_id: myApi
- name: ApiManagementDeleteProductApi
  azure_rm_apimanagementproductapi:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct
    api_id: myApi
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


class AzureRMProductApi(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                disposition='serviceName',
                required=true
            ),
            product_id=dict(
                type='str',
                updatable=False,
                disposition='productId',
                required=true
            ),
            api_id=dict(
                type='str',
                updatable=False,
                disposition='apiId',
                required=true
            ),
            description=dict(
                type='str',
                disposition='/properties/*'
            ),
            authentication_settings=dict(
                type='dict',
                disposition='/properties/authenticationSettings',
                options=dict(
                    o_auth2=dict(
                        type='dict',
                        disposition='oAuth2',
                        options=dict(
                            authorization_server_id=dict(
                                type='str',
                                disposition='authorizationServerId'
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
                                type='str',
                                disposition='openidProviderId'
                            ),
                            bearer_token_sending_methods=dict(
                                type='list',
                                disposition='bearerTokenSendingMethods',
                                choices=['authorizationHeader',
                                         'query']
                            )
                        )
                    ),
                    subscription_key_required=dict(
                        type='boolean',
                        disposition='subscriptionKeyRequired'
                    )
                )
            ),
            subscription_key_parameter_names=dict(
                type='dict',
                disposition='/properties/subscriptionKeyParameterNames',
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
                disposition='/properties/*',
                choices=['http',
                         'soap']
            ),
            api_revision=dict(
                type='str',
                disposition='/properties/apiRevision'
            ),
            api_version=dict(
                type='str',
                disposition='/properties/apiVersion'
            ),
            is_current=dict(
                type='boolean',
                disposition='/properties/isCurrent'
            ),
            is_online=dict(
                type='boolean',
                disposition='/properties/isOnline'
            ),
            api_revision_description=dict(
                type='str',
                disposition='/properties/apiRevisionDescription'
            ),
            api_version_description=dict(
                type='str',
                disposition='/properties/apiVersionDescription'
            ),
            api_version_set_id=dict(
                type='str',
                disposition='/properties/apiVersionSetId'
            ),
            subscription_required=dict(
                type='boolean',
                disposition='/properties/subscriptionRequired'
            ),
            source_api_id=dict(
                type='str',
                disposition='/properties/sourceApiId'
            ),
            display_name=dict(
                type='str',
                disposition='/properties/displayName'
            ),
            service_url=dict(
                type='str',
                disposition='/properties/serviceUrl'
            ),
            path=dict(
                type='str',
                disposition='/properties/*',
                required=true
            ),
            protocols=dict(
                type='list',
                disposition='/properties/*',
                choices=['http',
                         'https']
            ),
            api_version_set=dict(
                type='dict',
                disposition='/properties/apiVersionSet',
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
                        disposition='versioningScheme',
                        choices=['Segment',
                                 'Query',
                                 'Header']
                    ),
                    version_query_name=dict(
                        type='str',
                        disposition='versionQueryName'
                    ),
                    version_header_name=dict(
                        type='str',
                        disposition='versionHeaderName'
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
        self.service_name = None
        self.product_id = None
        self.api_id = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None

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

        super(AzureRMProductApi, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/products' +
                    '/{{ product_name }}' +
                    '/apis' +
                    '/{{ api_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ product_name }}', self.product_name)
        self.url = self.url.replace('{{ api_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ProductApi instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ProductApi instance already exists')

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
            self.log('Need to Create / Update the ProductApi instance')

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
            self.log('ProductApi instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ProductApi instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ProductApi instance {0}'.format(self.))

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
            self.log('Error attempting to create the ProductApi instance.')
            self.fail('Error creating the ProductApi instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ProductApi instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ProductApi instance.')
            self.fail('Error deleting the ProductApi instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ProductApi instance {0} is present'.format(self.))
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
            # self.log("ProductApi instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ProductApi instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMProductApi()


if __name__ == '__main__':
    main()
