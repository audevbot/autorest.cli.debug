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
module: azure_rm_apimanagementauthorizationserver
version_added: '2.9'
short_description: Manage Azure AuthorizationServer instance.
description:
  - 'Create, update and delete instance of Azure AuthorizationServer.'
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
  authsid:
    description:
      - Identifier of the authorization server.
    required: true
    type: str
  description:
    description:
      - >-
        Description of the authorization server. Can contain HTML formatting
        tags.
    type: str
  authorization_methods:
    description:
      - >-
        HTTP verbs supported by the authorization endpoint. GET must be always
        present. POST is optional.
    type: list
  client_authentication_method:
    description:
      - >-
        Method of authentication supported by the token endpoint of this
        authorization server. Possible values are Basic and/or Body. When Body
        is specified, client credentials and other parameters are passed within
        the request body in the application/x-www-form-urlencoded format.
    type: list
  token_body_parameters:
    description:
      - >-
        Additional parameters required by the token endpoint of this
        authorization server represented as an array of JSON objects with name
        and value string properties, i.e. {"name" : "name value", "value": "a
        value"}.
    type: list
    suboptions:
      name:
        description:
          - body parameter name.
        required: true
        type: str
      value:
        description:
          - body parameter value.
        required: true
        type: str
  token_endpoint:
    description:
      - OAuth token endpoint. Contains absolute URI to entity being referenced.
    type: str
  support_state:
    description:
      - >-
        If true, authorization server will include state parameter from the
        authorization request to its response. Client may use state parameter to
        raise protocol security.
    type: boolean
  default_scope:
    description:
      - >-
        Access token scope that is going to be requested by default. Can be
        overridden at the API level. Should be provided in the form of a string
        containing space-delimited values.
    type: str
  bearer_token_sending_methods:
    description:
      - 'Specifies the mechanism by which access token is passed to the API. '
    type: list
  client_secret:
    description:
      - Client or app secret registered with this authorization server.
    type: str
  resource_owner_username:
    description:
      - >-
        Can be optionally specified when resource owner password grant type is
        supported by this authorization server. Default resource owner username.
    type: str
  resource_owner_password:
    description:
      - >-
        Can be optionally specified when resource owner password grant type is
        supported by this authorization server. Default resource owner password.
    type: str
  display_name:
    description:
      - User-friendly authorization server name.
    required: true
    type: str
  client_registration_endpoint:
    description:
      - >-
        Optional reference to a page where client or app registration for this
        authorization server is performed. Contains absolute URL to entity being
        referenced.
    required: true
    type: str
  authorization_endpoint:
    description:
      - >-
        OAuth authorization endpoint. See
        http://tools.ietf.org/html/rfc6749#section-3.2.
    required: true
    type: str
  grant_types:
    description:
      - >-
        Form of an authorization grant, which the client uses to request the
        access token.
    required: true
    type: list
  client_id:
    description:
      - Client or app id registered with this authorization server.
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
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the AuthorizationServer.
      - >-
        Use C(present) to create or update an AuthorizationServer and C(absent)
        to delete it.
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
- name: ApiManagementCreateAuthorizationServer
  azure_rm_apimanagementauthorizationserver:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer
    description: test server
    authorization_methods:
      - GET
    token_endpoint: 'https://www.contoso.com/oauth2/token'
    support_state: true
    default_scope: read write
    bearer_token_sending_methods:
      - authorizationHeader
    client_secret: '2'
    resource_owner_username: un
    resource_owner_password: pwd
    display_name: test2
    client_registration_endpoint: 'https://www.contoso.com/apps'
    authorization_endpoint: 'https://www.contoso.com/oauth2/auth'
    grant_types:
      - authorizationCode
      - implicit
    client_id: '1'
- name: ApiManagementUpdateAuthorizationServer
  azure_rm_apimanagementauthorizationserver:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer
    client_secret: updated
    client_id: update
- name: ApiManagementDeleteAuthorizationServer
  azure_rm_apimanagementauthorizationserver:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer
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
    - Properties of the External OAuth authorization server Contract.
  returned: always
  type: dict
  sample: null
  contains:
    description:
      description:
        - >-
          Description of the authorization server. Can contain HTML formatting
          tags.
      returned: always
      type: str
      sample: null
    authorization_methods:
      description:
        - >-
          HTTP verbs supported by the authorization endpoint. GET must be always
          present. POST is optional.
      returned: always
      type: str
      sample: null
    client_authentication_method:
      description:
        - >-
          Method of authentication supported by the token endpoint of this
          authorization server. Possible values are Basic and/or Body. When Body
          is specified, client credentials and other parameters are passed
          within the request body in the application/x-www-form-urlencoded
          format.
      returned: always
      type: str
      sample: null
    token_body_parameters:
      description:
        - >-
          Additional parameters required by the token endpoint of this
          authorization server represented as an array of JSON objects with name
          and value string properties, i.e. {"name" : "name value", "value": "a
          value"}.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - body parameter name.
          returned: always
          type: str
          sample: null
        value:
          description:
            - body parameter value.
          returned: always
          type: str
          sample: null
    token_endpoint:
      description:
        - >-
          OAuth token endpoint. Contains absolute URI to entity being
          referenced.
      returned: always
      type: str
      sample: null
    support_state:
      description:
        - >-
          If true, authorization server will include state parameter from the
          authorization request to its response. Client may use state parameter
          to raise protocol security.
      returned: always
      type: boolean
      sample: null
    default_scope:
      description:
        - >-
          Access token scope that is going to be requested by default. Can be
          overridden at the API level. Should be provided in the form of a
          string containing space-delimited values.
      returned: always
      type: str
      sample: null
    bearer_token_sending_methods:
      description:
        - 'Specifies the mechanism by which access token is passed to the API. '
      returned: always
      type: str
      sample: null
    client_secret:
      description:
        - Client or app secret registered with this authorization server.
      returned: always
      type: str
      sample: null
    resource_owner_username:
      description:
        - >-
          Can be optionally specified when resource owner password grant type is
          supported by this authorization server. Default resource owner
          username.
      returned: always
      type: str
      sample: null
    resource_owner_password:
      description:
        - >-
          Can be optionally specified when resource owner password grant type is
          supported by this authorization server. Default resource owner
          password.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - User-friendly authorization server name.
      returned: always
      type: str
      sample: null
    client_registration_endpoint:
      description:
        - >-
          Optional reference to a page where client or app registration for this
          authorization server is performed. Contains absolute URL to entity
          being referenced.
      returned: always
      type: str
      sample: null
    authorization_endpoint:
      description:
        - >-
          OAuth authorization endpoint. See
          http://tools.ietf.org/html/rfc6749#section-3.2.
      returned: always
      type: str
      sample: null
    grant_types:
      description:
        - >-
          Form of an authorization grant, which the client uses to request the
          access token.
      returned: always
      type: str
      sample: null
    client_id:
      description:
        - Client or app id registered with this authorization server.
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


class AzureRMAuthorizationServer(AzureRMModuleBaseExt):
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
            authsid=dict(
                type='str',
                updatable=False,
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            authorization_methods=dict(
                type='list',
                disposition='/',
                choices=['HEAD',
                         'OPTIONS',
                         'TRACE',
                         'GET',
                         'POST',
                         'PUT',
                         'PATCH',
                         'DELETE']
            ),
            client_authentication_method=dict(
                type='list',
                disposition='/',
                choices=['Basic',
                         'Body']
            ),
            token_body_parameters=dict(
                type='list',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str',
                        required=true
                    ),
                    value=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            token_endpoint=dict(
                type='str',
                disposition='/'
            ),
            support_state=dict(
                type='boolean',
                disposition='/'
            ),
            default_scope=dict(
                type='str',
                disposition='/'
            ),
            bearer_token_sending_methods=dict(
                type='list',
                disposition='/',
                choices=['authorizationHeader',
                         'query']
            ),
            client_secret=dict(
                type='str',
                disposition='/'
            ),
            resource_owner_username=dict(
                type='str',
                disposition='/'
            ),
            resource_owner_password=dict(
                type='str',
                disposition='/'
            ),
            display_name=dict(
                type='str',
                disposition='/',
                required=true
            ),
            client_registration_endpoint=dict(
                type='str',
                disposition='/',
                required=true
            ),
            authorization_endpoint=dict(
                type='str',
                disposition='/',
                required=true
            ),
            grant_types=dict(
                type='list',
                disposition='/',
                choices=['authorizationCode',
                         'implicit',
                         'resourceOwnerPassword',
                         'clientCredentials'],
                required=true
            ),
            client_id=dict(
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
        self.authsid = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAuthorizationServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.authorization_server.create_or_update(resource_group_name=self.resource_group,
                                                                              service_name=self.service_name,
                                                                              authsid=self.authsid,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AuthorizationServer instance.')
            self.fail('Error creating the AuthorizationServer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the AuthorizationServer instance {0}'.format(self.))
        try:
            response = self.mgmt_client.authorization_server.delete(resource_group_name=self.resource_group,
                                                                    service_name=self.service_name,
                                                                    authsid=self.authsid)
        except CloudError as e:
            self.log('Error attempting to delete the AuthorizationServer instance.')
            self.fail('Error deleting the AuthorizationServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the AuthorizationServer instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.authorization_server.get(resource_group_name=self.resource_group,
                                                                 service_name=self.service_name,
                                                                 authsid=self.authsid)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAuthorizationServer()


if __name__ == '__main__':
    main()
