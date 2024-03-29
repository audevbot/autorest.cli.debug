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
module: azure_rm_apimanagementdiagnostic_info
version_added: '2.9'
short_description: Get Diagnostic info.
description:
  - Get info of Diagnostic.
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
  diagnostic_id:
    description:
      - >-
        Diagnostic identifier. Must be unique in the current API Management
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
  always_log:
    description:
      - Specifies for what type of messages sampling settings should not apply.
    type: str
  logger_id:
    description:
      - Resource Id of a target logger.
    required: true
    type: str
  sampling:
    description:
      - Sampling settings for Diagnostic.
    type: dict
    suboptions:
      sampling_type:
        description:
          - Sampling type.
        type: str
      percentage:
        description:
          - Rate of sampling for fixed-rate sampling.
        type: number
  frontend:
    description:
      - Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
    type: dict
    suboptions:
      request:
        description:
          - Diagnostic settings for request.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: number
      response:
        description:
          - Diagnostic settings for response.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: number
  backend:
    description:
      - Diagnostic settings for incoming/outgoing HTTP messages to the Backend
    type: dict
    suboptions:
      request:
        description:
          - Diagnostic settings for request.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: number
      response:
        description:
          - Diagnostic settings for response.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: number
  enable_http_correlation_headers:
    description:
      - >-
        Whether to process Correlation Headers coming to Api Management Service.
        Only applicable to Application Insights diagnostics. Default is true.
    type: boolean
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListDiagnostics
  azure_rm_apimanagementdiagnostic_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetDiagnostic
  azure_rm_apimanagementdiagnostic_info:
    resource_group: myResourceGroup
    service_name: myService
    diagnostic_id: myDiagnostic

'''

RETURN = '''
diagnostic:
  description: >-
    A list of dict results where the key is the name of the Diagnostic and the
    values are the facts for that Diagnostic.
  returned: always
  type: complex
  contains:
    diagnostic_name:
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
            - Diagnostic entity contract properties.
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


class AzureRMDiagnosticInfo(AzureRMModuleBase):
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
            diagnostic_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.diagnostic_id = None
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
        super(AzureRMDiagnosticInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.diagnostic_id is not None):
            self.results['diagnostic'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['diagnostic'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.diagnostic.get(resource_group_name=self.resource_group,
                                                       service_name=self.service_name,
                                                       diagnostic_id=self.diagnostic_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.diagnostic.list_by_service(resource_group_name=self.resource_group,
                                                                   service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMDiagnosticInfo()


if __name__ == '__main__':
    main()
