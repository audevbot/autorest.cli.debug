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
module: azure_rm_apimanagementopenidconnectprovider_info
version_added: '2.9'
short_description: Get OpenIdConnectProvider info.
description:
  - Get info of OpenIdConnectProvider.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  opid:
    description:
      - Identifier of the OpenID Connect Provider.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  display_name:
    description:
      - User-friendly OpenID Connect Provider name.
    required: true
  description:
    description:
      - User-friendly description of OpenID Connect Provider.
  metadata_endpoint:
    description:
      - Metadata endpoint URI.
    required: true
  client_id:
    description:
      - Client ID of developer console which is the client application.
    required: true
  client_secret:
    description:
      - Client Secret of developer console which is the client application.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListOpenIdConnectProviders
  azure_rm_apimanagementopenidconnectprovider_info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetOpenIdConnectProvider
  azure_rm_apimanagementopenidconnectprovider_info:
    resource_group: myResourceGroup
    name: myService
    opid: myOpenidConnectProvider

'''

RETURN = '''
open_id_connect_provider:
  description: >-
    A list of dict results where the key is the name of the
    OpenIdConnectProvider and the values are the facts for that
    OpenIdConnectProvider.
  returned: always
  type: complex
  contains:
    openidconnectprovider_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type for API Management resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - OpenId Connect Provider contract properties.
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOpenIdConnectProviderInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            ),
            opid=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.opid = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None

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
        super(AzureRMOpenIdConnectProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.opid is not None):
            self.results['open_id_connect_provider'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['open_id_connect_provider'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.open_id_connect_provider.get(resource_group_name=self.resource_group,
                                                                     service_name=self.name,
                                                                     opid=self.opid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.open_id_connect_provider.list_by_service(resource_group_name=self.resource_group,
                                                                                 service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMOpenIdConnectProviderInfo()


if __name__ == '__main__':
    main()
