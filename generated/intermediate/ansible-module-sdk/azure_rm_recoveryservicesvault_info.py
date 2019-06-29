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
  name:
    description:
      - Resource name associated with the resource.
  id:
    description:
      - Resource Id represents the complete path to the resource.
  type:
    description:
      - >-
        Resource type represents the complete path of the form
        Namespace/ResourceType/ResourceType/...
  e_tag:
    description:
      - Optional ETag.
  location:
    description:
      - Resource location.
  provisioning_state:
    description:
      - Provisioning State.
  upgrade_details:
    description:
      - undefined
    suboptions:
      operation_id:
        description:
          - ID of the vault upgrade operation.
      start_time_utc:
        description:
          - UTC time at which the upgrade operation has started.
      last_updated_time_utc:
        description:
          - UTC time at which the upgrade operation status was last updated.
      end_time_utc:
        description:
          - UTC time at which the upgrade operation has ended.
      status:
        description:
          - Status of the vault upgrade operation.
      message:
        description:
          - >-
            Message to the user containing information about the upgrade
            operation.
      trigger_type:
        description:
          - The way the vault upgrade was triggered.
      upgraded_resource_id:
        description:
          - Resource ID of the upgraded vault.
      previous_resource_id:
        description:
          - Resource ID of the vault before the upgrade.
  sku_name:
    description:
      - The Sku name.
    required: true
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
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.recoveryservices import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


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

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
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

        try:
            response = self.mgmt_client.vaults.get(resource_group_name=self.resource_group,
                                                   vault_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.vaults.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbysubscriptionid(self):
        response = None

        try:
            response = self.mgmt_client.vaults.list_by_subscription_id()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMVaultsInfo()


if __name__ == '__main__':
    main()
