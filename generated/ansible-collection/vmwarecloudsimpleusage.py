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
module: vmwarecloudsimpleusage
version_added: '2.9'
short_description: Manage Azure Usage instance.
description:
  - 'Create, update and delete instance of Azure Usage.'
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  next_link:
    description:
      - Link for next list of DedicatedCloudNode
    type: str
  value:
    description:
      - The list of usages
    type: list
    suboptions:
      current_value:
        description:
          - The current usage value
        required: true
        type: number
      limit:
        description:
          - >-
            limit of a given sku in a region for a subscription. The maximum
            permitted value for the usage quota. If there is no limit, this
            value will be -1
        required: true
        type: number
      name:
        description:
          - Usage name value and localized name
        type: dict
        suboptions:
          localized_value:
            description:
              - e.g. "Virtual Machines"
            type: str
          value:
            description:
              - 'resource type or resource type sku name, e.g. virtualMachines'
            type: str
      unit:
        description:
          - The usages' unit
        type: str
  state:
    description:
      - Assert the state of the Usage.
      - Use C(present) to create or update an Usage and C(absent) to delete it.
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
next_link:
  description:
    - Link for next list of DedicatedCloudNode
  returned: always
  type: str
  sample: null
value:
  description:
    - The list of usages
  returned: always
  type: dict
  sample: null
  contains:
    current_value:
      description:
        - The current usage value
      returned: always
      type: number
      sample: null
    limit:
      description:
        - >-
          limit of a given sku in a region for a subscription. The maximum
          permitted value for the usage quota. If there is no limit, this value
          will be -1
      returned: always
      type: number
      sample: null
    name:
      description:
        - Usage name value and localized name
      returned: always
      type: dict
      sample: null
      contains:
        localized_value:
          description:
            - e.g. "Virtual Machines"
          returned: always
          type: str
          sample: null
        value:
          description:
            - 'resource type or resource type sku name, e.g. virtualMachines'
          returned: always
          type: str
          sample: null
    unit:
      description:
        - The usages' unit
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


class AzureRMUsages(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                updatable=False,
                disposition='regionId',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.region_id = None
        self.next_link = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMUsages, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/Microsoft.VMwareCloudSimple' +
                    '/locations' +
                    '/{{ location_name }}' +
                    '/usages')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ location_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Usage instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Usage instance already exists')

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
            self.log('Need to Create / Update the Usage instance')

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
            self.log('Usage instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Usage instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["next_link"] = response["next_link"]
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Usage instance {0}'.format(self.))

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
            self.log('Error attempting to create the Usage instance.')
            self.fail('Error creating the Usage instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Usage instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Usage instance.')
            self.fail('Error deleting the Usage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Usage instance {0} is present'.format(self.))
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
            # self.log("Usage instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Usage instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMUsages()


if __name__ == '__main__':
    main()
