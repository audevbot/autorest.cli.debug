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
module: azure_rm_recoveryservicesoperation_info
version_added: '2.9'
short_description: Get Operation info.
description:
  - Get info of Operation.
options:
  value:
    description:
      - List of available operations.
    type: list
    suboptions:
      name:
        description:
          - Name of the Operation.
        type: str
      display:
        description:
          - >-
            Contains the localized display information for this particular
            operation
        type: dict
        suboptions:
          provider:
            description:
              - Name of the provider for display purposes
            type: str
          resource:
            description:
              - ResourceType for which this Operation can be performed.
            type: str
          operation:
            description:
              - Operations Name itself.
            type: str
          description:
            description:
              - >-
                Description of the operation having details of what operation is
                about.
            type: str
      origin:
        description:
          - >-
            The intended executor of the operation;governs the display of the
            operation in the RBAC UX and the audit logs UX
        type: str
      service_specification:
        description:
          - Operation properties.
        type: dict
        suboptions:
          log_specifications:
            description:
              - List of log specifications of this operation.
            type: list
            suboptions:
              name:
                description:
                  - Name of the log.
                type: str
              display_name:
                description:
                  - Localized display name
                type: str
              blob_duration:
                description:
                  - Blobs created in customer storage account per hour
                type: str
  next_link:
    description:
      - Link to the next chunk of the response
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListOperations
  azure_rm_recoveryservicesoperation_info: {}

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
            - List of available operations.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the Operation.
              returned: always
              type: str
              sample: null
            display:
              description:
                - >-
                  Contains the localized display information for this particular
                  operation
              returned: always
              type: dict
              sample: null
              contains:
                provider:
                  description:
                    - Name of the provider for display purposes
                  returned: always
                  type: str
                  sample: null
                resource:
                  description:
                    - ResourceType for which this Operation can be performed.
                  returned: always
                  type: str
                  sample: null
                operation:
                  description:
                    - Operations Name itself.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - >-
                      Description of the operation having details of what
                      operation is about.
                  returned: always
                  type: str
                  sample: null
            origin:
              description:
                - >-
                  The intended executor of the operation;governs the display of
                  the operation in the RBAC UX and the audit logs UX
              returned: always
              type: str
              sample: null
            properties:
              description:
                - ShoeBox properties for the given operation.
              returned: always
              type: dict
              sample: null
            service_specification:
              description:
                - Operation properties.
              returned: always
              type: dict
              sample: null
              contains:
                log_specifications:
                  description:
                    - List of log specifications of this operation.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    name:
                      description:
                        - Name of the log.
                      returned: always
                      type: str
                      sample: null
                    display_name:
                      description:
                        - Localized display name
                      returned: always
                      type: str
                      sample: null
                    blob_duration:
                      description:
                        - Blobs created in customer storage account per hour
                      returned: always
                      type: str
                      sample: null
        next_link:
          description:
            - Link to the next chunk of the response
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
    from azure.mgmt.recoveryservices import RecoveryServicesClient
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
        self.query_parameters['api-version'] = '2016-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
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
