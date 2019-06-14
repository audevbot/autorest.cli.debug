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
module: azure_rm_batchapplication
version_added: '2.9'
short_description: Manage Azure Application instance.
description:
  - 'Create, update and delete instance of Azure Application.'
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
  account_name:
    description:
      - The name of the Batch account.
    required: true
  name:
    description:
      - The name of the application. This must be unique within the account.
    required: true
  display_name:
    description:
      - The display name for the application.
  allow_updates:
    description:
      - >-
        A value indicating whether packages within the application may be
        overwritten using the same version string.
  default_version:
    description:
      - >-
        The package to use if a client requests the application but does not
        specify a version. This property can only be set to the name of an
        existing package.
  id:
    description:
      - The ID of the resource.
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
  state:
    description:
      - Assert the state of the Application.
      - >-
        Use C(present) to create or update an Application and C(absent) to
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
- name: ApplicationCreate
  azure_rm_batchapplication:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myApplication
    display_name: myAppName
    allow_updates: false
- name: ApplicationUpdate
  azure_rm_batchapplication:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myApplication
    display_name: myAppName
    allow_updates: true
    default_version: '2'
- name: ApplicationDelete
  azure_rm_batchapplication:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myApplication
    state: absent

'''

RETURN = '''
id:
  description:
    - The ID of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
etag:
  description:
    - 'The ETag of the resource, used for concurrency statements.'
  returned: always
  type: str
  sample: null
properties:
  description:
    - The properties associated with the Application.
  returned: always
  type: dict
  sample: null
  contains:
    display_name:
      description:
        - The display name for the application.
      returned: always
      type: str
      sample: null
    allow_updates:
      description:
        - >-
          A value indicating whether packages within the application may be
          overwritten using the same version string.
      returned: always
      type: boolean
      sample: null
    default_version:
      description:
        - >-
          The package to use if a client requests the application but does not
          specify a version. This property can only be set to the name of an
          existing package.
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
    from azure.mgmt.batch import BatchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApplication(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            account_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='application_name',
                required=true
            ),
            display_name=dict(
                type='str',
                disposition='/'
            ),
            allow_updates=dict(
                type='boolean',
                disposition='/'
            ),
            default_version=dict(
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
        self.account_name = None
        self.name = None
        self.id = None
        self.etag = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplication, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagement,
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
           self.results["etag"] = response["etag"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.application.create(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               application_name=self.name)
            else:
                response = self.mgmt_client.application.update(resource_group_name=self.resource_group,
                                                               account_name=self.account_name,
                                                               application_name=self.name,
                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Application instance.')
            self.fail('Error creating the Application instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Application instance {0}'.format(self.))
        try:
            response = self.mgmt_client.application.delete(resource_group_name=self.resource_group,
                                                           account_name=self.account_name,
                                                           application_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Application instance.')
            self.fail('Error deleting the Application instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Application instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.application.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        application_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApplication()


if __name__ == '__main__':
    main()
