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
module: azure_rm_recoveryservicesvaultextendedinfo_info
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
  integrity_key:
    description:
      - Integrity key.
  encryption_key:
    description:
      - Encryption key.
  encryption_key_thumbprint:
    description:
      - Encryption key thumbprint.
  algorithm:
    description:
      - Algorithm for Vault ExtendedInfo
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Get ExtendedInfo of Resource
  azure_rm_recoveryservicesvaultextendedinfo_info:
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
            - !<tag:yaml.org,2002:js/undefined> ''
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

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['vault_extended_info'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vault_extended_info.get(resource_group_name=self.resource_group,
                                                                vault_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMVaultExtendedInfoInfo()


if __name__ == '__main__':
    main()
