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
module: azure_rm_batchaccount_info
version_added: '2.9'
short_description: Get BatchAccount info.
description:
  - Get info of BatchAccount.
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
  name:
    description:
      - The name of the Batch account.
  id:
    description:
      - The ID of the resource.
  location:
    description:
      - The location of the resource.
  account_endpoint:
    description:
      - The account endpoint used to interact with the Batch service.
  pool_allocation_mode:
    description:
      - undefined
  key_vault_reference:
    description:
      - undefined
    suboptions:
      id:
        description:
          - >-
            The resource ID of the Azure key vault associated with the Batch
            account.
        required: true
      url:
        description:
          - The URL of the Azure key vault associated with the Batch account.
        required: true
  auto_storage_account_id:
    description:
      - >-
        The UTC time at which storage keys were last synchronized with the Batch
        account.
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: BatchAccountList
  azure_rm_batchaccount_info: {}
- name: BatchAccountListByResourceGroup
  azure_rm_batchaccount_info:
    resource_group: myResourceGroup
- name: BatchAccountGet
  azure_rm_batchaccount_info:
    resource_group: myResourceGroup
    name: myBatchAccount

'''

RETURN = '''
batch_account:
  description: >-
    A list of dict results where the key is the name of the BatchAccount and the
    values are the facts for that BatchAccount.
  returned: always
  type: complex
  contains:
    batchaccount_name:
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
        location:
          description:
            - The location of the resource.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - The tags of the resource.
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"170","$type":"DictionaryType","valueType":{"$id":"171","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"172","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"173","fixed":false},"deprecated":false}]
          sample: null
        properties:
          description:
            - The properties associated with the account.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMBatchAccountInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.location = None
        self.tags = None
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
        super(AzureRMBatchAccountInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['batch_account'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['batch_account'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['batch_account'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/batchAccounts' +
                    '/{{ batch_account_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ batch_account_name }}', self.name)

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

    def listbyresourcegroup(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/batchAccounts')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ batch_account_name }}', self.name)

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

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/batchAccounts')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ batch_account_name }}', self.name)

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
    AzureRMBatchAccountInfo()


if __name__ == '__main__':
    main()
