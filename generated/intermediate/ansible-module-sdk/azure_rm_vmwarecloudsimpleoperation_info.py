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
module: azure_rm_vmwarecloudsimpleoperation_info
version_added: '2.9'
short_description: Get Operation info.
description:
  - Get info of Operation.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    type: str
  referer:
    description:
      - referer url
    type: str
  operation_id:
    description:
      - operation id
    type: str
  end_time:
    description:
      - End time of the operation
    type: datetime
  error:
    description:
      - Error Message if operation failed
    type: dict
    suboptions:
      code:
        description:
          - Error's code
        type: str
      message:
        description:
          - Error's message
        type: str
  id:
    description:
      - Operation Id
    type: str
  name:
    description:
      - Operation ID
    type: str
  start_time:
    description:
      - Start time of the operation
    type: datetime
  status:
    description:
      - Operation status
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListOperations
  azure_rm_vmwarecloudsimpleoperation_info: {}
- name: GetFailedOperationResult
  azure_rm_vmwarecloudsimpleoperation_info:
    region_id: myLocation
    referer: 'https://management.azure.com/'
    operation_id: myOperationResult
- name: GetOperationResult
  azure_rm_vmwarecloudsimpleoperation_info:
    region_id: myLocation
    referer: 'https://management.azure.com/'
    operation_id: myOperationResult

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
        end_time:
          description:
            - End time of the operation
          returned: always
          type: datetime
          sample: null
        error:
          description:
            - Error Message if operation failed
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - Error's code
              returned: always
              type: str
              sample: null
            message:
              description:
                - Error's message
              returned: always
              type: str
              sample: null
        id:
          description:
            - Operation Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Operation ID
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - Start time of the operation
          returned: always
          type: datetime
          sample: null
        status:
          description:
            - Operation status
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
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str'
            ),
            referer=dict(
                type='str'
            ),
            operation_id=dict(
                type='str'
            )
        )

        self.region_id = None
        self.referer = None
        self.operation_id = None
        self.end_time = None
        self.error = None
        self.id = None
        self.name = None
        self.start_time = None
        self.status = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.referer is not None and
            self.operation_id is not None):
            self.results['operations'] = self.format_item(self.get())
        else:
            self.results['operations'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.operations.get(region_id=self.region_id,
                                                       referer=self.referer,
                                                       operation_id=self.operation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

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
