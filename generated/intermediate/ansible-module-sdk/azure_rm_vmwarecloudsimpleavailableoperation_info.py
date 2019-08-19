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
module: azure_rm_vmwarecloudsimpleavailableoperation_info
version_added: '2.9'
short_description: Get AvailableOperation info.
description:
  - Get info of AvailableOperation.
options:
  next_link:
    description:
      - Link for next list of available operations
    type: str
  value:
    description:
      - Returns a list of available operations
    type: list
    suboptions:
      display:
        description:
          - The list of operations
        type: dict
        suboptions:
          description:
            description:
              - Description of the operation for display purposes
            type: str
          operation:
            description:
              - Name of the operation for display purposes
            type: str
          provider:
            description:
              - Name of the provider for display purposes
            type: str
          resource:
            description:
              - Name of the resource type for display purposes
            type: str
      is_data_action:
        description:
          - Indicating whether the operation is a data action or not
        type: boolean
      name:
        description:
          - >-
            {resourceProviderNamespace}/{resourceType}/{read|write|delete|action}
        type: str
      origin:
        description:
          - The origin of operation
        type: str
      service_specification:
        description:
          - The list of specification's service metrics
        type: dict
        suboptions:
          metric_specifications:
            description:
              - Metric specifications of operation
            type: list
            suboptions:
              aggregation_type:
                description:
                  - 'Metric''s aggregation type for e.g. (Average, Total)'
                required: true
                type: str
              display_description:
                description:
                  - Metric's description
                required: true
                type: str
              display_name:
                description:
                  - Human readable metric's name
                required: true
                type: str
              name:
                description:
                  - Metric's name/id
                required: true
                type: str
              unit:
                description:
                  - Metric's unit
                required: true
                type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListOperations
  azure_rm_vmwarecloudsimpleavailableoperation_info: {}

'''

RETURN = '''
available_operations:
  description: >-
    A list of dict results where the key is the name of the AvailableOperation
    and the values are the facts for that AvailableOperation.
  returned: always
  type: complex
  contains:
    availableoperation_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - Link for next list of available operations
          returned: always
          type: str
          sample: null
        value:
          description:
            - Returns a list of available operations
          returned: always
          type: dict
          sample: null
          contains:
            display:
              description:
                - The list of operations
              returned: always
              type: dict
              sample: null
              contains:
                description:
                  description:
                    - Description of the operation for display purposes
                  returned: always
                  type: str
                  sample: null
                operation:
                  description:
                    - Name of the operation for display purposes
                  returned: always
                  type: str
                  sample: null
                provider:
                  description:
                    - Name of the provider for display purposes
                  returned: always
                  type: str
                  sample: null
                resource:
                  description:
                    - Name of the resource type for display purposes
                  returned: always
                  type: str
                  sample: null
            is_data_action:
              description:
                - Indicating whether the operation is a data action or not
              returned: always
              type: boolean
              sample: null
            name:
              description:
                - >-
                  {resourceProviderNamespace}/{resourceType}/{read|write|delete|action}
              returned: always
              type: str
              sample: null
            origin:
              description:
                - The origin of operation
              returned: always
              type: str
              sample: null
            properties:
              description:
                - The list of operation properties
              returned: always
              type: dict
              sample: null
            service_specification:
              description:
                - The list of specification's service metrics
              returned: always
              type: dict
              sample: null
              contains:
                metric_specifications:
                  description:
                    - Metric specifications of operation
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    aggregation_type:
                      description:
                        - 'Metric''s aggregation type for e.g. (Average, Total)'
                      returned: always
                      type: str
                      sample: null
                    display_description:
                      description:
                        - Metric's description
                      returned: always
                      type: str
                      sample: null
                    display_name:
                      description:
                        - Human readable metric's name
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - Metric's name/id
                      returned: always
                      type: str
                      sample: null
                    unit:
                      description:
                        - Metric's unit
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


class AzureRMAvailableOperationsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )

        self.next_link = None
        self.value = None

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
        super(AzureRMAvailableOperationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        else:
            self.results['available_operations'] = [self.format_item(self.list())]
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.available_operations.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMAvailableOperationsInfo()


if __name__ == '__main__':
    main()
