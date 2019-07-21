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
module: batchaccount
version_added: '2.9'
short_description: Manage Azure BatchAccount instance.
description:
  - 'Create, update and delete instance of Azure BatchAccount.'
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
    type: str
  name:
    description:
      - >-
        A name for the Batch account which must be unique within the region.
        Batch account names must be between 3 and 24 characters in length and
        must use only numbers and lowercase letters. This name is used as part
        of the DNS name that is used to access the Batch service in the region
        in which the account is created. For example:
        http://accountname.region.batch.azure.com/.
    required: true
    type: str
  location:
    description:
      - The region in which to create the account.
    required: true
    type: str
  auto_storage_account_id:
    description:
      - >-
        The UTC time at which storage keys were last synchronized with the Batch
        account.
    required: true
    type: datetime
  pool_allocation_mode:
    description:
      - >-
        The pool allocation mode also affects how clients may authenticate to
        the Batch Service API. If the mode is BatchService, clients may
        authenticate using access keys or Azure Active Directory. If the mode is
        UserSubscription, clients must use Azure Active Directory. The default
        is BatchService.
    type: str
  key_vault_reference:
    description:
      - A reference to the Azure key vault associated with the Batch account.
    type: dict
    suboptions:
      id:
        description:
          - >-
            The resource ID of the Azure key vault associated with the Batch
            account.
        required: true
        type: str
      url:
        description:
          - The URL of the Azure key vault associated with the Batch account.
        required: true
        type: str
  account_endpoint:
    description:
      - The account endpoint used to interact with the Batch service.
    type: str
  id:
    description:
      - The ID of the resource.
    type: str
  state:
    description:
      - Assert the state of the BatchAccount.
      - >-
        Use C(present) to create or update an BatchAccount and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: BatchAccountCreate_Default
  azure.rm.batchaccount:
    resource_group: myResourceGroup
    name: myBatchAccount
    location: japaneast
    auto_storage_account_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.Storage/storageAccounts/{{ storage_account_name }}
- name: BatchAccountCreate_BYOS
  azure.rm.batchaccount:
    resource_group: myResourceGroup
    name: myBatchAccount
    location: japaneast
    auto_storage_account_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.Storage/storageAccounts/{{ storage_account_name }}
    pool_allocation_mode: UserSubscription
    key_vault_reference:
      id: >-
        /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
        }}/providers/Microsoft.KeyVault/vaults/{{ vault_name }}
      url: 'http://sample.vault.azure.net/'
- name: BatchAccountUpdate
  azure.rm.batchaccount:
    resource_group: myResourceGroup
    name: myBatchAccount
    auto_storage_account_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.Storage/storageAccounts/{{ storage_account_name }}
- name: BatchAccountDelete
  azure.rm.batchaccount:
    resource_group: myResourceGroup
    name: myBatchAccount
    state: absent

'''

RETURN = '''
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
  contains:
    account_endpoint:
      description:
        - The account endpoint used to interact with the Batch service.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioned state of the resource
      returned: always
      type: str
      sample: null
    pool_allocation_mode:
      description:
        - ''
      returned: always
      type: str
      sample: null
    key_vault_reference:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              The resource ID of the Azure key vault associated with the Batch
              account.
          returned: always
          type: str
          sample: null
        url:
          description:
            - The URL of the Azure key vault associated with the Batch account.
          returned: always
          type: str
          sample: null
    auto_storage:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        storage_account_id:
          description:
            - >-
              The resource ID of the storage account to be used for auto-storage
              account.
          returned: always
          type: str
          sample: null
        auto_storage_account_id:
          description:
            - >-
              The UTC time at which storage keys were last synchronized with the
              Batch account.
          returned: always
          type: datetime
          sample: null
    dedicated_core_quota:
      description:
        - ''
      returned: always
      type: number
      sample: null
    low_priority_core_quota:
      description:
        - ''
      returned: always
      type: number
      sample: null
    pool_quota:
      description:
        - ''
      returned: always
      type: number
      sample: null
    active_job_and_job_schedule_quota:
      description:
        - ''
      returned: always
      type: number
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBatchAccount(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='accountName',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            auto_storage_account_id=dict(
                type='raw',
                disposition='/properties/autoStorage/storageAccountId',
                required=true,
                pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                         '/{{ resource_group }}/providers/Microsoft.Storage/storageAccounts'
                         '/{{ name }}')
            ),
            pool_allocation_mode=dict(
                type='str',
                disposition='/properties/poolAllocationMode',
                choices=['BatchService',
                         'UserSubscription']
            ),
            key_vault_reference=dict(
                type='dict',
                disposition='/properties/keyVaultReference',
                options=dict(
                    id=dict(
                        type='raw',
                        required=true,
                        pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                                 '/{{ resource_group }}/providers/Microsoft.KeyVault/vaults'
                                 '/{{ name }}')
                    ),
                    url=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMBatchAccount, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

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

        old_response = self.get_resource()

        if not old_response:
            self.log("BatchAccount instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('BatchAccount instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the BatchAccount instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('BatchAccount instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('BatchAccount instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the BatchAccount instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the BatchAccount instance.')
            self.fail('Error creating the BatchAccount instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the BatchAccount instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the BatchAccount instance.')
            self.fail('Error deleting the BatchAccount instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the BatchAccount instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("BatchAccount instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the BatchAccount instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMBatchAccount()


if __name__ == '__main__':
    main()
