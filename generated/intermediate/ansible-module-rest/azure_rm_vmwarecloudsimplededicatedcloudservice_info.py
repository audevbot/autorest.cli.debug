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
module: azure_rm_vmwarecloudsimplededicatedcloudservice_info
version_added: '2.9'
short_description: Get DedicatedCloudService info.
description:
  - Get info of DedicatedCloudService.
options:
  resource_group:
    description:
      - The name of the resource group
    type: str
  name:
    description:
      - '{dedicatedCloudServiceName}'
    type: str
  id:
    description:
      - >-
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
    type: str
  location:
    description:
      - Azure region
    type: str
  gateway_subnet:
    description:
      - >-
        gateway Subnet for the account. It will collect the subnet address and
        always treat it as /28
    required: true
    type: str
  is_account_onboarded:
    description:
      - indicates whether account onboarded or not in a given region
    type: str
  nodes:
    description:
      - total nodes purchased
    type: number
  service_url:
    description:
      - link to a service management web portal
    type: str
  type:
    description:
      - '{resourceProviderNamespace}/{resourceType}'
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListDedicatedCloudServices
  azure_rm_vmwarecloudsimplededicatedcloudservice_info: {}
- name: ListRGDedicatedCloudServices
  azure_rm_vmwarecloudsimplededicatedcloudservice_info:
    resource_group: myResourceGroup
- name: GetDedicatedCloudService
  azure_rm_vmwarecloudsimplededicatedcloudservice_info:
    resource_group: myResourceGroup
    name: myDedicatedCloudService

'''

RETURN = '''
dedicated_cloud_service:
  description: >-
    A list of dict results where the key is the name of the
    DedicatedCloudService and the values are the facts for that
    DedicatedCloudService.
  returned: always
  type: complex
  contains:
    dedicatedcloudservice_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - >-
              /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure region
          returned: always
          type: str
          sample: null
        name:
          description:
            - '{dedicatedCloudServiceName}'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The properties of Dedicated Node Service
          returned: always
          type: dict
          sample: null
        tags:
          description:
            - The list of tags
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"406","$type":"DictionaryType","valueType":{"$id":"407","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"408","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"409","fixed":false},"deprecated":false}]
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
          returned: always
          type: str
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMDedicatedCloudServiceInfo(AzureRMModuleBase):
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
        self.name = None
        self.properties = None
        self.tags = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDedicatedCloudServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['dedicated_cloud_service'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['dedicated_cloud_service'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['dedicated_cloud_service'] = [self.format_item(self.listbysubscription())]
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
                    '/Microsoft.VMwareCloudSimple' +
                    '/dedicatedCloudServices' +
                    '/{{ dedicated_cloud_service_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ dedicated_cloud_service_name }}', self.name)

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
                    '/Microsoft.VMwareCloudSimple' +
                    '/dedicatedCloudServices')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ dedicated_cloud_service_name }}', self.name)

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

    def listbysubscription(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.VMwareCloudSimple' +
                    '/dedicatedCloudServices')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ dedicated_cloud_service_name }}', self.name)

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
    AzureRMDedicatedCloudServiceInfo()


if __name__ == '__main__':
    main()
