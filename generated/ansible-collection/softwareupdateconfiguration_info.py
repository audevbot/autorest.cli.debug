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
module: softwareupdateconfiguration_info
version_added: '2.9'
short_description: Get SoftwareUpdateConfiguration info.
description:
  - Get info of SoftwareUpdateConfiguration.
options:
  resource_group:
    description:
      - Name of an Azure Resource group.
    required: true
    type: str
  automation_account_name:
    description:
      - The name of the automation account.
    required: true
    type: str
  client_request_id:
    description:
      - Identifies this specific client request.
    required: true
    type: str
  name:
    description:
      - The name of the software update configuration to be created.
    type: str
  value:
    description:
      - outer object returned when listing all software update configurations
    type: list
    suboptions:
      name:
        description:
          - Name of the software update configuration.
        type: str
      id:
        description:
          - Resource Id of the software update configuration
        type: str
      update_configuration:
        description:
          - Update specific properties of the software update configuration.
        type: dict
        suboptions:
          azure_virtual_machines:
            description:
              - >-
                List of azure resource Ids for azure virtual machines targeted
                by the software update configuration.
            type: list
          duration:
            description:
              - >-
                Maximum time allowed for the software update configuration run.
                Duration needs to be specified using the format PT[n]H[n]M[n]S
                as per ISO8601
            type: 'unknown-primary[timeSpan]'
      frequency:
        description:
          - >-
            execution frequency of the schedule associated with the software
            update configuration
        type: str
      start_time:
        description:
          - the start time of the update.
        type: datetime
      creation_time:
        description:
          - >-
            Creation time of the software update configuration, which only
            appears in the response.
        type: datetime
      last_modified_time:
        description:
          - >-
            Last time software update configuration was modified, which only
            appears in the response.
        type: datetime
      provisioning_state:
        description:
          - >-
            Provisioning state for the software update configuration, which only
            appears in the response.
        type: str
      next_run:
        description:
          - ext run time of the update.
        type: datetime
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List software update configurations
  azure.rm.softwareupdateconfiguration.info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
- name: >-
    List software update configurations Targeting a specific azure virtual
    machine
  azure.rm.softwareupdateconfiguration.info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
- name: Get software update configuration by name
  azure.rm.softwareupdateconfiguration.info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: mySoftwareUpdateConfiguration

'''

RETURN = '''
software_update_configurations:
  description: >-
    A list of dict results where the key is the name of the
    SoftwareUpdateConfiguration and the values are the facts for that
    SoftwareUpdateConfiguration.
  returned: always
  type: complex
  contains:
    softwareupdateconfiguration_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - >-
              outer object returned when listing all software update
              configurations
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the software update configuration.
              returned: always
              type: str
              sample: null
            id:
              description:
                - Resource Id of the software update configuration
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Software update configuration properties.
              returned: always
              type: dict
              sample: null
            update_configuration:
              description:
                - >-
                  Update specific properties of the software update
                  configuration.
              returned: always
              type: dict
              sample: null
              contains:
                azure_virtual_machines:
                  description:
                    - >-
                      List of azure resource Ids for azure virtual machines
                      targeted by the software update configuration.
                  returned: always
                  type: str
                  sample: null
                duration:
                  description:
                    - >-
                      Maximum time allowed for the software update configuration
                      run. Duration needs to be specified using the format
                      PT[n]H[n]M[n]S as per ISO8601
                  returned: always
                  type: 'unknown-primary[timeSpan]'
                  sample: null
            frequency:
              description:
                - >-
                  execution frequency of the schedule associated with the
                  software update configuration
              returned: always
              type: str
              sample: null
            start_time:
              description:
                - the start time of the update.
              returned: always
              type: datetime
              sample: null
            creation_time:
              description:
                - >-
                  Creation time of the software update configuration, which only
                  appears in the response.
              returned: always
              type: datetime
              sample: null
            last_modified_time:
              description:
                - >-
                  Last time software update configuration was modified, which
                  only appears in the response.
              returned: always
              type: datetime
              sample: null
            provisioning_state:
              description:
                - >-
                  Provisioning state for the software update configuration,
                  which only appears in the response.
              returned: always
              type: str
              sample: null
            next_run:
              description:
                - ext run time of the update.
              returned: always
              type: datetime
              sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMSoftwareUpdateConfigurationsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            automation_account_name=dict(
                type='str',
                required=true
            ),
            client_request_id=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.automation_account_name = None
        self.client_request_id = None
        self.name = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-05-15-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSoftwareUpdateConfigurationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.automation_account_name is not None and
            self.name is not None):
            self.results['software_update_configurations'] = self.format_item(self.getbyname())
        elif (self.resource_group is not None and
              self.automation_account_name is not None):
            self.results['software_update_configurations'] = self.format_item(self.list())
        return self.results

    def getbyname(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Automation' +
                    '/automationAccounts' +
                    '/{{ automation_account_name }}' +
                    '/softwareUpdateConfigurations' +
                    '/{{ software_update_configuration_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ automation_account_name }}', self.automation_account_name)
        self.url = self.url.replace('{{ software_update_configuration_name }}', self.name)

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

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Automation' +
                    '/automationAccounts' +
                    '/{{ automation_account_name }}' +
                    '/softwareUpdateConfigurations')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ automation_account_name }}', self.automation_account_name)
        self.url = self.url.replace('{{ software_update_configuration_name }}', self.name)

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
    AzureRMSoftwareUpdateConfigurationsInfo()


if __name__ == '__main__':
    main()
