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
module: azure_rm_batchapplicationpackage_info
version_added: '2.9'
short_description: Get ApplicationPackage info.
description:
  - Get info of ApplicationPackage.
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
  account_name:
    description:
      - The name of the Batch account.
    required: true
  application_name:
    description:
      - The name of the application. This must be unique within the account.
    required: true
  maxresults:
    description:
      - The maximum number of items to return in the response.
  name:
    description:
      - The version of the application.
  id:
    description:
      - The ID of the resource.
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
  state:
    description:
      - The current state of the application package.
  format:
    description:
      - 'The format of the application package, if the package is active.'
  storage_url:
    description:
      - The URL for the application package in Azure Storage.
  storage_url_expiry:
    description:
      - The UTC time at which the Azure Storage URL will expire.
  last_activation_time:
    description:
      - >-
        The time at which the package was last activated, if the package is
        active.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApplicationList
  azure_rm_batchapplicationpackage_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    application_name: myApplication
- name: ApplicationPackageGet
  azure_rm_batchapplicationpackage_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    application_name: myApplication
    name: myVersion

'''

RETURN = '''
application_package:
  description: >-
    A list of dict results where the key is the name of the ApplicationPackage
    and the values are the facts for that ApplicationPackage.
  returned: always
  type: complex
  contains:
    applicationpackage_name:
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
            - The properties associated with the Application Package.
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


class AzureRMApplicationPackageInfo(AzureRMModuleBase):
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
            application_name=dict(
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
        self.application_name = None
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
        super(AzureRMApplicationPackageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.application_name is not None and
            self.name is not None):
            self.results['application_package'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.account_name is not None and
              self.application_name is not None):
            self.results['application_package'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.application_package.get(resource_group_name=self.resource_group,
                                                                account_name=self.account_name,
                                                                application_name=self.application_name,
                                                                version_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.application_package.list(resource_group_name=self.resource_group,
                                                                 account_name=self.account_name,
                                                                 application_name=self.application_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMApplicationPackageInfo()


if __name__ == '__main__':
    main()
