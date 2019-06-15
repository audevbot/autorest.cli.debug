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
module: azure_rm_frontdoorloadbalancingsetting
version_added: '2.9'
short_description: Manage Azure LoadBalancingSetting instance.
description:
  - 'Create, update and delete instance of Azure LoadBalancingSetting.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
  name:
    description:
      - Resource name.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type.
  state:
    description:
      - Assert the state of the LoadBalancingSetting.
      - >-
        Use C(present) to create or update an LoadBalancingSetting and C(absent)
        to delete it.
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
- name: Create or update specific LoadBalancingSettings
  azure_rm_frontdoorloadbalancingsetting:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myLoadBalancingSetting
- name: Delete LoadBalancingSettings
  azure_rm_frontdoorloadbalancingsetting:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myLoadBalancingSetting
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties of the load balancing settings
  returned: always
  type: dict
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
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
    from azure.mgmt.frontdoor import FrontdoorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLoadBalancingSettings(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            front_door_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='load_balancing_settings_name',
                required=true
            ),
            id=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.front_door_name = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLoadBalancingSettings, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(FrontdoorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

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
           self.results["id"] = response["id"]
           self.results["properties"] = response["properties"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.load_balancing_settings.create_or_update(resource_group_name=self.resource_group,
                                                                                 front_door_name=self.front_door_name,
                                                                                 load_balancing_settings_name=self.name,
                                                                                 load_balancing_settings_parameters=self.loadBalancingSettingsParameters)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LoadBalancingSetting instance.')
            self.fail('Error creating the LoadBalancingSetting instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the LoadBalancingSetting instance {0}'.format(self.))
        try:
            response = self.mgmt_client.load_balancing_settings.delete(resource_group_name=self.resource_group,
                                                                       front_door_name=self.front_door_name,
                                                                       load_balancing_settings_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the LoadBalancingSetting instance.')
            self.fail('Error deleting the LoadBalancingSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the LoadBalancingSetting instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.load_balancing_settings.get(resource_group_name=self.resource_group,
                                                                    front_door_name=self.front_door_name,
                                                                    load_balancing_settings_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLoadBalancingSettings()


if __name__ == '__main__':
    main()
