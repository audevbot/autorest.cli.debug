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
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  sample_size:
    description:
      - The number of samples to consider for load balancing decisions
    type: number
  successful_samples_required:
    description:
      - The number of samples within the sample period that must succeed
    type: number
  additional_latency_milliseconds:
    description:
      - >-
        The additional latency in milliseconds for probes to fall into the
        lowest latency bucket
    type: number
  resource_state:
    description:
      - Resource status.
    type: str
  type:
    description:
      - Resource type.
    type: str
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
    load_balancing_settings_parameters:
      name: loadBalancingSettings1
      properties:
        sampleSize: '4'
        successfulSamplesRequired: '2'
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
  contains:
    sample_size:
      description:
        - The number of samples to consider for load balancing decisions
      returned: always
      type: number
      sample: null
    successful_samples_required:
      description:
        - The number of samples within the sample period that must succeed
      returned: always
      type: number
      sample: null
    additional_latency_milliseconds:
      description:
        - >-
          The additional latency in milliseconds for probes to fall into the
          lowest latency bucket
      returned: always
      type: number
      sample: null
    resource_state:
      description:
        - Resource status.
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
    - Resource type.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLoadBalancingSettings(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            front_door_name=dict(
                type='str',
                updatable=False,
                disposition='frontDoorName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='loadBalancingSettingsName',
                required=true
            ),
            id=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            sample_size=dict(
                type='number',
                disposition='/properties/sampleSize'
            ),
            successful_samples_required=dict(
                type='number',
                disposition='/properties/successfulSamplesRequired'
            ),
            additional_latency_milliseconds=dict(
                type='number',
                disposition='/properties/additionalLatencyMilliseconds'
            ),
            resource_state=dict(
                type='str',
                disposition='/properties/resourceState',
                choices=['Creating',
                         'Enabling',
                         'Enabled',
                         'Disabling',
                         'Disabled',
                         'Deleting']
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

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors' +
                    '/{{ front_door_name }}' +
                    '/loadBalancingSettings' +
                    '/{{ load_balancing_setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.front_door_name)
        self.url = self.url.replace('{{ load_balancing_setting_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("LoadBalancingSetting instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('LoadBalancingSetting instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the LoadBalancingSetting instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('LoadBalancingSetting instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('LoadBalancingSetting instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["properties"] = response["properties"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the LoadBalancingSetting instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the LoadBalancingSetting instance.')
            self.fail('Error creating the LoadBalancingSetting instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the LoadBalancingSetting instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the LoadBalancingSetting instance.')
            self.fail('Error deleting the LoadBalancingSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the LoadBalancingSetting instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("LoadBalancingSetting instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the LoadBalancingSetting instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMLoadBalancingSettings()


if __name__ == '__main__':
    main()
