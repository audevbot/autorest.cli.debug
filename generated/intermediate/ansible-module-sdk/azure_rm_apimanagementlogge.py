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
module: azure_rm_apimanagementlogge
version_added: '2.9'
short_description: Manage Azure Logger instance.
description:
  - 'Create, update and delete instance of Azure Logger.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  logger_id:
    description:
      - >-
        Logger identifier. Must be unique in the API Management service
        instance.
    required: true
    type: str
  logger_type:
    description:
      - Logger type.
    required: true
    type: str
  description:
    description:
      - Logger description.
    type: str
  credentials:
    description:
      - >-
        The name and SendRule connection string of the event hub for
        azureEventHub logger.<br>Instrumentation key for applicationInsights
        logger.
    required: true
    type: >-
      unknown[DictionaryType
      {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]
  is_buffered:
    description:
      - >-
        Whether records are buffered in the logger before publishing. Default is
        assumed to be true.
    type: boolean
  resource_id:
    description:
      - >-
        Azure Resource Id of a log target (either Azure Event Hub resource or
        Azure Application Insights resource).
    type: str
  id:
    description:
      - Resource ID.
    type: str
  name:
    description:
      - Resource name.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the Logger.
      - Use C(present) to create or update an Logger and C(absent) to delete it.
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
- name: ApiManagementCreateEHLogger
  azure_rm_apimanagementlogge:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    logger_type: azureEventHub
    description: adding a new logger
    credentials:
      name: hydraeventhub
      connectionString: >-
        Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********=
- name: ApiManagementCreateAILogger
  azure_rm_apimanagementlogge:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    logger_type: applicationInsights
    description: adding a new logger
    credentials:
      instrumentationKey: 11................a1
- name: ApiManagementUpdateLogger
  azure_rm_apimanagementlogge:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    credentials:
      name: hydraeventhub
      connectionString: >-
        Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********=
- name: ApiManagementDeleteLogger
  azure_rm_apimanagementlogge:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
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
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Logger entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    logger_type:
      description:
        - Logger type.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Logger description.
      returned: always
      type: str
      sample: null
    credentials:
      description:
        - >-
          The name and SendRule connection string of the event hub for
          azureEventHub logger.<br>Instrumentation key for applicationInsights
          logger.
      returned: always
      type: >-
        unknown[DictionaryType
        {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]
      sample: null
    is_buffered:
      description:
        - >-
          Whether records are buffered in the logger before publishing. Default
          is assumed to be true.
      returned: always
      type: boolean
      sample: null
    resource_id:
      description:
        - >-
          Azure Resource Id of a log target (either Azure Event Hub resource or
          Azure Application Insights resource).
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLogger(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            logger_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            logger_type=dict(
                type='str',
                disposition='/',
                choices=['azureEventHub',
                         'applicationInsights'],
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            credentials=dict(
                type='unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]',
                disposition='/',
                required=true
            ),
            is_buffered=dict(
                type='boolean',
                disposition='/'
            ),
            resource_id=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.logger_id = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLogger, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClient,
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
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.logger.create_or_update(resource_group_name=self.resource_group,
                                                                service_name=self.service_name,
                                                                logger_id=self.logger_id,
                                                                parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Logger instance.')
            self.fail('Error creating the Logger instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Logger instance {0}'.format(self.))
        try:
            response = self.mgmt_client.logger.delete(resource_group_name=self.resource_group,
                                                      service_name=self.service_name,
                                                      logger_id=self.logger_id)
        except CloudError as e:
            self.log('Error attempting to delete the Logger instance.')
            self.fail('Error deleting the Logger instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Logger instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.logger.get(resource_group_name=self.resource_group,
                                                   service_name=self.service_name,
                                                   logger_id=self.logger_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLogger()


if __name__ == '__main__':
    main()
