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
module: azure_rm_apimanagementnetworkstatu_info
version_added: '2.9'
short_description: Get NetworkStatu info.
description:
  - Get info of NetworkStatu.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  name:
    description:
      - >-
        Location in which the API Management service is deployed. This is one of
        the Azure Regions like West US, East US, South Central US.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementServiceGetNetworkStatus
  azure_rm_apimanagementnetworkstatu_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementServiceGetNetworkStatusByLocation
  azure_rm_apimanagementnetworkstatu_info:
    resource_group: myResourceGroup
    service_name: myService
    name: myLocation

'''

RETURN = '''
network_status:
  description: >-
    A list of dict results where the key is the name of the NetworkStatu and the
    values are the facts for that NetworkStatu.
  returned: always
  type: complex
  contains:
    networkstatu_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains: {}

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


class AzureRMNetworkStatusInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.name = None

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
        super(AzureRMNetworkStatusInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.name is not None):
            self.results['network_status'] = self.format_item(self.listbylocation())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['network_status'] = self.format_item(self.listbyservice())
        return self.results

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.network_status.list_by_location(resource_group_name=self.resource_group,
                                                                        service_name=self.service_name,
                                                                        location_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.network_status.list_by_service(resource_group_name=self.resource_group,
                                                                       service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMNetworkStatusInfo()


if __name__ == '__main__':
    main()
