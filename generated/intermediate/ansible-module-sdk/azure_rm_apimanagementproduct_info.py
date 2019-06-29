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
module: azure_rm_apimanagementproduct_info
version_added: '2.9'
short_description: Get Product info.
description:
  - Get info of Product.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  expand_groups:
    description:
      - >-
        When set to true, the response contains an array of groups that have
        visibility to the product. The default is false.
  include_not_tagged_products:
    description:
      - Include not tagged Products.
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
  id:
    description:
      - Resource ID.
  name:
    description:
      - Resource name.
  type:
    description:
      - Resource type for API Management resource.
  description:
    description:
      - Product description. May include HTML formatting tags.
  terms:
    description:
      - >-
        Product terms of use. Developers trying to subscribe to the product will
        be presented and required to accept these terms before they can complete
        the subscription process.
  subscription_required:
    description:
      - >-
        Whether a product subscription is required for accessing APIs included
        in this product. If true, the product is referred to as "protected" and
        a valid subscription key is required for a request to an API included in
        the product to succeed. If false, the product is referred to as "open"
        and requests to an API included in the product can be made without a
        subscription key. If property is omitted when creating a new product
        it's value is assumed to be true.
  approval_required:
    description:
      - >-
        whether subscription approval is required. If false, new subscriptions
        will be approved automatically enabling developers to call the product’s
        APIs immediately after subscribing. If true, administrators must
        manually approve the subscription before the developer can any of the
        product’s APIs. Can be present only if subscriptionRequired property is
        present and has a value of false.
  subscriptions_limit:
    description:
      - >-
        Whether the number of subscriptions a user can have to this product at
        the same time. Set to null or omit to allow unlimited per user
        subscriptions. Can be present only if subscriptionRequired property is
        present and has a value of false.
  state:
    description:
      - >-
        whether product is published or not. Published products are discoverable
        by users of developer portal. Non published products are visible only to
        administrators. Default state of Product is notPublished.
  display_name:
    description:
      - Product name.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListProducts
  azure_rm_apimanagementproduct_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementListProductsByTags
  azure_rm_apimanagementproduct_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetProduct
  azure_rm_apimanagementproduct_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct

'''

RETURN = '''
product:
  description: >-
    A list of dict results where the key is the name of the Product and the
    values are the facts for that Product.
  returned: always
  type: complex
  contains:
    product_name:
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
            - Product entity contract properties.
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


class AzureRMProductInfo(AzureRMModuleBase):
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
            expand_groups=dict(
                type='boolean'
            ),
            include_not_tagged_products=dict(
                type='boolean'
            ),
            product_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.expand_groups = None
        self.tags = None
        self.include_not_tagged_products = None
        self.product_id = None
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
        super(AzureRMProductInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.product_id is not None):
            self.results['product'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['product'] = self.format_item(self.listbytags())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['product'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.product.get(resource_group_name=self.resource_group,
                                                    service_name=self.service_name,
                                                    product_id=self.product_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbytags(self):
        response = None

        try:
            response = self.mgmt_client.product.list_by_tags(resource_group_name=self.resource_group,
                                                             service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.product.list_by_service(resource_group_name=self.resource_group,
                                                                service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMProductInfo()


if __name__ == '__main__':
    main()
