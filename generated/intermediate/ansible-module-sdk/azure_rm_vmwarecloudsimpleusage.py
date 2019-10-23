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
module: azure_rm_vmwarecloudsimpleusage
version_added: '2.9'
short_description: Manage Azure Usage instance.
description:
  - 'Create, update and delete instance of Azure Usage.'
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  next_link:
    description:
      - Link for next list of DedicatedCloudNode
    type: str
  value:
    description:
      - The list of usages
    type: list
    suboptions:
      current_value:
        description:
          - The current usage value
        required: true
        type: number
      limit:
        description:
          - >-
            limit of a given sku in a region for a subscription. The maximum
            permitted value for the usage quota. If there is no limit, this
            value will be -1
        required: true
        type: number
      name:
        description:
          - Usage name value and localized name
        type: dict
        suboptions:
          localized_value:
            description:
              - e.g. "Virtual Machines"
            type: str
          value:
            description:
              - 'resource type or resource type sku name, e.g. virtualMachines'
            type: str
      unit:
        description:
          - The usages' unit
        type: str
  state:
    description:
      - Assert the state of the Usage.
      - Use C(present) to create or update an Usage and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
[]

'''

RETURN = '''
next_link:
  description:
    - Link for next list of DedicatedCloudNode
  returned: always
  type: str
  sample: null
value:
  description:
    - The list of usages
  returned: always
  type: dict
  sample: null
  contains:
    current_value:
      description:
        - The current usage value
      returned: always
      type: number
      sample: null
    limit:
      description:
        - >-
          limit of a given sku in a region for a subscription. The maximum
          permitted value for the usage quota. If there is no limit, this value
          will be -1
      returned: always
      type: number
      sample: null
    name:
      description:
        - Usage name value and localized name
      returned: always
      type: dict
      sample: null
      contains:
        localized_value:
          description:
            - e.g. "Virtual Machines"
          returned: always
          type: str
          sample: null
        value:
          description:
            - 'resource type or resource type sku name, e.g. virtualMachines'
          returned: always
          type: str
          sample: null
    unit:
      description:
        - The usages' unit
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


class AzureRMUsages(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.region_id = None
        self.next_link = None
        self.value = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMUsages, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        if self.location is None:
            self.location = resource_group.location

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
           self.results["next_link"] = response["next_link"]
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.usages.create()
            else:
                response = self.mgmt_client.usages.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Usage instance.')
            self.fail('Error creating the Usage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Usage instance {0}'.format(self.))
        try:
            response = self.mgmt_client.usages.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Usage instance.')
            self.fail('Error deleting the Usage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Usage instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.usages.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMUsages()


if __name__ == '__main__':
    main()
