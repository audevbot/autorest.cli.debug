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
module: azure_rm_alertsmanagementsmartdetectoralertrule_info
version_added: '2.9'
short_description: Get SmartDetectorAlertRule info.
description:
  - Get info of SmartDetectorAlertRule.
options:
  expand_detector:
    description:
      - Indicates if Smart Detector should be expanded.
    required: true
    type: boolean
  resource_group:
    description:
      - The name of the resource group.
    type: str
  name:
    description:
      - The resource name.
    type: str
  id:
    description:
      - The resource ID.
    type: str
  type:
    description:
      - The resource type.
    type: str
  location:
    description:
      - The resource location.
    type: str
  description:
    description:
      - The alert rule description.
    type: str
  state:
    description:
      - The alert rule state.
    required: true
    type: str
  severity:
    description:
      - The alert rule severity.
    required: true
    type: str
  frequency:
    description:
      - >-
        The alert rule frequency in ISO8601 format. The time granularity must be
        in minutes and minimum value is 5 minutes.
    required: true
    type: 'unknown-primary[timeSpan]'
  detector:
    description:
      - The alert rule's detector.
    required: true
    type: dict
    suboptions:
      id:
        description:
          - The detector id.
        required: true
        type: str
      parameters:
        description:
          - The detector's parameters.'
        type: >-
          unknown[DictionaryType
          {"$id":"973","$type":"DictionaryType","valueType":{"$id":"974","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"975","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"976","fixed":false},"deprecated":false}]
      name:
        description:
          - >-
            The Smart Detector name. By default this is not populated, unless
            it's specified in expandDetector
        type: str
      description:
        description:
          - >-
            The Smart Detector description. By default this is not populated,
            unless it's specified in expandDetector
        type: str
      supported_resource_types:
        description:
          - >-
            The Smart Detector supported resource types. By default this is not
            populated, unless it's specified in expandDetector
        type: list
      image_paths:
        description:
          - >-
            The Smart Detector image path. By default this is not populated,
            unless it's specified in expandDetector
        type: list
  scope:
    description:
      - The alert rule resources scope.
    required: true
    type: list
  action_groups:
    description:
      - The alert rule actions.
    required: true
    type: dict
    suboptions:
      custom_email_subject:
        description:
          - An optional custom email subject to use in email notifications.
        type: str
      custom_webhook_payload:
        description:
          - >-
            An optional custom web-hook payload to use in web-hook
            notifications.
        type: str
      group_ids:
        description:
          - The Action Group resource IDs.
        required: true
        type: list
  throttling:
    description:
      - The alert rule throttling information.
    type: dict
    suboptions:
      duration:
        description:
          - >-
            The required duration (in ISO8601 format) to wait before notifying
            on the alert rule again. The time granularity must be in minutes and
            minimum value is 0 minutes
        type: 'unknown-primary[timeSpan]'
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List Smart Detector alert rules
  azure_rm_alertsmanagementsmartdetectoralertrule_info:
    resource_group: MyAlertRules
- name: List alert rules
  azure_rm_alertsmanagementsmartdetectoralertrule_info:
    resource_group: myResourceGroup
- name: Get a Smart Detector alert rule
  azure_rm_alertsmanagementsmartdetectoralertrule_info:
    resource_group: myResourceGroup
    name: mySmartDetectorAlertRule

'''

RETURN = '''
smart_detector_alert_rules:
  description: >-
    A list of dict results where the key is the name of the
    SmartDetectorAlertRule and the values are the facts for that
    SmartDetectorAlertRule.
  returned: always
  type: complex
  contains:
    smartdetectoralertrule_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - The resource ID.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The resource type.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The resource name.
          returned: always
          type: str
          sample: null
        location:
          description:
            - The resource location.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - The resource tags.
          returned: always
          type: 'unknown-primary[object]'
          sample: null
        properties:
          description:
            - The properties of the alert rule.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMSmartDetectorAlertRulesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            expand_detector=dict(
                type='boolean',
                required=true
            ),
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.expand_detector = None
        self.resource_group = None
        self.name = None
        self.id = None
        self.type = None
        self.name = None
        self.location = None
        self.tags = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = 'undefined'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSmartDetectorAlertRulesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['smart_detector_alert_rules'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['smart_detector_alert_rules'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['smart_detector_alert_rules'] = [self.format_item(self.list())]
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
                    '/microsoft.alertsManagement' +
                    '/smartDetectorAlertRules' +
                    '/{{ smart_detector_alert_rule_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ smart_detector_alert_rule_name }}', self.name)

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

    def listbyresourcegroup(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/microsoft.alertsManagement' +
                    '/smartDetectorAlertRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ smart_detector_alert_rule_name }}', self.name)

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
                    '/providers' +
                    '/microsoft.alertsManagement' +
                    '/smartDetectorAlertRules')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ smart_detector_alert_rule_name }}', self.name)

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
    AzureRMSmartDetectorAlertRulesInfo()


if __name__ == '__main__':
    main()
