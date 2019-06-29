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
module: azure_rm_batchoperation_info
version_added: '2.9'
short_description: Get Operation info.
description:
  - Get info of Operation.
options:
  value:
    description:
      - undefined
    type: list
    suboptions:
      name:
        description:
          - 'This is of the format {provider}/{resource}/{operation}'
      display:
        description:
          - undefined
        suboptions:
          provider:
            description:
              - undefined
          operation:
            description:
              - 'For example: read, write, delete, or listKeys/action'
          resource:
            description:
              - undefined
          description:
            description:
              - undefined
      origin:
        description:
          - undefined
  next_link:
    description:
      - undefined
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
[]

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
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - 'This is of the format {provider}/{resource}/{operation}'
              returned: always
              type: str
              sample: null
            display:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                provider:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
                operation:
                  description:
                    - 'For example: read, write, delete, or listKeys/action'
                  returned: always
                  type: str
                  sample: null
                resource:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
            origin:
              description:
                - ''
              returned: always
              type: str
              sample: null
            properties:
              description:
                - ''
              returned: always
              type: 'unknown-primary[object]'
              sample: null
        next_link:
          description:
            - ''
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
        self.query_parameters['api-version'] = '2018-12-01'
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
                    '/Microsoft.Batch' +
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
