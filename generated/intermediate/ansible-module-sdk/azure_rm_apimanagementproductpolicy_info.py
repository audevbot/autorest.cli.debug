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
module: azure_rm_apimanagementproductpolicy_info
version_added: '2.9'
short_description: Get ProductPolicy info.
description:
  - Get info of ProductPolicy.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
  policy_id:
    description:
      - The identifier of the Policy.
  format:
    description:
      - Format of the policyContent.
  id:
    description:
      - Resource ID.
  name:
    description:
      - Resource name.
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
- name: ApiManagementListProductPolicies
  azure_rm_apimanagementproductpolicy_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct
- name: ApiManagementGetProductPolicy
  azure_rm_apimanagementproductpolicy_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct
    policy_id: myPolicy

'''

RETURN = '''
product_policy:
  description: >-
    A list of dict results where the key is the name of the ProductPolicy and
    the values are the facts for that ProductPolicy.
  returned: always
  type: complex
  contains:
    productpolicy_name:
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


class AzureRMProductPolicyInfo(AzureRMModuleBase):
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
            product_id=dict(
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
        self.service_name = None
        self.product_id = None
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
        super(AzureRMProductPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.product_id is not None and
            self.policy_id is not None):
            self.results['product_policy'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.product_id is not None):
            self.results['product_policy'] = self.format_item(self.listbyproduct())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.product_policy.get(resource_group_name=self.resource_group,
                                                           service_name=self.service_name,
                                                           product_id=self.product_id,
                                                           policy_id=self.policy_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyproduct(self):
        response = None

        try:
            response = self.mgmt_client.product_policy.list_by_product(resource_group_name=self.resource_group,
                                                                       service_name=self.service_name,
                                                                       product_id=self.product_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMProductPolicyInfo()


if __name__ == '__main__':
    main()
