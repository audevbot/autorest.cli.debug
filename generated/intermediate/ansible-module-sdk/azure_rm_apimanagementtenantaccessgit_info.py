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
module: azure_rm_apimanagementtenantaccessgit_info
version_added: '2.9'
short_description: Get TenantAccessGit info.
description:
  - Get info of TenantAccessGit.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  service_name:
    description:
      - The name of the API Management service.
    required: true
  name:
    description:
      - The identifier of the Access configuration.
    required: true
  id:
    description:
      - Identifier.
  primary_key:
    description:
      - Primary access key.
  secondary_key:
    description:
      - Secondary access key.
  enabled:
    description:
      - Determines whether direct access is enabled.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementGetTenantAccess
  azure_rm_apimanagementtenantaccessgit_info:
    resource_group: myResourceGroup
    service_name: myService
    name: myTenant

'''

RETURN = '''
tenant_access_git:
  description: >-
    A list of dict results where the key is the name of the TenantAccessGit and
    the values are the facts for that TenantAccessGit.
  returned: always
  type: complex
  contains:
    tenantaccessgit_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Identifier.
          returned: always
          type: str
          sample: null
        primary_key:
          description:
            - Primary access key.
          returned: always
          type: str
          sample: null
        secondary_key:
          description:
            - Secondary access key.
          returned: always
          type: str
          sample: null
        enabled:
          description:
            - Determines whether direct access is enabled.
          returned: always
          type: boolean
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTenantAccessGitInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            service_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.service_name = None
        self.name = None
        self.id = None
        self.primary_key = None
        self.secondary_key = None
        self.enabled = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTenantAccessGitInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.name is not None):
            self.results['tenant_access_git'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.tenant_access_git.get(resource_group_name=self.resource_group,
                                                              service_name=self.service_name,
                                                              access_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMTenantAccessGitInfo()


if __name__ == '__main__':
    main()
