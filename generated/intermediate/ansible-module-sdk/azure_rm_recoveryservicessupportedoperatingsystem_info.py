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
module: azure_rm_recoveryservicessupportedoperatingsystem_info
version_added: '2.9'
short_description: Get SupportedOperatingSystem info.
description:
  - Get info of SupportedOperatingSystem.
options:
  resource_name:
    description:
      - The name of the recovery services vault.
    required: true
  name:
    description:
      - Resource Name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource Type
  location:
    description:
      - Resource Location
  supported_os_list:
    description:
      - The supported OS List.
    type: list
    suboptions:
      instance_type:
        description:
          - Gets the replication provider type.
      supported_os:
        description:
          - List of supported OS.
        type: list
        suboptions:
          os_name:
            description:
              - The name.
          os_type:
            description:
              - The type.
          os_versions:
            description:
              - List of version for OS.
            type: list
            suboptions:
              version:
                description:
                  - The version.
              service_pack:
                description:
                  - Service pack.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the data of supported OSes by SRS.
  azure_rm_recoveryservicessupportedoperatingsystem_info:
    resource_name: myVault
    name: myResourceGroup

'''

RETURN = '''
supported_operating_systems:
  description: >-
    A list of dict results where the key is the name of the
    SupportedOperatingSystem and the values are the facts for that
    SupportedOperatingSystem.
  returned: always
  type: complex
  contains:
    supportedoperatingsystem_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource Name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource Type
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource Location
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties model for supported OS API.
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


class AzureRMSupportedOperatingSystemsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-10'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSupportedOperatingSystemsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.name is not None):
            self.results['supported_operating_systems'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.supported_operating_systems.get(resource_name=self.resource_name,
                                                                        resource_group_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMSupportedOperatingSystemsInfo()


if __name__ == '__main__':
    main()
