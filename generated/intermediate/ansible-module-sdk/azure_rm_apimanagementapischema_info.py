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
module: azure_rm_apimanagementapischema_info
version_added: '2.9'
short_description: Get ApiSchema info.
description:
  - Get info of ApiSchema.
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
  schema_id:
    description:
      - >-
        Schema identifier within an API. Must be unique in the current API
        Management service instance.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  content_type:
    description:
      - >-
        Must be a valid a media type used in a Content-Type header as defined in
        the RFC 2616. Media type of the schema document (e.g. application/json,
        application/xml).
    required: true
  document:
    description:
      - Properties of the Schema Document.
    suboptions:
      value:
        description:
          - Json escaped string defining the document representing the Schema.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiSchemas
  azure_rm_apimanagementapischema_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
- name: ApiManagementGetApiSchema
  azure_rm_apimanagementapischema_info:
    resource_group: myResourceGroup
    name: myService
    api_id: myApis
    schema_id: mySchema

'''

RETURN = '''
api_schema:
  description: >-
    A list of dict results where the key is the name of the ApiSchema and the
    values are the facts for that ApiSchema.
  returned: always
  type: complex
  contains:
    apischema_name:
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
            - Properties of the Schema.
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


class AzureRMApiSchemaInfo(AzureRMModuleBase):
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
            schema_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.api_id = None
        self.schema_id = None
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
        super(AzureRMApiSchemaInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.api_id is not None and
            self.schema_id is not None):
            self.results['api_schema'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None and
              self.api_id is not None):
            self.results['api_schema'] = self.format_item(self.listbyapi())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_schema.get(resource_group_name=self.resource_group,
                                                       service_name=self.name,
                                                       api_id=self.api_id,
                                                       schema_id=self.schema_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyapi(self):
        response = None

        try:
            response = self.mgmt_client.api_schema.list_by_api(resource_group_name=self.resource_group,
                                                               service_name=self.name,
                                                               api_id=self.api_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiSchemaInfo()


if __name__ == '__main__':
    main()
