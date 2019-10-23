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
module: batchlocation
version_added: '2.9'
short_description: Manage Azure Location instance.
description:
  - 'Create, update and delete instance of Azure Location.'
options:
  name:
    description:
      - The region for which to retrieve Batch service quotas.
    required: true
    type: str
  account_quota:
    description:
      - >-
        The number of Batch accounts that may be created under the subscription
        in the specified region.
    type: number
  state:
    description:
      - Assert the state of the Location.
      - >-
        Use C(present) to create or update an Location and C(absent) to delete
        it.
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
account_quota:
  description:
    - >-
      The number of Batch accounts that may be created under the subscription in
      the specified region.
  returned: always
  type: number
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


class AzureRMLocation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str',
                updatable=False,
                disposition='locationName',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.name = None
        self.account_quota = None

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

        super(AzureRMLocation, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/locations' +
                    '/{{ location_name }}' +
                    '/quotas')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ location_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Location instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Location instance already exists')

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
            self.log('Need to Create / Update the Location instance')

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
            self.log('Location instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Location instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["account_quota"] = response["account_quota"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Location instance {0}'.format(self.))

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
            self.log('Error attempting to create the Location instance.')
            self.fail('Error creating the Location instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Location instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Location instance.')
            self.fail('Error deleting the Location instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Location instance {0} is present'.format(self.))
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
            # self.log("Location instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Location instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMLocation()


if __name__ == '__main__':
    main()
