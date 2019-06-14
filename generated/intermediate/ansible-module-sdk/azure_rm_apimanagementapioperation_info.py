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
module: azure_rm_apimanagementapioperation_info
version_added: '2.9'
short_description: Get ApiOperation info.
description:
  - Get info of ApiOperation.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
  operation_id:
    description:
      - >-
        Operation identifier within an API. Must be unique in the current API
        Management service instance.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  template_parameters:
    description:
      - Collection of URL template parameters.
    type: list
    suboptions:
      name:
        description:
          - Parameter name.
        required: true
      description:
        description:
          - Parameter description.
      type:
        description:
          - Parameter type.
        required: true
      default_value:
        description:
          - Default parameter value.
      required:
        description:
          - Specifies whether parameter is required or not.
      values:
        description:
          - Parameter values.
        type: list
  description:
    description:
      - Description of the operation. May include HTML formatting tags.
  request:
    description:
      - An entity containing request details.
    suboptions:
      description:
        description:
          - Operation request description.
      query_parameters:
        description:
          - Collection of operation request query parameters.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
          description:
            description:
              - Parameter description.
          type:
            description:
              - Parameter type.
            required: true
          default_value:
            description:
              - Default parameter value.
          required:
            description:
              - Specifies whether parameter is required or not.
          values:
            description:
              - Parameter values.
            type: list
      headers:
        description:
          - Collection of operation request headers.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
          description:
            description:
              - Parameter description.
          type:
            description:
              - Parameter type.
            required: true
          default_value:
            description:
              - Default parameter value.
          required:
            description:
              - Specifies whether parameter is required or not.
          values:
            description:
              - Parameter values.
            type: list
      representations:
        description:
          - Collection of operation request representations.
        type: list
        suboptions:
          content_type:
            description:
              - >-
                Specifies a registered or custom content type for this
                representation, e.g. application/xml.
            required: true
          sample:
            description:
              - An example of the representation.
          schema_id:
            description:
              - >-
                Schema identifier. Applicable only if 'contentType' value is
                neither 'application/x-www-form-urlencoded' nor
                'multipart/form-data'.
          type_name:
            description:
              - >-
                Type name defined by the schema. Applicable only if
                'contentType' value is neither
                'application/x-www-form-urlencoded' nor 'multipart/form-data'.
          form_parameters:
            description:
              - >-
                Collection of form parameters. Required if 'contentType' value
                is either 'application/x-www-form-urlencoded' or
                'multipart/form-data'..
            type: list
            suboptions:
              name:
                description:
                  - Parameter name.
                required: true
              description:
                description:
                  - Parameter description.
              type:
                description:
                  - Parameter type.
                required: true
              default_value:
                description:
                  - Default parameter value.
              required:
                description:
                  - Specifies whether parameter is required or not.
              values:
                description:
                  - Parameter values.
                type: list
  responses:
    description:
      - Array of Operation responses.
    type: list
    suboptions:
      status_code:
        description:
          - Operation response HTTP status code.
        required: true
      description:
        description:
          - Operation response description.
      representations:
        description:
          - Collection of operation response representations.
        type: list
        suboptions:
          content_type:
            description:
              - >-
                Specifies a registered or custom content type for this
                representation, e.g. application/xml.
            required: true
          sample:
            description:
              - An example of the representation.
          schema_id:
            description:
              - >-
                Schema identifier. Applicable only if 'contentType' value is
                neither 'application/x-www-form-urlencoded' nor
                'multipart/form-data'.
          type_name:
            description:
              - >-
                Type name defined by the schema. Applicable only if
                'contentType' value is neither
                'application/x-www-form-urlencoded' nor 'multipart/form-data'.
          form_parameters:
            description:
              - >-
                Collection of form parameters. Required if 'contentType' value
                is either 'application/x-www-form-urlencoded' or
                'multipart/form-data'..
            type: list
            suboptions:
              name:
                description:
                  - Parameter name.
                required: true
              description:
                description:
                  - Parameter description.
              type:
                description:
                  - Parameter type.
                required: true
              default_value:
                description:
                  - Default parameter value.
              required:
                description:
                  - Specifies whether parameter is required or not.
              values:
                description:
                  - Parameter values.
                type: list
      headers:
        description:
          - Collection of operation response headers.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
          description:
            description:
              - Parameter description.
          type:
            description:
              - Parameter type.
            required: true
          default_value:
            description:
              - Default parameter value.
          required:
            description:
              - Specifies whether parameter is required or not.
          values:
            description:
              - Parameter values.
            type: list
  policies:
    description:
      - Operation Policies
  display_name:
    description:
      - Operation Name.
    required: true
  method:
    description:
      - >-
        A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST
        but not limited by only them.
    required: true
  url_template:
    description:
      - >-
        Relative URL template identifying the target resource for this
        operation. May include parameters. Example:
        /customers/{cid}/orders/{oid}/?date={date}
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiOperations
  azure_rm_apimanagementapioperation_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    operation_id: 57d2ef278aa04f0ad01d6cdc
- name: ApiManagementGetApiOperation
  azure_rm_apimanagementapioperation_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    operation_id: myOperation
- name: ApiManagementGetApiOperationPetStore
  azure_rm_apimanagementapioperation_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    operation_id: myOperation

'''

RETURN = '''
api_operation:
  description: >-
    A list of dict results where the key is the name of the ApiOperation and the
    values are the facts for that ApiOperation.
  returned: always
  type: complex
  contains:
    apioperation_name:
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
            - Properties of the Operation Contract.
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


class AzureRMApiOperationInfo(AzureRMModuleBase):
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
            api_id=dict(
                type='str',
                required=true
            ),
            operation_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.api_id = None
        self.tags = None
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
        super(AzureRMApiOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.api_id is not None and
            self.operation_id is not None):
            self.results['api_operation'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None and
              self.api_id is not None):
            self.results['api_operation'] = self.format_item(self.listbyapi())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_operation.get(resource_group_name=self.resource_group,
                                                          service_name=self.name,
                                                          api_id=self.api_id,
                                                          operation_id=self.operation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyapi(self):
        response = None

        try:
            response = self.mgmt_client.api_operation.list_by_api(resource_group_name=self.resource_group,
                                                                  service_name=self.name,
                                                                  api_id=self.api_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiOperationInfo()


if __name__ == '__main__':
    main()
