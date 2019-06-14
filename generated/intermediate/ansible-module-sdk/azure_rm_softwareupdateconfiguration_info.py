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
module: azure_rm_softwareupdateconfiguration_info
version_added: '2.9'
short_description: Get SoftwareUpdateConfiguration info.
description:
  - Get info of SoftwareUpdateConfiguration.
options:
  resource_group:
    description:
      - Name of an Azure Resource group.
    required: true
  automation_account_name:
    description:
      - The name of the automation account.
    required: true
  client_request_id:
    description:
      - Identifies this specific client request.
    required: true
  name:
    description:
      - The name of the software update configuration to be created.
  value:
    description:
      - outer object returned when listing all software update configurations
    type: list
    suboptions:
      name:
        description:
          - Name of the software update configuration.
      id:
        description:
          - Resource Id of the software update configuration
      update_configuration:
        description:
          - Update specific properties of the software update configuration.
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
      frequency:
        description:
          - >-
            execution frequency of the schedule associated with the software
            update configuration
      start_time:
        description:
          - the start time of the update.
      creation_time:
        description:
          - >-
            Creation time of the software update configuration, which only
            appears in the response.
      last_modified_time:
        description:
          - >-
            Last time software update configuration was modified, which only
            appears in the response.
      provisioning_state:
        description:
          - >-
            Provisioning state for the software update configuration, which only
            appears in the response.
      next_run:
        description:
          - ext run time of the update.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List software update configurations
  azure_rm_softwareupdateconfiguration_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
- name: >-
    List software update configurations Targeting a specific azure virtual
    machine
  azure_rm_softwareupdateconfiguration_info:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
- name: Get software update configuration by name
  azure_rm_softwareupdateconfiguration_info:
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
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.automation import UpdateManagementAPIClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


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

        self.mgmt_client = self.get_mgmt_svc_client(UpdateManagementAPIClient,
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

        try:
            response = self.mgmt_client.software_update_configurations.get_by_name(resource_group_name=self.resource_group,
                                                                                   automation_account_name=self.automation_account_name,
                                                                                   software_update_configuration_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.software_update_configurations.list(resource_group_name=self.resource_group,
                                                                            automation_account_name=self.automation_account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMSoftwareUpdateConfigurationsInfo()


if __name__ == '__main__':
    main()
