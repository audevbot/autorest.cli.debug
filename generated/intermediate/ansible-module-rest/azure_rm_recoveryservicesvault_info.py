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
module: azure_rm_recoveryservicesvault_info
version_added: '2.9'
short_description: Get Vault info.
description:
  - Get info of Vault.
options:
  resource_group:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    type: str
  name:
    description:
      - Resource name associated with the resource.
    type: str
  id:
    description:
      - Resource Id represents the complete path to the resource.
    type: str
  type:
    description:
      - >-
        Resource type represents the complete path of the form
        Namespace/ResourceType/ResourceType/...
    type: str
  e_tag:
    description:
      - Optional ETag.
    type: str
  location:
    description:
      - Resource location.
    type: str
  provisioning_state:
    description:
      - Provisioning State.
    type: str
  upgrade_details:
    description:
      - undefined
    type: dict
    suboptions:
      operation_id:
        description:
          - ID of the vault upgrade operation.
        type: str
      start_time_utc:
        description:
          - UTC time at which the upgrade operation has started.
        type: datetime
      last_updated_time_utc:
        description:
          - UTC time at which the upgrade operation status was last updated.
        type: datetime
      end_time_utc:
        description:
          - UTC time at which the upgrade operation has ended.
        type: datetime
      status:
        description:
          - Status of the vault upgrade operation.
        type: str
      message:
        description:
          - >-
            Message to the user containing information about the upgrade
            operation.
        type: str
      trigger_type:
        description:
          - The way the vault upgrade was triggered.
        type: str
      upgraded_resource_id:
        description:
          - Resource ID of the upgraded vault.
        type: str
      previous_resource_id:
        description:
          - Resource ID of the vault before the upgrade.
        type: str
  sku_name:
    description:
      - The Sku name.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List of Recovery Services Resources in SubscriptionId
  azure_rm_recoveryservicesvault_info: {}
- name: List of Recovery Services Resources in ResourceGroup
  azure_rm_recoveryservicesvault_info:
    resource_group: myResourceGroup
- name: Get Recovery Services Resource
  azure_rm_recoveryservicesvault_info:
    resource_group: myResourceGroup
    name: myVault

'''

RETURN = '''
vaults:
  description: >-
    A list of dict results where the key is the name of the Vault and the values
    are the facts for that Vault.
  returned: always
  type: complex
  contains:
    vault_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id represents the complete path to the resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name associated with the resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - >-
              Resource type represents the complete path of the form
              Namespace/ResourceType/ResourceType/...
          returned: always
          type: str
          sample: null
        e_tag:
          description:
            - Optional ETag.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags.
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"187","$type":"DictionaryType","valueType":{"$id":"188","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"189","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"190","fixed":false},"deprecated":false}]
          sample: null
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null
        sku:
          description:
            - ''
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


class AzureRMVaultsInfo(AzureRMModuleBase):
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
        self.name = None
        self.type = None
        self.e_tag = None
        self.location = None
        self.tags = None
        self.properties = None
        self.sku = None

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
        super(AzureRMVaultsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['vaults'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['vaults'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['vaults'] = [self.format_item(self.listbysubscriptionid())]
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
                    '/Microsoft.RecoveryServices' +
                    '/vaults' +
                    '/{{ vault_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.name)

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
                    '/Microsoft.RecoveryServices' +
                    '/vaults')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.name)

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

    def listbysubscriptionid(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.RecoveryServices' +
                    '/vaults')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.name)

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
    AzureRMVaultsInfo()


if __name__ == '__main__':
    main()
