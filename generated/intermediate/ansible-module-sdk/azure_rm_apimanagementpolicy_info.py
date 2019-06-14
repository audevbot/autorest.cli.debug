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
module: azure_rm_apimanagementpolicy_info
version_added: '2.9'
short_description: Get Policy info.
description:
  - Get info of Policy.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  policy_id:
    description:
      - The identifier of the Policy.
  format:
    description:
      - Format of the policyContent.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  value:
    description:
      - Contents of the Policy as defined by the format.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListPolicies
  azure_rm_apimanagementpolicy_info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetPolicy
  azure_rm_apimanagementpolicy_info:
    resource_group: myResourceGroup
    name: myService
    policy_id: myPolicy
- name: ApiManagementGetPolicyFormat
  azure_rm_apimanagementpolicy_info:
    resource_group: myResourceGroup
    name: myService
    policy_id: myPolicy
    format: rawxml

'''

RETURN = '''
policy:
  description: >-
    A list of dict results where the key is the name of the Policy and the
    values are the facts for that Policy.
  returned: always
  type: complex
  contains:
    policy_name:
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
            - Properties of the Policy.
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


class AzureRMPolicyInfo(AzureRMModuleBase):
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
            policy_id=dict(
                type='str'
            ),
            format=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.policy_id = None
        self.format = None
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
        super(AzureRMPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.policy_id is not None):
            self.results['policy'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['policy'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.policy.get(resource_group_name=self.resource_group,
                                                   service_name=self.name,
                                                   policy_id=self.policy_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.policy.list_by_service(resource_group_name=self.resource_group,
                                                               service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMPolicyInfo()


if __name__ == '__main__':
    main()
