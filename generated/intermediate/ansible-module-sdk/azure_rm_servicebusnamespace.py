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
module: azure_rm_servicebusnamespace
version_added: '2.9'
short_description: Manage Azure Namespace instance.
description:
  - 'Create, update and delete instance of Azure Namespace.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  name:
    description:
      - Resource name
    type: str
  location:
    description:
      - The Geo-location where the resource lives
    required: true
    type: str
  sku:
    description:
      - Properties of Sku
    type: dict
    suboptions:
      name:
        description:
          - Name of this SKU.
        required: true
        type: str
      tier:
        description:
          - The billing tier of this particular SKU.
        type: str
      capacity:
        description:
          - >-
            The specified messaging units for the tier. For Premium tier,
            capacity are 1,2 and 4.
        type: number
  provisioning_state:
    description:
      - Provisioning state of the namespace.
    type: str
  created_at:
    description:
      - The time the namespace was created.
    type: datetime
  updated_at:
    description:
      - The time the namespace was updated.
    type: datetime
  service_bus_endpoint:
    description:
      - Endpoint you can use to perform Service Bus operations.
    type: str
  metric_id:
    description:
      - Identifier for Azure Insights metrics
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  state:
    description:
      - Assert the state of the Namespace.
      - >-
        Use C(present) to create or update an Namespace and C(absent) to delete
        it.
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
- name: NameSpaceCreate
  azure_rm_servicebusnamespace:
    resource_group: myResourceGroup
    name: my
    location: South Central US
    tags:
      tag1: value1
      tag2: value2
    sku:
      name: Standard
      tier: Standard
- name: NameSpaceUpdate
  azure_rm_servicebusnamespace:
    resource_group: myResourceGroup
    name: my
    location: South Central US
    tags:
      tag3: value3
      tag4: value4
- name: NameSpaceDelete
  azure_rm_servicebusnamespace:
    resource_group: myResourceGroup
    name: my
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - The Geo-location where the resource lives
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"13","$type":"DictionaryType","valueType":{"$id":"14","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"15","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"16","fixed":false},"deprecated":false}]
  sample: null
sku:
  description:
    - Properties of Sku
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of this SKU.
      returned: always
      type: str
      sample: null
    tier:
      description:
        - The billing tier of this particular SKU.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - >-
          The specified messaging units for the tier. For Premium tier, capacity
          are 1,2 and 4.
      returned: always
      type: number
      sample: null
properties:
  description:
    - Properties of the namespace.
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_state:
      description:
        - Provisioning state of the namespace.
      returned: always
      type: str
      sample: null
    created_at:
      description:
        - The time the namespace was created.
      returned: always
      type: datetime
      sample: null
    updated_at:
      description:
        - The time the namespace was updated.
      returned: always
      type: datetime
      sample: null
    service_bus_endpoint:
      description:
        - Endpoint you can use to perform Service Bus operations.
      returned: always
      type: str
      sample: null
    metric_id:
      description:
        - Identifier for Azure Insights metrics
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNamespaces(AzureRMModuleBaseExt):
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
                disposition='namespace_name',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            sku=dict(
                type='dict',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str',
                        choices=['Basic',
                                 'Standard',
                                 'Premium'],
                        required=true
                    ),
                    tier=dict(
                        type='str',
                        choices=['Basic',
                                 'Standard',
                                 'Premium']
                    ),
                    capacity=dict(
                        type='number'
                    )
                )
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

        super(AzureRMNamespaces, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
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
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["sku"] = response["sku"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.namespaces.create_or_update(resource_group_name=self.resource_group,
                                                                    namespace_name=self.name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Namespace instance.')
            self.fail('Error creating the Namespace instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Namespace instance {0}'.format(self.))
        try:
            response = self.mgmt_client.namespaces.delete(resource_group_name=self.resource_group,
                                                          namespace_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Namespace instance.')
            self.fail('Error deleting the Namespace instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Namespace instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.namespaces.get(resource_group_name=self.resource_group,
                                                       namespace_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNamespaces()


if __name__ == '__main__':
    main()
