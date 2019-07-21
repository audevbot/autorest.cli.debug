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
module: azure_rm_apimanagementuseridentity_info
version_added: '2.9'
short_description: Get UserIdentity info.
description:
  - Get info of UserIdentity.
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
  user_id:
    description:
      - >-
        User identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - User Identity values.
    type: list
    suboptions:
      provider:
        description:
          - Identity provider name.
        type: str
      id:
        description:
          - Identifier value within provider.
        type: str
  count:
    description:
      - Total record count number across all pages.
    type: number
  next_link:
    description:
      - Next page link if any.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListUserIdentities
  azure_rm_apimanagementuseridentity_info:
    resource_group: myResourceGroup
    service_name: myService
    user_id: myUser

'''

RETURN = '''
user_identities:
  description: >-
    A list of dict results where the key is the name of the UserIdentity and the
    values are the facts for that UserIdentity.
  returned: always
  type: complex
  contains:
    useridentity_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - User Identity values.
          returned: always
          type: dict
          sample: null
          contains:
            provider:
              description:
                - Identity provider name.
              returned: always
              type: str
              sample: null
            id:
              description:
                - Identifier value within provider.
              returned: always
              type: str
              sample: null
        count:
          description:
            - Total record count number across all pages.
          returned: always
          type: number
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


class AzureRMUserIdentitiesInfo(AzureRMModuleBase):
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
            user_id=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.user_id = None
        self.value = None
        self.count = None
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
        super(AzureRMUserIdentitiesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.user_id is not None):
            self.results['user_identities'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.user_identities.list(resource_group_name=self.resource_group,
                                                             service_name=self.service_name,
                                                             user_id=self.user_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMUserIdentitiesInfo()


if __name__ == '__main__':
    main()
