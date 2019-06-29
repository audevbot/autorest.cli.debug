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
module: azure_rm_apimanagementapiexport_info
version_added: '2.9'
short_description: Get ApiExport info.
description:
  - Get info of ApiExport.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
  format:
    description:
      - >-
        Format in which to export the Api Details to the Storage Blob with Sas
        Key valid for 5 minutes.
    required: true
  export:
    description:
      - Query parameter required to export the API details.
    required: true
  id:
    description:
      - ResourceId of the API which was exported.
  value:
    description:
      - The object defining the schema of the exported Api Detail
    suboptions:
      link:
        description:
          - >-
            Link to the Storage Blob containing the result of the export
            operation. The Blob Uri is only valid for 5 minutes.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementGetApiExportInOpenApi2dot0
  azure_rm_apimanagementapiexport_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    format: swagger-link
    export: 'true'
- name: ApiManagementGetApiExportInOpenApi3dot0
  azure_rm_apimanagementapiexport_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    format: openapi-link
    export: 'true'

'''

RETURN = '''
api_export:
  description: >-
    A list of dict results where the key is the name of the ApiExport and the
    values are the facts for that ApiExport.
  returned: always
  type: complex
  contains:
    apiexport_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - ResourceId of the API which was exported.
          returned: always
          type: str
          sample: null
        format:
          description:
            - >-
              Format in which the Api Details are exported to the Storage Blob
              with Sas Key valid for 5 minutes.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The object defining the schema of the exported Api Detail
          returned: always
          type: dict
          sample: null
          contains:
            link:
              description:
                - >-
                  Link to the Storage Blob containing the result of the export
                  operation. The Blob Uri is only valid for 5 minutes.
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


class AzureRMApiExportInfo(AzureRMModuleBase):
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
            api_id=dict(
                type='str',
                required=true
            ),
            format=dict(
                type='str',
                required=true
            ),
            export=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.format = None
        self.export = None
        self.id = None
        self.value = None

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
        super(AzureRMApiExportInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None and
            self.format is not None and
            self.export is not None):
            self.results['api_export'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.api_export.get(resource_group_name=self.resource_group,
                                                       service_name=self.service_name,
                                                       api_id=self.api_id,
                                                       format=self.format,
                                                       export=self.export)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApiExportInfo()


if __name__ == '__main__':
    main()
