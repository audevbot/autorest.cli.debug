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
module: azure_rm_servicebusoperation_info
version_added: '2.9'
short_description: Get Operation info.
description:
  - Get info of Operation.
options:
  value:
    description:
      - >-
        List of ServiceBus operations supported by the Microsoft.ServiceBus
        resource provider.
    type: list
    suboptions:
      name:
        description:
          - 'Operation name: {provider}/{resource}/{operation}'
      display:
        description:
          - The object that represents the operation.
        suboptions:
          provider:
            description:
              - 'Service provider: Microsoft.ServiceBus'
          resource:
            description:
              - 'Resource on which the operation is performed: Invoice, etc.'
          operation:
            description:
              - 'Operation type: Read, write, delete, etc.'
  next_link:
    description:
      - URL to get the next set of operation list results if there are any.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: OperationsList
  azure_rm_servicebusoperation_info: {}

'''

RETURN = '''
operations:
  description: >-
    A list of dict results where the key is the name of the Operation and the
    values are the facts for that Operation.
  returned: always
  type: complex
  contains:
    operation_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - >-
              List of ServiceBus operations supported by the
              Microsoft.ServiceBus resource provider.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - 'Operation name: {provider}/{resource}/{operation}'
              returned: always
              type: str
              sample: null
            display:
              description:
                - The object that represents the operation.
              returned: always
              type: dict
              sample: null
              contains:
                provider:
                  description:
                    - 'Service provider: Microsoft.ServiceBus'
                  returned: always
                  type: str
                  sample: null
                resource:
                  description:
                    - >-
                      Resource on which the operation is performed: Invoice,
                      etc.
                  returned: always
                  type: str
                  sample: null
                operation:
                  description:
                    - 'Operation type: Read, write, delete, etc.'
                  returned: always
                  type: str
                  sample: null
        next_link:
          description:
            - >-
              URL to get the next set of operation list results if there are
              any.
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )

        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        else:
            self.results['operations'] = [self.format_item(self.list())]
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.operations.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMOperationsInfo()


if __name__ == '__main__':
    main()
