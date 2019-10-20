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
module: azure_rm_batchapplicationpackage
version_added: '2.9'
short_description: Manage Azure ApplicationPackage instance.
description:
  - 'Create, update and delete instance of Azure ApplicationPackage.'
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
    type: str
  account_name:
    description:
      - The name of the Batch account.
    required: true
    type: str
  application_name:
    description:
      - The name of the application. This must be unique within the account.
    required: true
    type: str
  version_name:
    description:
      - The version of the application.
    required: true
    type: str
  state:
    description:
      - Assert the state of the ApplicationPackage.
      - >-
        Use C(present) to create or update an ApplicationPackage and C(absent)
        to delete it.
    default: present
    choices:
      - absent
      - present
  format:
    description:
      - 'The format of the application package, if the package is active.'
    type: str
  storage_url:
    description:
      - The URL for the application package in Azure Storage.
    type: str
  storage_url_expiry:
    description:
      - The UTC time at which the Azure Storage URL will expire.
    type: datetime
  last_activation_time:
    description:
      - >-
        The time at which the package was last activated, if the package is
        active.
    type: datetime
  id:
    description:
      - The ID of the resource.
    type: str
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApplicationPackageCreate
  azure_rm_batchapplicationpackage:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    application_name: myApplication
    version_name: myVersion
- name: ApplicationPackageDelete
  azure_rm_batchapplicationpackage:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    application_name: myApplication
    version_name: myVersion
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
    - The properties associated with the Application Package.
  returned: always
  type: dict
  sample: null
  contains:
    state:
      description:
        - The current state of the application package.
      returned: always
      type: str
      sample: null
    format:
      description:
        - 'The format of the application package, if the package is active.'
      returned: always
      type: str
      sample: null
    storage_url:
      description:
        - The URL for the application package in Azure Storage.
      returned: always
      type: str
      sample: null
    storage_url_expiry:
      description:
        - The UTC time at which the Azure Storage URL will expire.
      returned: always
      type: datetime
      sample: null
    last_activation_time:
      description:
        - >-
          The time at which the package was last activated, if the package is
          active.
      returned: always
      type: datetime
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


class AzureRMApplicationPackage(AzureRMModuleBaseExt):
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
            application_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            version_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.application_name = None
        self.version_name = None
        self.id = None
        self.etag = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApplicationPackage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.application_package.create(resource_group_name=self.resource_group,
                                                                       account_name=self.account_name,
                                                                       application_name=self.application_name,
                                                                       version_name=self.version_name)
            else:
                response = self.mgmt_client.application_package.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ApplicationPackage instance.')
            self.fail('Error creating the ApplicationPackage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ApplicationPackage instance {0}'.format(self.))
        try:
            response = self.mgmt_client.application_package.delete(resource_group_name=self.resource_group,
                                                                   account_name=self.account_name,
                                                                   application_name=self.application_name,
                                                                   version_name=self.version_name)
        except CloudError as e:
            self.log('Error attempting to delete the ApplicationPackage instance.')
            self.fail('Error deleting the ApplicationPackage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApplicationPackage instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.application_package.get(resource_group_name=self.resource_group,
                                                                account_name=self.account_name,
                                                                application_name=self.application_name,
                                                                version_name=self.version_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApplicationPackage()


if __name__ == '__main__':
    main()
