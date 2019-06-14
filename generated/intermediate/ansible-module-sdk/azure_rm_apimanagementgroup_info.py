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
module: azure_rm_apimanagementgroup_info
version_added: '2.9'
short_description: Get Group info.
description:
  - Get info of Group.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  group_id:
    description:
      - >-
        Group identifier. Must be unique in the current API Management service
        instance.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Group type.
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
  external_id:
    description:
      - >-
        For external groups, this property contains the id of the group from the
        external identity provider, e.g. for Azure Active Directory
        `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the
        value is null.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListGroups
  azure_rm_apimanagementgroup_info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetGroup
  azure_rm_apimanagementgroup_info:
    resource_group: myResourceGroup
    name: myService
    group_id: myGroup

'''

RETURN = '''
group:
  description: >-
    A list of dict results where the key is the name of the Group and the values
    are the facts for that Group.
  returned: always
  type: complex
  contains:
    group_name:
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
            - Group entity contract properties.
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


class AzureRMGroupInfo(AzureRMModuleBase):
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
            group_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.group_id = None
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
        super(AzureRMGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.group_id is not None):
            self.results['group'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['group'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.group.get(resource_group_name=self.resource_group,
                                                  service_name=self.name,
                                                  group_id=self.group_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.group.list_by_service(resource_group_name=self.resource_group,
                                                              service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMGroupInfo()


if __name__ == '__main__':
    main()
