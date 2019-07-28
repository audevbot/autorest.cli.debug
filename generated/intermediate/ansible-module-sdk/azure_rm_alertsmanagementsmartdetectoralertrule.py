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
module: azure_rm_alertsmanagementsmartdetectoralertrule
version_added: '2.9'
short_description: Manage Azure SmartDetectorAlertRule instance.
description:
  - 'Create, update and delete instance of Azure SmartDetectorAlertRule.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The resource name.
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
      - Assert the state of the SmartDetectorAlertRule.
      - >-
        Use C(present) to create or update an SmartDetectorAlertRule and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
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
  id:
    description:
      - The resource ID.
    type: str
  type:
    description:
      - The resource type.
    type: str
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Create or update a Smart Detector alert rule
  azure_rm_alertsmanagementsmartdetectoralertrule:
    resource_group: myResourceGroup
    name: mySmartDetectorAlertRule
    description: Sample smart detector alert rule description
    state: Enabled
    severity: Sev3
    frequency: PT5M
    detector:
      id: VMMemoryLeak
    scope:
      - >-
        /subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1
    action_groups:
      custom_email_subject: My custom email subject
      custom_webhook_payload: '{"AlertRuleName":"#alertrulename"}'
      group_ids:
        - >-
          /subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourcegroups/actionGroups/providers/microsoft.insights/actiongroups/MyActionGroup
    throttling:
      duration: PT20M
- name: Delete a Smart Detector alert rule
  azure_rm_alertsmanagementsmartdetectoralertrule:
    resource_group: myResourceGroup
    name: mySmartDetectorAlertRule
    state: absent

'''

RETURN = '''
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
  contains:
    description:
      description:
        - The alert rule description.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The alert rule state.
      returned: always
      type: str
      sample: null
    severity:
      description:
        - The alert rule severity.
      returned: always
      type: str
      sample: null
    frequency:
      description:
        - >-
          The alert rule frequency in ISO8601 format. The time granularity must
          be in minutes and minimum value is 5 minutes.
      returned: always
      type: 'unknown-primary[timeSpan]'
      sample: null
    detector:
      description:
        - The alert rule's detector.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The detector id.
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - The detector's parameters.'
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"973","$type":"DictionaryType","valueType":{"$id":"974","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"975","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"976","fixed":false},"deprecated":false}]
          sample: null
        name:
          description:
            - >-
              The Smart Detector name. By default this is not populated, unless
              it's specified in expandDetector
          returned: always
          type: str
          sample: null
        description:
          description:
            - >-
              The Smart Detector description. By default this is not populated,
              unless it's specified in expandDetector
          returned: always
          type: str
          sample: null
        supported_resource_types:
          description:
            - >-
              The Smart Detector supported resource types. By default this is
              not populated, unless it's specified in expandDetector
          returned: always
          type: str
          sample: null
        image_paths:
          description:
            - >-
              The Smart Detector image path. By default this is not populated,
              unless it's specified in expandDetector
          returned: always
          type: str
          sample: null
    scope:
      description:
        - The alert rule resources scope.
      returned: always
      type: str
      sample: null
    action_groups:
      description:
        - The alert rule actions.
      returned: always
      type: dict
      sample: null
      contains:
        custom_email_subject:
          description:
            - An optional custom email subject to use in email notifications.
          returned: always
          type: str
          sample: null
        custom_webhook_payload:
          description:
            - >-
              An optional custom web-hook payload to use in web-hook
              notifications.
          returned: always
          type: str
          sample: null
        group_ids:
          description:
            - The Action Group resource IDs.
          returned: always
          type: str
          sample: null
    throttling:
      description:
        - The alert rule throttling information.
      returned: always
      type: dict
      sample: null
      contains:
        duration:
          description:
            - >-
              The required duration (in ISO8601 format) to wait before notifying
              on the alert rule again. The time granularity must be in minutes
              and minimum value is 0 minutes
          returned: always
          type: 'unknown-primary[timeSpan]'
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.alertsmanagement import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSmartDetectorAlertRules(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='alert_rule_name',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                disposition='/',
                choices=['Enabled',
                         'Disabled'],
                required=true
            ),
            severity=dict(
                type='str',
                disposition='/',
                choices=['Sev0',
                         'Sev1',
                         'Sev2',
                         'Sev3',
                         'Sev4'],
                required=true
            ),
            frequency=dict(
                type='unknown-primary[timeSpan]',
                disposition='/',
                required=true
            ),
            detector=dict(
                type='dict',
                disposition='/',
                required=true,
                options=dict(
                    id=dict(
                        type='str',
                        required=true
                    ),
                    parameters=dict(
                        type='unknown[DictionaryType {"$id":"973","$type":"DictionaryType","valueType":{"$id":"974","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"975","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"976","fixed":false},"deprecated":false}]'
                    ),
                    name=dict(
                        type='str'
                    ),
                    description=dict(
                        type='str'
                    ),
                    supported_resource_types=dict(
                        type='list'
                    ),
                    image_paths=dict(
                        type='list'
                    )
                )
            ),
            scope=dict(
                type='raw',
                disposition='/',
                required=true,
                pattern=('//subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups'
                         '/MyVms/providers/Microsoft.Compute/virtualMachines/vm1')
            ),
            action_groups=dict(
                type='dict',
                disposition='/',
                required=true,
                options=dict(
                    custom_email_subject=dict(
                        type='str'
                    ),
                    custom_webhook_payload=dict(
                        type='str'
                    ),
                    group_ids=dict(
                        type='raw',
                        required=true,
                        pattern=('//subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa'
                                 '/resourcegroups/actionGroups/providers/microsoft.insights'
                                 '/actiongroups/MyActionGroup')
                    )
                )
            ),
            throttling=dict(
                type='dict',
                disposition='/',
                options=dict(
                    duration=dict(
                        type='unknown-primary[timeSpan]'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.type = None
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSmartDetectorAlertRules, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServices,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

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
           self.results["type"] = response["type"]
           self.results["name"] = response["name"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.smart_detector_alert_rules.create_or_update(resource_group_name=self.resource_group,
                                                                                    alert_rule_name=self.name,
                                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SmartDetectorAlertRule instance.')
            self.fail('Error creating the SmartDetectorAlertRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the SmartDetectorAlertRule instance {0}'.format(self.))
        try:
            response = self.mgmt_client.smart_detector_alert_rules.delete(resource_group_name=self.resource_group,
                                                                          alert_rule_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the SmartDetectorAlertRule instance.')
            self.fail('Error deleting the SmartDetectorAlertRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the SmartDetectorAlertRule instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.smart_detector_alert_rules.get(resource_group_name=self.resource_group,
                                                                       alert_rule_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSmartDetectorAlertRules()


if __name__ == '__main__':
    main()
