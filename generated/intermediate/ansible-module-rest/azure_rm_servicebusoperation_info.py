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
        type: str
      display:
        description:
          - The object that represents the operation.
        type: dict
        suboptions:
          provider:
            description:
              - 'Service provider: Microsoft.ServiceBus'
            type: str
          resource:
            description:
              - 'Resource on which the operation is performed: Invoice, etc.'
            type: str
          operation:
            description:
              - 'Operation type: Read, write, delete, etc.'
            type: str
  next_link:
    description:
      - URL to get the next set of operation list results if there are any.
    type: str
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        else:
            self.results['operations'] = [self.format_item(self.list())]
        return self.results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/providers' +
                    '/Microsoft.ServiceBus' +
                    '/operations')

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
    AzureRMOperationsInfo()


if __name__ == '__main__':
    main()
