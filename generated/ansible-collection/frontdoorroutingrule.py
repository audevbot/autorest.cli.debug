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
module: frontdoorroutingrule
version_added: '2.9'
short_description: Manage Azure RoutingRule instance.
description:
  - 'Create, update and delete instance of Azure RoutingRule.'
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
  frontend_endpoints:
    description:
      - Frontend endpoints associated with this rule
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
  accepted_protocols:
    description:
      - Protocol schemes to match for this rule
    type: list
  patterns_to_match:
    description:
      - The route patterns of the rule.
    type: list
  enabled_state:
    description:
      - >-
        Whether to enable use of this rule. Permitted values are 'Enabled' or
        'Disabled'
  route_configuration:
    description:
      - A reference to the routing configuration.
  resource_state:
    description:
      - Resource status.
  type:
    description:
      - Resource type.
  state:
    description:
      - Assert the state of the RoutingRule.
      - >-
        Use C(present) to create or update an RoutingRule and C(absent) to
        delete it.
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
- name: Create or update specific Forwarding Routing Rule
  azure.rm.frontdoorroutingrule:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myRoutingRule
    routing_rule_parameters:
      name: routingRule1
      properties:
        frontendEndpoints:
          - id: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Network/frontDoors/{{
              front_door_name }}/frontendEndpoints/{{ frontend_endpoint_name }}
          - id: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Network/frontDoors/{{
              front_door_name }}/frontendEndpoints/{{ frontend_endpoint_name }}
        acceptedProtocols:
          - Http
        patternsToMatch:
          - /*
        routeConfiguration:
          '@odata.type': '#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration'
          backendPool:
            id: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Network/frontDoors/{{
              front_door_name }}/backendPools/{{ backend_pool_name }}
        enabledState: Enabled
- name: Create or update specific Redirect Routing Rule
  azure.rm.frontdoorroutingrule:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myRoutingRule
    routing_rule_parameters:
      name: redirectRoutingRule1
      properties:
        frontendEndpoints:
          - id: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Network/frontDoors/{{
              front_door_name }}/frontendEndpoints/{{ frontend_endpoint_name }}
          - id: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Network/frontDoors/{{
              front_door_name }}/frontendEndpoints/{{ frontend_endpoint_name }}
        acceptedProtocols:
          - Https
        patternsToMatch:
          - /*
        routeConfiguration:
          '@odata.type': '#Microsoft.Azure.FrontDoor.Models.FrontdoorRedirectConfiguration'
          redirectType: Moved
          redirectProtocol: HttpsOnly
          customHost: www.bing.com
          customPath: /api
          customFragment: fragment
          customQueryString: a=b
        enabledState: Enabled
- name: Delete Routing Rule
  azure.rm.frontdoorroutingrule:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myRoutingRule
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
    - Properties of the Front Door Routing Rule
  returned: always
  type: dict
  sample: null
  contains:
    frontend_endpoints:
      description:
        - Frontend endpoints associated with this rule
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    accepted_protocols:
      description:
        - Protocol schemes to match for this rule
      returned: always
      type: str
      sample: null
    patterns_to_match:
      description:
        - The route patterns of the rule.
      returned: always
      type: str
      sample: null
    enabled_state:
      description:
        - >-
          Whether to enable use of this rule. Permitted values are 'Enabled' or
          'Disabled'
      returned: always
      type: str
      sample: null
    route_configuration:
      description:
        - A reference to the routing configuration.
      returned: always
      type: dict
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
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRoutingRules(AzureRMModuleBaseExt):
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
                disposition='routingRuleName',
                required=true
            ),
            id=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            frontend_endpoints=dict(
                type='list',
                disposition='/properties/frontendEndpoints',
                options=dict(
                    id=dict(
                        type='str'
                    )
                )
            ),
            accepted_protocols=dict(
                type='list',
                disposition='/properties/acceptedProtocols',
                choices=['Http',
                         'Https']
            ),
            patterns_to_match=dict(
                type='list',
                disposition='/properties/patternsToMatch'
            ),
            enabled_state=dict(
                type='str',
                disposition='/properties/enabledState',
                choices=['Enabled',
                         'Disabled']
            ),
            route_configuration=dict(
                type='dict',
                disposition='/properties/routeConfiguration'
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

        super(AzureRMRoutingRules, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/routingRules' +
                    '/{{ routing_rule_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.front_door_name)
        self.url = self.url.replace('{{ routing_rule_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("RoutingRule instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('RoutingRule instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the RoutingRule instance')

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
            self.log('RoutingRule instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('RoutingRule instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["properties"] = response["properties"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the RoutingRule instance {0}'.format(self.))

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
            self.log('Error attempting to create the RoutingRule instance.')
            self.fail('Error creating the RoutingRule instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the RoutingRule instance {0}'.format(self.))
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
            self.log('Error attempting to delete the RoutingRule instance.')
            self.fail('Error deleting the RoutingRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the RoutingRule instance {0} is present'.format(self.))
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
            # self.log("RoutingRule instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the RoutingRule instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMRoutingRules()


if __name__ == '__main__':
    main()
