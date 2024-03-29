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
module: apimanagementapidiagnostic_info
version_added: '2.9'
short_description: Get ApiDiagnostic info.
description:
  - Get info of ApiDiagnostic.
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
  api_id:
    description:
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
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
- name: ApiManagementListApiDiagnostics
  azure.rm.apimanagementapidiagnostic.info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
- name: ApiManagementGetApiDiagnostic
  azure.rm.apimanagementapidiagnostic.info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    diagnostic_id: myDiagnostic

'''

RETURN = '''
api_diagnostic:
  description: >-
    A list of dict results where the key is the name of the ApiDiagnostic and
    the values are the facts for that ApiDiagnostic.
  returned: always
  type: complex
  contains:
    apidiagnostic_name:
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMApiDiagnosticInfo(AzureRMModuleBase):
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
            diagnostic_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
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
        super(AzureRMApiDiagnosticInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None and
            self.diagnostic_id is not None):
            self.results['api_diagnostic'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None):
            self.results['api_diagnostic'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/apis' +
                    '/{{ api_name }}' +
                    '/diagnostics' +
                    '/{{ diagnostic_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.api_name)
        self.url = self.url.replace('{{ diagnostic_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbyservice(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/apis' +
                    '/{{ api_name }}' +
                    '/diagnostics')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.api_name)
        self.url = self.url.replace('{{ diagnostic_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMApiDiagnosticInfo()


if __name__ == '__main__':
    main()
