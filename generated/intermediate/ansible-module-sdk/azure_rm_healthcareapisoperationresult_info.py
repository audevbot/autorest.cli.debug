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
module: azure_rm_healthcareapisoperationresult_info
version_added: '2.9'
short_description: Get OperationResult info.
description:
  - Get info of OperationResult.
options:
  location_name:
    description:
      - The location of the operation.
    required: true
    type: str
  operation_result_id:
    description:
      - The ID of the operation result to get.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Get operation result
  azure_rm_healthcareapisoperationresult_info:
    location_name: myLocation
    operation_result_id: myOperationresult

'''

RETURN = '''
operation_results:
  description: >-
    A list of dict results where the key is the name of the OperationResult and
    the values are the facts for that OperationResult.
  returned: always
  type: complex
  contains:
    operationresult_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains: {}

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.healthcareapis import HealthCareApisClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationResultsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location_name=dict(
                type='str',
                required=true
            ),
            operation_result_id=dict(
                type='str',
                required=true
            )
        )

        self.location_name = None
        self.operation_result_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-09-16'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationResultsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HealthCareApisClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.location_name is not None and
            self.operation_result_id is not None):
            self.results['operation_results'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.operation_results.get(location_name=self.location_name,
                                                              operation_result_id=self.operation_result_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMOperationResultsInfo()


if __name__ == '__main__':
    main()
