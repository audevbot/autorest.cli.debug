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
module: frontdoorhealthprobesetting_info
version_added: '2.9'
short_description: Get HealthProbeSetting info.
description:
  - Get info of HealthProbeSetting.
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
  path:
    description:
      - The path to use for the health probe. Default is /
    type: str
  protocol:
    description:
      - Protocol scheme to use for this probe
    type: str
  interval_in_seconds:
    description:
      - The number of seconds between health probes.
    type: number
  resource_state:
    description:
      - Resource status.
    type: str
  type:
    description:
      - Resource type.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List HealthProbeSettings in a Front Door
  azure.rm.frontdoorhealthprobesetting.info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
- name: Get HealthProbeSettings
  azure.rm.frontdoorhealthprobesetting.info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myHealthProbeSetting

'''

RETURN = '''
health_probe_settings:
  description: >-
    A list of dict results where the key is the name of the HealthProbeSetting
    and the values are the facts for that HealthProbeSetting.
  returned: always
  type: complex
  contains:
    healthprobesetting_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the health probe settings
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMHealthProbeSettingsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            front_door_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.front_door_name = None
        self.name = None
        self.id = None
        self.properties = None
        self.name = None
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
        super(AzureRMHealthProbeSettingsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.front_door_name is not None and
            self.name is not None):
            self.results['health_probe_settings'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.front_door_name is not None):
            self.results['health_probe_settings'] = self.format_item(self.listbyfrontdoor())
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
                    '/Microsoft.Network' +
                    '/frontDoors' +
                    '/{{ front_door_name }}' +
                    '/healthProbeSettings' +
                    '/{{ health_probe_setting_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.front_door_name)
        self.url = self.url.replace('{{ health_probe_setting_name }}', self.name)

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

    def listbyfrontdoor(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors' +
                    '/{{ front_door_name }}' +
                    '/healthProbeSettings')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.front_door_name)
        self.url = self.url.replace('{{ health_probe_setting_name }}', self.name)

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
    AzureRMHealthProbeSettingsInfo()


if __name__ == '__main__':
    main()
