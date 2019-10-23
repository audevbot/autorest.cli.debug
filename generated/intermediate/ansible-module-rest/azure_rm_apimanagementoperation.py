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
module: azure_rm_apimanagementoperation
version_added: '2.9'
short_description: Manage Azure ApiManagementOperation instance.
description:
  - 'Create, update and delete instance of Azure ApiManagementOperation.'
options:
  value:
    description:
      - List of operations supported by the resource provider.
    type: list
    suboptions:
      name:
        description:
          - 'Operation name: {provider}/{resource}/{operation}'
        type: str
      display:
        description:
          - The object that describes the operation.
        type: dict
        suboptions:
          provider:
            description:
              - Friendly name of the resource provider
            type: str
          operation:
            description:
              - 'Operation type: read, write, delete, listKeys/action, etc.'
            type: str
          resource:
            description:
              - Resource type on which the operation is performed.
            type: str
          description:
            description:
              - Friendly name of the operation
            type: str
      origin:
        description:
          - The operation origin.
        type: str
  next_link:
    description:
      - URL to get the next set of operation list results if there are any.
    type: str
  state:
    description:
      - Assert the state of the ApiManagementOperation.
      - >-
        Use C(present) to create or update an ApiManagementOperation and
        C(absent) to delete it.
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
[]

'''

RETURN = '''
value:
  description:
    - List of operations supported by the resource provider.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - 'Operation name: {provider}/{resource}/{operation}'
      returned: always
      type: str
      sample: null
    display:
      description:
        - The object that describes the operation.
      returned: always
      type: dict
      sample: null
      contains:
        provider:
          description:
            - Friendly name of the resource provider
          returned: always
          type: str
          sample: null
        operation:
          description:
            - 'Operation type: read, write, delete, listKeys/action, etc.'
          returned: always
          type: str
          sample: null
        resource:
          description:
            - Resource type on which the operation is performed.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Friendly name of the operation
          returned: always
          type: str
          sample: null
    origin:
      description:
        - The operation origin.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - The operation properties.
      returned: always
      type: 'unknown-primary[object]'
      sample: null
next_link:
  description:
    - URL to get the next set of operation list results if there are any.
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
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApiManagementOperations(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            undefined,
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMApiManagementOperations, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url = ('/providers' +
                    '/Microsoft.ApiManagement' +
                    '/operations')

        old_response = self.get_resource()

        if not old_response:
            self.log("ApiManagementOperation instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ApiManagementOperation instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ApiManagementOperation instance')

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
            self.log('ApiManagementOperation instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ApiManagementOperation instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["value"] = response["value"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ApiManagementOperation instance {0}'.format(self.))

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
            self.log('Error attempting to create the ApiManagementOperation instance.')
            self.fail('Error creating the ApiManagementOperation instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ApiManagementOperation instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ApiManagementOperation instance.')
            self.fail('Error deleting the ApiManagementOperation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiManagementOperation instance {0} is present'.format(self.))
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
            # self.log("ApiManagementOperation instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ApiManagementOperation instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMApiManagementOperations()


if __name__ == '__main__':
    main()
