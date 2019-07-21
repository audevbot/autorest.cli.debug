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
module: azure_rm_apimanagementapiversionset_info
version_added: '2.9'
short_description: Get ApiVersionSet info.
description:
  - Get info of ApiVersionSet.
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
  version_set_id:
    description:
      - >-
        Api Version Set identifier. Must be unique in the current API Management
        service instance.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  name:
    description:
      - Resource name.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  description:
    description:
      - Description of API Version Set.
    type: str
  version_query_name:
    description:
      - >-
        Name of query parameter that indicates the API Version if
        versioningScheme is set to `query`.
    type: str
  version_header_name:
    description:
      - >-
        Name of HTTP header parameter that indicates the API Version if
        versioningScheme is set to `header`.
    type: str
  display_name:
    description:
      - Name of API Version Set
    required: true
    type: str
  versioning_scheme:
    description:
      - >-
        An value that determines where the API Version identifer will be located
        in a HTTP request.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiVersionSets
  azure_rm_apimanagementapiversionset_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetApiVersionSet
  azure_rm_apimanagementapiversionset_info:
    resource_group: myResourceGroup
    service_name: myService
    version_set_id: myApiVersionSet

'''

RETURN = '''
api_version_set:
  description: >-
    A list of dict results where the key is the name of the ApiVersionSet and
    the values are the facts for that ApiVersionSet.
  returned: always
  type: complex
  contains:
    apiversionset_name:
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
            - Api VersionSet contract properties.
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


class AzureRMApiVersionSetInfo(AzureRMModuleBase):
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
            version_set_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.version_set_id = None
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
        super(AzureRMApiVersionSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.version_set_id is not None):
            self.results['api_version_set'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['api_version_set'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_version_set.get(resource_group_name=self.resource_group,
                                                            service_name=self.service_name,
                                                            version_set_id=self.version_set_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.api_version_set.list_by_service(resource_group_name=self.resource_group,
                                                                        service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiVersionSetInfo()


if __name__ == '__main__':
    main()
