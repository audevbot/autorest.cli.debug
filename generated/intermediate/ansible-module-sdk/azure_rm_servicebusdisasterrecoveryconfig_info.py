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
module: azure_rm_servicebusdisasterrecoveryconfig_info
version_added: '2.9'
short_description: Get DisasterRecoveryConfig info.
description:
  - Get info of DisasterRecoveryConfig.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
  namespace_name:
    description:
      - The namespace name
    required: true
  alias:
    description:
      - The Disaster Recovery configuration name
  name:
    description:
      - Resource name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  provisioning_state:
    description:
      - >-
        Provisioning state of the Alias(Disaster Recovery configuration) -
        possible values 'Accepted' or 'Succeeded' or 'Failed'
  pending_replication_operations_count:
    description:
      - Number of entities pending to be replicated.
  partner_namespace:
    description:
      - >-
        ARM Id of the Primary/Secondary eventhub namespace name, which is part
        of GEO DR pairing
  alternate_name:
    description:
      - >-
        Primary/Secondary eventhub namespace name, which is part of GEO DR
        pairing
  role:
    description:
      - >-
        role of namespace in GEO DR - possible values 'Primary' or
        'PrimaryNotReplicating' or 'Secondary'
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: SBAliasList
  azure_rm_servicebusdisasterrecoveryconfig_info:
    resource_group: myResourceGroup
    namespace_name: my
    alias: sdk-DisasterRecovery-3814
- name: SBAliasGet
  azure_rm_servicebusdisasterrecoveryconfig_info:
    resource_group: myResourceGroup
    namespace_name: my
    alias: myDisasterRecoveryConfig
- name: NameSpaceAuthorizationRuleListAll
  azure_rm_servicebusdisasterrecoveryconfig_info:
    resource_group: myResourceGroup
    namespace_name: my
    alias: myDisasterRecoveryConfig
- name: DisasterRecoveryConfigsAuthorizationRuleGet
  azure_rm_servicebusdisasterrecoveryconfig_info:
    resource_group: myResourceGroup
    namespace_name: my
    alias: myDisasterRecoveryConfig
    name: myAuthorizationRule

'''

RETURN = '''
disaster_recovery_configs:
  description: >-
    A list of dict results where the key is the name of the
    DisasterRecoveryConfig and the values are the facts for that
    DisasterRecoveryConfig.
  returned: always
  type: complex
  contains:
    disasterrecoveryconfig_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
        properties:
          description:
            - >-
              Properties required to the Create Or Update Alias(Disaster
              Recovery configurations)
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDisasterRecoveryConfigsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            namespace_name=dict(
                type='str',
                required=true
            ),
            alias=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.alias = None
        self.name = None
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
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDisasterRecoveryConfigsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.namespace_name is not None and
            self.alias is not None and
            self.name is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.getauthorizationrule())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.alias is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.listauthorizationrules())
        elif (self.resource_group is not None and
              self.namespace_name is not None and
              self.alias is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.namespace_name is not None):
            self.results['disaster_recovery_configs'] = self.format_item(self.list())
        return self.results

    def getauthorizationrule(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.get_authorization_rule(resource_group_name=self.resource_group,
                                                                                         namespace_name=self.namespace_name,
                                                                                         alias=self.alias,
                                                                                         authorization_rule_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listauthorizationrules(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.list_authorization_rules(resource_group_name=self.resource_group,
                                                                                           namespace_name=self.namespace_name,
                                                                                           alias=self.alias)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.get(resource_group_name=self.resource_group,
                                                                      namespace_name=self.namespace_name,
                                                                      alias=self.alias)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.disaster_recovery_configs.list(resource_group_name=self.resource_group,
                                                                       namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMDisasterRecoveryConfigsInfo()


if __name__ == '__main__':
    main()
