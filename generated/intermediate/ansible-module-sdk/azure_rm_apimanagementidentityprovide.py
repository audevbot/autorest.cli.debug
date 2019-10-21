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
module: azure_rm_apimanagementidentityprovide
version_added: '2.9'
short_description: Manage Azure IdentityProvider instance.
description:
  - 'Create, update and delete instance of Azure IdentityProvider.'
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
  name:
    description:
      - Resource name.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  signin_tenant:
    description:
      - The TenantId to use instead of Common when logging into Active Directory
    type: str
  allowed_tenants:
    description:
      - List of Allowed Tenants when configuring Azure Active Directory login.
    type: list
  authority:
    description:
      - OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
    type: str
  signup_policy_name:
    description:
      - Signup Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  signin_policy_name:
    description:
      - Signin Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  profile_editing_policy_name:
    description:
      - Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  password_reset_policy_name:
    description:
      - Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  client_id:
    description:
      - >-
        Client Id of the Application in the external Identity Provider. It is
        App ID for Facebook login, Client ID for Google login, App ID for
        Microsoft.
    required: true
    type: str
  client_secret:
    description:
      - >-
        Client secret of the Application in external Identity Provider, used to
        authenticate login request. For example, it is App Secret for Facebook
        login, API Key for Google login, Public Key for Microsoft.
    required: true
    type: str
  id:
    description:
      - Resource ID.
    type: str
  state:
    description:
      - Assert the state of the IdentityProvider.
      - >-
        Use C(present) to create or update an IdentityProvider and C(absent) to
        delete it.
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
- name: ApiManagementCreateIdentityProvider
  azure_rm_apimanagementidentityprovide:
    resource_group: myResourceGroup
    service_name: myService
    name: myIdentityProvider
    client_id: facebookid
    client_secret: facebookapplicationsecret
- name: ApiManagementUpdateIdentityProvider
  azure_rm_apimanagementidentityprovide:
    resource_group: myResourceGroup
    service_name: myService
    name: myIdentityProvider
    client_id: updatedfacebookid
    client_secret: updatedfacebooksecret
- name: ApiManagementDeleteIdentityProvider
  azure_rm_apimanagementidentityprovide:
    resource_group: myResourceGroup
    service_name: myService
    name: myIdentityProvider
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
    - Identity Provider contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - Identity Provider Type identifier.
      returned: always
      type: str
      sample: null
    signin_tenant:
      description:
        - >-
          The TenantId to use instead of Common when logging into Active
          Directory
      returned: always
      type: str
      sample: null
    allowed_tenants:
      description:
        - List of Allowed Tenants when configuring Azure Active Directory login.
      returned: always
      type: str
      sample: null
    authority:
      description:
        - OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
      returned: always
      type: str
      sample: null
    signup_policy_name:
      description:
        - Signup Policy Name. Only applies to AAD B2C Identity Provider.
      returned: always
      type: str
      sample: null
    signin_policy_name:
      description:
        - Signin Policy Name. Only applies to AAD B2C Identity Provider.
      returned: always
      type: str
      sample: null
    profile_editing_policy_name:
      description:
        - >-
          Profile Editing Policy Name. Only applies to AAD B2C Identity
          Provider.
      returned: always
      type: str
      sample: null
    password_reset_policy_name:
      description:
        - Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
      returned: always
      type: str
      sample: null
    client_id:
      description:
        - >-
          Client Id of the Application in the external Identity Provider. It is
          App ID for Facebook login, Client ID for Google login, App ID for
          Microsoft.
      returned: always
      type: str
      sample: null
    client_secret:
      description:
        - >-
          Client secret of the Application in external Identity Provider, used
          to authenticate login request. For example, it is App Secret for
          Facebook login, API Key for Google login, Public Key for Microsoft.
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


class AzureRMIdentityProvider(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='identity_provider_name',
                required=true
            ),
            type=dict(
                type='str',
                disposition='/',
                choices=['facebook',
                         'google',
                         'microsoft',
                         'twitter',
                         'aad',
                         'aadB2C']
            ),
            signin_tenant=dict(
                type='str',
                disposition='/'
            ),
            allowed_tenants=dict(
                type='list',
                disposition='/'
            ),
            authority=dict(
                type='str',
                disposition='/'
            ),
            signup_policy_name=dict(
                type='str',
                disposition='/'
            ),
            signin_policy_name=dict(
                type='str',
                disposition='/'
            ),
            profile_editing_policy_name=dict(
                type='str',
                disposition='/'
            ),
            password_reset_policy_name=dict(
                type='str',
                no_log=True,
                disposition='/'
            ),
            client_id=dict(
                type='str',
                disposition='/',
                required=true
            ),
            client_secret=dict(
                type='str',
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
        self.service_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIdentityProvider, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.identity_provider.create_or_update(resource_group_name=self.resource_group,
                                                                           service_name=self.service_name,
                                                                           identity_provider_name=self.name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IdentityProvider instance.')
            self.fail('Error creating the IdentityProvider instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the IdentityProvider instance {0}'.format(self.))
        try:
            response = self.mgmt_client.identity_provider.delete(resource_group_name=self.resource_group,
                                                                 service_name=self.service_name,
                                                                 identity_provider_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the IdentityProvider instance.')
            self.fail('Error deleting the IdentityProvider instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the IdentityProvider instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.identity_provider.get(resource_group_name=self.resource_group,
                                                              service_name=self.service_name,
                                                              identity_provider_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIdentityProvider()


if __name__ == '__main__':
    main()
