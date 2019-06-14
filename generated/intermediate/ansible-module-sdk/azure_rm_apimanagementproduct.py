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
module: azure_rm_apimanagementproduct
version_added: '2.9'
short_description: Manage Azure Product instance.
description:
  - 'Create, update and delete instance of Azure Product.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
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
      - Assert the state of the Product.
      - >-
        Use C(present) to create or update an Product and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
  display_name:
    description:
      - Product name.
    required: true
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateProduct
  azure_rm_apimanagementproduct:
    resource_group: myResourceGroup
    name: myService
    product_id: myProduct
    display_name: Test Template ProductName 4
- name: ApiManagementUpdateProduct
  azure_rm_apimanagementproduct:
    resource_group: myResourceGroup
    name: myService
    product_id: myProduct
    display_name: Test Template ProductName 4
- name: ApiManagementDeleteProduct
  azure_rm_apimanagementproduct:
    resource_group: myResourceGroup
    name: myService
    product_id: myProduct
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
    - Product entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    description:
      description:
        - Product description. May include HTML formatting tags.
      returned: always
      type: str
      sample: null
    terms:
      description:
        - >-
          Product terms of use. Developers trying to subscribe to the product
          will be presented and required to accept these terms before they can
          complete the subscription process.
      returned: always
      type: str
      sample: null
    subscription_required:
      description:
        - >-
          Whether a product subscription is required for accessing APIs included
          in this product. If true, the product is referred to as "protected"
          and a valid subscription key is required for a request to an API
          included in the product to succeed. If false, the product is referred
          to as "open" and requests to an API included in the product can be
          made without a subscription key. If property is omitted when creating
          a new product it's value is assumed to be true.
      returned: always
      type: boolean
      sample: null
    approval_required:
      description:
        - >-
          whether subscription approval is required. If false, new subscriptions
          will be approved automatically enabling developers to call the
          product’s APIs immediately after subscribing. If true, administrators
          must manually approve the subscription before the developer can any of
          the product’s APIs. Can be present only if subscriptionRequired
          property is present and has a value of false.
      returned: always
      type: boolean
      sample: null
    subscriptions_limit:
      description:
        - >-
          Whether the number of subscriptions a user can have to this product at
          the same time. Set to null or omit to allow unlimited per user
          subscriptions. Can be present only if subscriptionRequired property is
          present and has a value of false.
      returned: always
      type: number
      sample: null
    state:
      description:
        - >-
          whether product is published or not. Published products are
          discoverable by users of developer portal. Non published products are
          visible only to administrators. Default state of Product is
          notPublished.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Product name.
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


class AzureRMProduct(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='service_name',
                required=true
            ),
            product_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            terms=dict(
                type='str',
                disposition='/'
            ),
            subscription_required=dict(
                type='boolean',
                disposition='/'
            ),
            approval_required=dict(
                type='boolean',
                disposition='/'
            ),
            subscriptions_limit=dict(
                type='number',
                disposition='/'
            ),
            state=dict(
                type='str',
                disposition='/',
                choices=['notPublished',
                         'published']
            ),
            display_name=dict(
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
        self.name = None
        self.product_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMProduct, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.product.create_or_update(resource_group_name=self.resource_group,
                                                                 service_name=self.name,
                                                                 product_id=self.product_id,
                                                                 parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Product instance.')
            self.fail('Error creating the Product instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Product instance {0}'.format(self.))
        try:
            response = self.mgmt_client.product.delete(resource_group_name=self.resource_group,
                                                       service_name=self.name,
                                                       product_id=self.product_id,
                                                       if-match=self.If-Match)
        except CloudError as e:
            self.log('Error attempting to delete the Product instance.')
            self.fail('Error deleting the Product instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Product instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.product.get(resource_group_name=self.resource_group,
                                                    service_name=self.name,
                                                    product_id=self.product_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMProduct()


if __name__ == '__main__':
    main()
