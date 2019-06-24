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
module: azure_rm_apimanagementdiagnostic
version_added: '2.9'
short_description: Manage Azure Diagnostic instance.
description:
  - 'Create, update and delete instance of Azure Diagnostic.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  diagnostic_id:
    description:
      - >-
        Diagnostic identifier. Must be unique in the current API Management
        service instance.
    required: true
  always_log:
    description:
      - Specifies for what type of messages sampling settings should not apply.
  logger_id:
    description:
      - Resource Id of a target logger.
    required: true
  sampling:
    description:
      - Sampling settings for Diagnostic.
    suboptions:
      sampling_type:
        description:
          - Sampling type.
      percentage:
        description:
          - Rate of sampling for fixed-rate sampling.
  frontend:
    description:
      - Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
    suboptions:
      request:
        description:
          - Diagnostic settings for request.
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
      response:
        description:
          - Diagnostic settings for response.
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
  backend:
    description:
      - Diagnostic settings for incoming/outgoing HTTP messages to the Backend
    suboptions:
      request:
        description:
          - Diagnostic settings for request.
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
      response:
        description:
          - Diagnostic settings for response.
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
  enable_http_correlation_headers:
    description:
      - >-
        Whether to process Correlation Headers coming to Api Management Service.
        Only applicable to Application Insights diagnostics. Default is true.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  state:
    description:
      - Assert the state of the Diagnostic.
      - >-
        Use C(present) to create or update an Diagnostic and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateDiagnostic
  azure_rm_apimanagementdiagnostic:
    resource_group: myResourceGroup
    name: myService
    diagnostic_id: myDiagnostic
    always_log: allErrors
    logger_id: /loggers/azuremonitor
    sampling:
      sampling_type: fixed
      percentage: '50'
    frontend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
    backend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
- name: ApiManagementUpdateDiagnostic
  azure_rm_apimanagementdiagnostic:
    resource_group: myResourceGroup
    name: myService
    diagnostic_id: myDiagnostic
    always_log: allErrors
    logger_id: /loggers/applicationinsights
    sampling:
      sampling_type: fixed
      percentage: '50'
    frontend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
    backend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
- name: ApiManagementDeleteDiagnostic
  azure_rm_apimanagementdiagnostic:
    resource_group: myResourceGroup
    name: myService
    diagnostic_id: myDiagnostic
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
    - Diagnostic entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    always_log:
      description:
        - >-
          Specifies for what type of messages sampling settings should not
          apply.
      returned: always
      type: str
      sample: null
    logger_id:
      description:
        - Resource Id of a target logger.
      returned: always
      type: str
      sample: null
    sampling:
      description:
        - Sampling settings for Diagnostic.
      returned: always
      type: dict
      sample: null
      contains:
        sampling_type:
          description:
            - Sampling type.
          returned: always
          type: str
          sample: null
        percentage:
          description:
            - Rate of sampling for fixed-rate sampling.
          returned: always
          type: number
          sample: null
    frontend:
      description:
        - >-
          Diagnostic settings for incoming/outgoing HTTP messages to the
          Gateway.
      returned: always
      type: dict
      sample: null
      contains:
        request:
          description:
            - Diagnostic settings for request.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: number
                  sample: null
        response:
          description:
            - Diagnostic settings for response.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: number
                  sample: null
    backend:
      description:
        - Diagnostic settings for incoming/outgoing HTTP messages to the Backend
      returned: always
      type: dict
      sample: null
      contains:
        request:
          description:
            - Diagnostic settings for request.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: number
                  sample: null
        response:
          description:
            - Diagnostic settings for response.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: number
                  sample: null
    enable_http_correlation_headers:
      description:
        - >-
          Whether to process Correlation Headers coming to Api Management
          Service. Only applicable to Application Insights diagnostics. Default
          is true.
      returned: always
      type: boolean
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


class AzureRMDiagnostic(AzureRMModuleBaseExt):
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
            diagnostic_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            always_log=dict(
                type='str',
                disposition='/',
                choices=['allErrors']
            ),
            logger_id=dict(
                type='str',
                disposition='/',
                required=true
            ),
            sampling=dict(
                type='dict',
                disposition='/',
                options=dict(
                    sampling_type=dict(
                        type='str',
                        choices=['fixed']
                    ),
                    percentage=dict(
                        type='number'
                    )
                )
            ),
            frontend=dict(
                type='dict',
                disposition='/',
                options=dict(
                    request=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='number'
                                    )
                                )
                            )
                        )
                    ),
                    response=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='number'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            backend=dict(
                type='dict',
                disposition='/',
                options=dict(
                    request=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='number'
                                    )
                                )
                            )
                        )
                    ),
                    response=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='number'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            enable_http_correlation_headers=dict(
                type='boolean',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.diagnostic_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDiagnostic, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.diagnostic.create_or_update(resource_group_name=self.resource_group,
                                                                    service_name=self.name,
                                                                    diagnostic_id=self.diagnostic_id,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Diagnostic instance.')
            self.fail('Error creating the Diagnostic instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Diagnostic instance {0}'.format(self.))
        try:
            response = self.mgmt_client.diagnostic.delete(resource_group_name=self.resource_group,
                                                          service_name=self.name,
                                                          diagnostic_id=self.diagnostic_id)
        except CloudError as e:
            self.log('Error attempting to delete the Diagnostic instance.')
            self.fail('Error deleting the Diagnostic instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Diagnostic instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.diagnostic.get(resource_group_name=self.resource_group,
                                                       service_name=self.name,
                                                       diagnostic_id=self.diagnostic_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDiagnostic()


if __name__ == '__main__':
    main()
