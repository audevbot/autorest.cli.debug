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
module: batchapplication
version_added: '2.9'
short_description: Manage Azure Application instance.
description:
  - 'Create, update and delete instance of Azure Application.'
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
  name:
    description:
      - The name of the application. This must be unique within the account.
    required: true
    type: str
  display_name:
    description:
      - The display name for the application.
    type: str
  allow_updates:
    description:
      - >-
        A value indicating whether packages within the application may be
        overwritten using the same version string.
    type: boolean
  default_version:
    description:
      - >-
        The package to use if a client requests the application but does not
        specify a version. This property can only be set to the name of an
        existing package.
    type: str
  id:
    description:
      - The ID of the resource.
    type: str
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
    type: str
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
  azure.rm.batchapplication:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myApplication
    display_name: myAppName
    allow_updates: false
- name: ApplicationUpdate
  azure.rm.batchapplication:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myApplication
    display_name: myAppName
    allow_updates: true
    default_version: '2'
- name: ApplicationDelete
  azure.rm.batchapplication:
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApplication(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            account_name=dict(
                type='str',
                updatable=False,
                disposition='accountName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='applicationName',
                required=true
            ),
            display_name=dict(
                type='str',
                disposition='/properties/displayName'
            ),
            allow_updates=dict(
                type='boolean',
                disposition='/properties/allowUpdates'
            ),
            default_version=dict(
                type='str',
                disposition='/properties/defaultVersion'
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

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/batchAccounts' +
                    '/{{ batch_account_name }}' +
                    '/applications' +
                    '/{{ application_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ batch_account_name }}', self.batch_account_name)
        self.url = self.url.replace('{{ application_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Application instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Application instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the Application instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('Application instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Application instance unchanged')
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
        # self.log('Creating / Updating the Application instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the Application instance.')
            self.fail('Error creating the Application instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Application instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the Application instance.')
            self.fail('Error deleting the Application instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Application instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("Application instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Application instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMApplication()


if __name__ == '__main__':
    main()
