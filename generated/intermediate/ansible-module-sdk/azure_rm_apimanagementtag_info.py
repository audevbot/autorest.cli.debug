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
module: azure_rm_apimanagementtag_info
version_added: '2.9'
short_description: Get Tag info.
description:
  - Get info of Tag.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  scope:
    description:
      - 'Scope like ''apis'', ''products'' or ''apis/{apiId}'
  tag_id:
    description:
      - >-
        Tag identifier. Must be unique in the current API Management service
        instance.
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
  operation_id:
    description:
      - >-
        Operation identifier within an API. Must be unique in the current API
        Management service instance.
  id:
    description:
      - Resource ID.
  name:
    description:
      - Resource name.
  type:
    description:
      - Resource type for API Management resource.
  display_name:
    description:
      - Tag name.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListTags
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetTag
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    tag_id: myTag
- name: ApiManagementListApiTags
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
- name: ApiManagementGetApiTag
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    tag_id: myTag
    api_id: myApi
- name: ApiManagementListProductTags
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct
- name: ApiManagementGetProductTag
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    tag_id: myTag
    product_id: myProduct
- name: ApiManagementListApiOperationTags
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: myOperation
- name: ApiManagementGetApiOperationTag
  azure_rm_apimanagementtag_info:
    resource_group: myResourceGroup
    service_name: myService
    tag_id: myTag
    api_id: myApi
    operation_id: myOperation

'''

RETURN = '''
tag:
  description: >-
    A list of dict results where the key is the name of the Tag and the values
    are the facts for that Tag.
  returned: always
  type: complex
  contains:
    tag_name:
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
            - Tag entity contract properties.
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


class AzureRMTagInfo(AzureRMModuleBase):
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
            scope=dict(
                type='str'
            ),
            tag_id=dict(
                type='str'
            ),
            api_id=dict(
                type='str'
            ),
            product_id=dict(
                type='str'
            ),
            operation_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.scope = None
        self.tag_id = None
        self.api_id = None
        self.product_id = None
        self.operation_id = None
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
        super(AzureRMTagInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None and
            self.operation_id is not None and
            self.tag_id is not None):
            self.results['tag'] = self.format_item(self.getbyoperation())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None and
              self.operation_id is not None):
            self.results['tag'] = self.format_item(self.listbyoperation())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.product_id is not None and
              self.tag_id is not None):
            self.results['tag'] = self.format_item(self.getbyproduct())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None and
              self.tag_id is not None):
            self.results['tag'] = self.format_item(self.getbyapi())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.product_id is not None):
            self.results['tag'] = self.format_item(self.listbyproduct())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None):
            self.results['tag'] = self.format_item(self.listbyapi())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.tag_id is not None):
            self.results['tag'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['tag'] = self.format_item(self.listbyservice())
        return self.results

    def getbyoperation(self):
        response = None

        try:
            response = self.mgmt_client.tag.get_by_operation(resource_group_name=self.resource_group,
                                                             service_name=self.service_name,
                                                             api_id=self.api_id,
                                                             operation_id=self.operation_id,
                                                             tag_id=self.tag_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyoperation(self):
        response = None

        try:
            response = self.mgmt_client.tag.list_by_operation(resource_group_name=self.resource_group,
                                                              service_name=self.service_name,
                                                              api_id=self.api_id,
                                                              operation_id=self.operation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getbyproduct(self):
        response = None

        try:
            response = self.mgmt_client.tag.get_by_product(resource_group_name=self.resource_group,
                                                           service_name=self.service_name,
                                                           product_id=self.product_id,
                                                           tag_id=self.tag_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getbyapi(self):
        response = None

        try:
            response = self.mgmt_client.tag.get_by_api(resource_group_name=self.resource_group,
                                                       service_name=self.service_name,
                                                       api_id=self.api_id,
                                                       tag_id=self.tag_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyproduct(self):
        response = None

        try:
            response = self.mgmt_client.tag.list_by_product(resource_group_name=self.resource_group,
                                                            service_name=self.service_name,
                                                            product_id=self.product_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyapi(self):
        response = None

        try:
            response = self.mgmt_client.tag.list_by_api(resource_group_name=self.resource_group,
                                                        service_name=self.service_name,
                                                        api_id=self.api_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.tag.get(resource_group_name=self.resource_group,
                                                service_name=self.service_name,
                                                tag_id=self.tag_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.tag.list_by_service(resource_group_name=self.resource_group,
                                                            service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMTagInfo()


if __name__ == '__main__':
    main()
