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
module: azure_rm_vmwarecloudsimplededicatedcloudservice
version_added: '2.9'
short_description: Manage Azure DedicatedCloudService instance.
description:
  - 'Create, update and delete instance of Azure DedicatedCloudService.'
options:
  resource_group:
    description:
      - The name of the resource group
    required: true
    type: str
  name:
    description:
      - '{dedicatedCloudServiceName}'
    type: str
  location:
    description:
      - Azure region
    required: true
    type: str
  gateway_subnet:
    description:
      - >-
        gateway Subnet for the account. It will collect the subnet address and
        always treat it as /28
    required: true
    type: str
  nodes:
    description:
      - total nodes purchased
    type: number
  service_url:
    description:
      - link to a service management web portal
    type: str
  is_account_onboarded:
    description:
      - indicates whether account onboarded or not in a given region
    type: str
  id:
    description:
      - >-
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
    type: str
  type:
    description:
      - '{resourceProviderNamespace}/{resourceType}'
    type: str
  state:
    description:
      - Assert the state of the DedicatedCloudService.
      - >-
        Use C(present) to create or update an DedicatedCloudService and
        C(absent) to delete it.
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
- name: CreateDedicatedCloudService
  azure_rm_vmwarecloudsimplededicatedcloudservice:
    resource_group: myResourceGroup
    name: myDedicatedCloudService
    dedicated_cloud_service_request:
      location: westus
      properties:
        gatewaySubnet: 10.0.0.0
- name: PatchDedicatedService
  azure_rm_vmwarecloudsimplededicatedcloudservice:
    resource_group: myResourceGroup
    name: myDedicatedCloudService
    dedicated_cloud_service_request:
      tags:
        myTag: tagValue
- name: DeleteDedicatedCloudService
  azure_rm_vmwarecloudsimplededicatedcloudservice:
    resource_group: myResourceGroup
    name: myDedicatedCloudService
    state: absent

'''

RETURN = '''
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
  contains:
    gateway_subnet:
      description:
        - >-
          gateway Subnet for the account. It will collect the subnet address and
          always treat it as /28
      returned: always
      type: str
      sample: null
    is_account_onboarded:
      description:
        - indicates whether account onboarded or not in a given region
      returned: always
      type: str
      sample: null
    nodes:
      description:
        - total nodes purchased
      returned: always
      type: number
      sample: null
    service_url:
      description:
        - link to a service management web portal
      returned: always
      type: str
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedCloudService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='dedicated_cloud_service_name',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            gateway_subnet=dict(
                type='str',
                disposition='/',
                required=true
            ),
            nodes=dict(
                type='number',
                disposition='/'
            ),
            service_url=dict(
                type='str',
                disposition='/'
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
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedCloudService, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["location"] = response["location"]
           self.results["name"] = response["name"]
           self.results["properties"] = response["properties"]
           self.results["tags"] = response["tags"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.dedicated_cloud_service.create_or_update(resource_group_name=self.resource_group,
                                                                                 dedicated_cloud_service_name=self.name,
                                                                                 dedicated_cloud_service_request=self.dedicatedCloudServiceRequest)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedCloudService instance.')
            self.fail('Error creating the DedicatedCloudService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the DedicatedCloudService instance {0}'.format(self.))
        try:
            response = self.mgmt_client.dedicated_cloud_service.delete(resource_group_name=self.resource_group,
                                                                       dedicated_cloud_service_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedCloudService instance.')
            self.fail('Error deleting the DedicatedCloudService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the DedicatedCloudService instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.dedicated_cloud_service.get(resource_group_name=self.resource_group,
                                                                    dedicated_cloud_service_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedCloudService()


if __name__ == '__main__':
    main()
