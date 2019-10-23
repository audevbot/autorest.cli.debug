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
module: azure_rm_batchlocation
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


class AzureRMLocation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str',
                updatable=False,
                disposition='location_name',
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

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

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagement,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

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
           self.results["account_quota"] = response["account_quota"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.location.create()
            else:
                response = self.mgmt_client.location.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Location instance.')
            self.fail('Error creating the Location instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Location instance {0}'.format(self.))
        try:
            response = self.mgmt_client.location.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Location instance.')
            self.fail('Error deleting the Location instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Location instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.location.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLocation()


if __name__ == '__main__':
    main()