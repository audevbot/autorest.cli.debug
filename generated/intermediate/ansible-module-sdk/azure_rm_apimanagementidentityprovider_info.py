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
module: azure_rm_apimanagementidentityprovider_info
version_added: '2.9'
short_description: Get IdentityProvider info.
description:
  - Get info of IdentityProvider.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  name:
    description:
      - Resource name.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Identity Provider Type identifier.
  allowed_tenants:
    description:
      - List of Allowed Tenants when configuring Azure Active Directory login.
    type: list
  authority:
    description:
      - OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
  signup_policy_name:
    description:
      - Signup Policy Name. Only applies to AAD B2C Identity Provider.
  signin_policy_name:
    description:
      - Signin Policy Name. Only applies to AAD B2C Identity Provider.
  profile_editing_policy_name:
    description:
      - Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
  password_reset_policy_name:
    description:
      - Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
  client_id:
    description:
      - >-
        Client Id of the Application in the external Identity Provider. It is
        App ID for Facebook login, Client ID for Google login, App ID for
        Microsoft.
    required: true
  client_secret:
    description:
      - >-
        Client secret of the Application in external Identity Provider, used to
        authenticate login request. For example, it is App Secret for Facebook
        login, API Key for Google login, Public Key for Microsoft.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListIdentityProviders
  azure_rm_apimanagementidentityprovider_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetIdentityProvider
  azure_rm_apimanagementidentityprovider_info:
    resource_group: myResourceGroup
    service_name: myService
    name: myIdentityProvider

'''

RETURN = '''
identity_provider:
  description: >-
    A list of dict results where the key is the name of the IdentityProvider and
    the values are the facts for that IdentityProvider.
  returned: always
  type: complex
  contains:
    identityprovider_name:
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
            - Identity Provider contract properties.
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


class AzureRMIdentityProviderInfo(AzureRMModuleBase):
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
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.name = None
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
        super(AzureRMIdentityProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.name is not None):
            self.results['identity_provider'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['identity_provider'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.identity_provider.get(resource_group_name=self.resource_group,
                                                              service_name=self.service_name,
                                                              identity_provider_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.identity_provider.list_by_service(resource_group_name=self.resource_group,
                                                                          service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMIdentityProviderInfo()


if __name__ == '__main__':
    main()
