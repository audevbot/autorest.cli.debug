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
module: azure_rm_apimanagementlogger_info
version_added: '2.9'
short_description: Get Logger info.
description:
  - Get info of Logger.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  logger_id:
    description:
      - >-
        Logger identifier. Must be unique in the API Management service
        instance.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  logger_type:
    description:
      - Logger type.
    required: true
  description:
    description:
      - Logger description.
  credentials:
    description:
      - >-
        The name and SendRule connection string of the event hub for
        azureEventHub logger.
      - Instrumentation key for applicationInsights logger.
    required: true
  is_buffered:
    description:
      - >-
        Whether records are buffered in the logger before publishing. Default is
        assumed to be true.
  resource_id:
    description:
      - >-
        Azure Resource Id of a log target (either Azure Event Hub resource or
        Azure Application Insights resource).
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListLoggers
  azure_rm_apimanagementlogger_info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetLogger
  azure_rm_apimanagementlogger_info:
    resource_group: myResourceGroup
    name: myService
    logger_id: myLogger

'''

RETURN = '''
logger:
  description: >-
    A list of dict results where the key is the name of the Logger and the
    values are the facts for that Logger.
  returned: always
  type: complex
  contains:
    logger_name:
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
            - Logger entity contract properties.
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


class AzureRMLoggerInfo(AzureRMModuleBase):
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
            logger_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.logger_id = None
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
        super(AzureRMLoggerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.logger_id is not None):
            self.results['logger'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['logger'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.logger.get(resource_group_name=self.resource_group,
                                                   service_name=self.name,
                                                   logger_id=self.logger_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.logger.list_by_service(resource_group_name=self.resource_group,
                                                               service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMLoggerInfo()


if __name__ == '__main__':
    main()
