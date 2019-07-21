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
module: azure_rm_frontdoorroutingrule_info
version_added: '2.9'
short_description: Get RoutingRule info.
description:
  - Get info of RoutingRule.
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
  frontend_endpoints:
    description:
      - Frontend endpoints associated with this rule
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
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
    type: str
  route_configuration:
    description:
      - A reference to the routing configuration.
    type: dict
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
- name: List Routing Rules in a Front Door
  azure_rm_frontdoorroutingrule_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
- name: Get Forwarding Routing Rule
  azure_rm_frontdoorroutingrule_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myRoutingRule
- name: Get Redirect Routing Rule
  azure_rm_frontdoorroutingrule_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myRoutingRule

'''

RETURN = '''
routing_rules:
  description: >-
    A list of dict results where the key is the name of the RoutingRule and the
    values are the facts for that RoutingRule.
  returned: always
  type: complex
  contains:
    routingrule_name:
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
            - Properties of the Front Door Routing Rule
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
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.frontdoor import FrontdoorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRoutingRulesInfo(AzureRMModuleBase):
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
        super(AzureRMRoutingRulesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontdoorClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.front_door_name is not None and
            self.name is not None):
            self.results['routing_rules'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.front_door_name is not None):
            self.results['routing_rules'] = self.format_item(self.listbyfrontdoor())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.routing_rules.get(resource_group_name=self.resource_group,
                                                          front_door_name=self.front_door_name,
                                                          routing_rule_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyfrontdoor(self):
        response = None

        try:
            response = self.mgmt_client.routing_rules.list_by_front_door(resource_group_name=self.resource_group,
                                                                         front_door_name=self.front_door_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMRoutingRulesInfo()


if __name__ == '__main__':
    main()
