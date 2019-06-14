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
module: azure_rm_apimanagementuser_info
version_added: '2.9'
short_description: Get User info.
description:
  - Get info of User.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  expand_groups:
    description:
      - Detailed Group in response.
  user_id:
    description:
      - >-
        User identifier. Must be unique in the current API Management service
        instance.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  state:
    description:
      - >-
        Account state. Specifies whether the user is active or not. Blocked
        users are unable to sign into the developer portal or call any APIs of
        subscribed products. Default state is Active.
  note:
    description:
      - Optional note about a user set by the administrator.
  identities:
    description:
      - Collection of user identities.
    type: list
    suboptions:
      provider:
        description:
          - Identity provider name.
      id:
        description:
          - Identifier value within provider.
  first_name:
    description:
      - First name.
  last_name:
    description:
      - Last name.
  email:
    description:
      - Email address.
  registration_date:
    description:
      - >-
        Date of user registration. The date conforms to the following format:
        `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
      - ''
  groups:
    description:
      - Collection of groups user is part of.
    type: list
    suboptions:
      display_name:
        description:
          - Group name.
        required: true
      description:
        description:
          - Group description. Can contain HTML formatting tags.
      built_in:
        description:
          - >-
            true if the group is one of the three system groups (Administrators,
            Developers, or Guests); otherwise false.
      type:
        description:
          - Group type.
      external_id:
        description:
          - >-
            For external groups, this property contains the id of the group from
            the external identity provider, e.g. for Azure Active Directory
            `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise
            the value is null.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListUsers
  azure_rm_apimanagementuser_info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetUser
  azure_rm_apimanagementuser_info:
    resource_group: myResourceGroup
    name: myService
    user_id: myUser

'''

RETURN = '''
user:
  description: >-
    A list of dict results where the key is the name of the User and the values
    are the facts for that User.
  returned: always
  type: complex
  contains:
    user_name:
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
            - User entity contract properties.
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


class AzureRMUserInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            ),
            expand_groups=dict(
                type='boolean'
            ),
            user_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.expand_groups = None
        self.user_id = None
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
        super(AzureRMUserInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.user_id is not None):
            self.results['user'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['user'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.user.get(resource_group_name=self.resource_group,
                                                 service_name=self.name,
                                                 user_id=self.user_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.user.list_by_service(resource_group_name=self.resource_group,
                                                             service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMUserInfo()


if __name__ == '__main__':
    main()
