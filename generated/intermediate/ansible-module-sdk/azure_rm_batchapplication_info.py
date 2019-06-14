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
module: azure_rm_batchapplication_info
version_added: '2.9'
short_description: Get Application info.
description:
  - Get info of Application.
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
  account_name:
    description:
      - The name of the Batch account.
    required: true
  maxresults:
    description:
      - The maximum number of items to return in the response.
  name:
    description:
      - The name of the application. This must be unique within the account.
  id:
    description:
      - The ID of the resource.
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
  display_name:
    description:
      - The display name for the application.
  allow_updates:
    description:
      - >-
        A value indicating whether packages within the application may be
        overwritten using the same version string.
  default_version:
    description:
      - >-
        The package to use if a client requests the application but does not
        specify a version. This property can only be set to the name of an
        existing package.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApplicationList
  azure_rm_batchapplication_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
- name: ApplicationGet
  azure_rm_batchapplication_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myApplication

'''

RETURN = '''
application:
  description: >-
    A list of dict results where the key is the name of the Application and the
    values are the facts for that Application.
  returned: always
  type: complex
  contains:
    application_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - The ID of the resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - 'The ETag of the resource, used for concurrency statements.'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The properties associated with the Application.
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
    from azure.mgmt.batch import BatchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMApplicationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            account_name=dict(
                type='str',
                required=true
            ),
            maxresults=dict(
                type='number'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.account_name = None
        self.maxresults = None
        self.name = None
        self.id = None
        self.etag = None
        self.properties = None

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
        super(AzureRMApplicationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.name is not None):
            self.results['application'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['application'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.application.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        application_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.application.list(resource_group_name=self.resource_group,
                                                         account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApplicationInfo()


if __name__ == '__main__':
    main()
