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
module: azure_rm_apimanagementdelegationsetting
version_added: '2.9'
short_description: Manage Azure DelegationSetting instance.
description:
  - 'Create, update and delete instance of Azure DelegationSetting.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  url:
    description:
      - A delegation Url.
    type: str
  validation_key:
    description:
      - >-
        A base64-encoded validation key to validate, that a request is coming
        from Azure API Management.
    type: str
  subscriptions:
    description:
      - Subscriptions delegation settings.
    type: dict
    suboptions:
      enabled:
        description:
          - Enable or disable delegation for subscriptions.
        type: boolean
  user_registration:
    description:
      - User registration delegation settings.
    type: dict
    suboptions:
      enabled:
        description:
          - Enable or disable delegation for user registration.
        type: boolean
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  state:
    description:
      - Assert the state of the DelegationSetting.
      - >-
        Use C(present) to create or update an DelegationSetting and C(absent) to
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
- name: ApiManagementPortalSettingsUpdateDelegation
  azure_rm_apimanagementdelegationsetting:
    resource_group: myResourceGroup
    name: myService
    url: 'http://contoso.com/delegation'
    validation_key: >-
      nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
    subscriptions:
      enabled: true
    user_registration:
      enabled: true
- name: ApiManagementPortalSettingsUpdateDelegation
  azure_rm_apimanagementdelegationsetting:
    resource_group: myResourceGroup
    name: myService
    url: 'http://contoso.com/delegation'
    validation_key: >-
      nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
    subscriptions:
      enabled: true
    user_registration:
      enabled: true

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
    - Delegation settings contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    url:
      description:
        - A delegation Url.
      returned: always
      type: str
      sample: null
    validation_key:
      description:
        - >-
          A base64-encoded validation key to validate, that a request is coming
          from Azure API Management.
      returned: always
      type: str
      sample: null
    subscriptions:
      description:
        - Subscriptions delegation settings.
      returned: always
      type: dict
      sample: null
      contains:
        enabled:
          description:
            - Enable or disable delegation for subscriptions.
          returned: always
          type: boolean
          sample: null
    user_registration:
      description:
        - User registration delegation settings.
      returned: always
      type: dict
      sample: null
      contains:
        enabled:
          description:
            - Enable or disable delegation for user registration.
          returned: always
          type: boolean
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


class AzureRMDelegationSettings(AzureRMModuleBaseExt):
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
                disposition='service_name',
                required=true
            ),
            url=dict(
                type='str',
                disposition='/'
            ),
            validation_key=dict(
                type='str',
                disposition='/'
            ),
            subscriptions=dict(
                type='dict',
                disposition='/',
                options=dict(
                    enabled=dict(
                        type='boolean'
                    )
                )
            ),
            user_registration=dict(
                type='dict',
                disposition='/',
                options=dict(
                    enabled=dict(
                        type='boolean'
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
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDelegationSettings, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.delegation_settings.create_or_update(resource_group_name=self.resource_group,
                                                                             service_name=self.name,
                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DelegationSetting instance.')
            self.fail('Error creating the DelegationSetting instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the DelegationSetting instance {0}'.format(self.))
        try:
            response = self.mgmt_client.delegation_settings.delete()
        except CloudError as e:
            self.log('Error attempting to delete the DelegationSetting instance.')
            self.fail('Error deleting the DelegationSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the DelegationSetting instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.delegation_settings.get(resource_group_name=self.resource_group,
                                                                service_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDelegationSettings()


if __name__ == '__main__':
    main()
