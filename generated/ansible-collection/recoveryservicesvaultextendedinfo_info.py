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
module: recoveryservicesvaultextendedinfo_info
version_added: '2.9'
short_description: Get VaultExtendedInfo info.
description:
  - Get info of VaultExtendedInfo.
options:
  resource_group:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
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
  integrity_key:
    description:
      - Integrity key.
    type: str
  encryption_key:
    description:
      - Encryption key.
    type: str
  encryption_key_thumbprint:
    description:
      - Encryption key thumbprint.
    type: str
  algorithm:
    description:
      - Algorithm for Vault ExtendedInfo
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Get ExtendedInfo of Resource
  azure.rm.recoveryservicesvaultextendedinfo.info:
    resource_group: myResourceGroup
    name: myVault

'''

RETURN = '''
vault_extended_info:
  description: >-
    A list of dict results where the key is the name of the VaultExtendedInfo
    and the values are the facts for that VaultExtendedInfo.
  returned: always
  type: complex
  contains:
    vaultextendedinfo_name:
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
        properties:
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


class AzureRMVaultExtendedInfoInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.e_tag = None
        self.properties = None

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
        super(AzureRMVaultExtendedInfoInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['vault_extended_info'] = self.format_item(self.get())
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
                    '/{{ vault_name }}' +
                    '/extendedInformation' +
                    '/{{ extended_information_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ extended_information_name }}', self.name)

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
    AzureRMVaultExtendedInfoInfo()


if __name__ == '__main__':
    main()
