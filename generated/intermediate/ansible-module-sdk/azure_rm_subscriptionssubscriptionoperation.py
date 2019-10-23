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
module: azure_rm_subscriptionssubscriptionoperation
version_added: '2.9'
short_description: Manage Azure SubscriptionOperation instance.
description:
  - 'Create, update and delete instance of Azure SubscriptionOperation.'
options:
  value:
    description:
      - A list of pending SubscriptionOperations
    type: list
    suboptions:
      id:
        description:
          - The operation Id.
        type: str
      status:
        description:
          - Status of the pending subscription
        type: str
      status_detail:
        description:
          - Status Detail of the pending subscription
        type: str
  state:
    description:
      - Assert the state of the SubscriptionOperation.
      - >-
        Use C(present) to create or update an SubscriptionOperation and
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
    - A list of pending SubscriptionOperations
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - The operation Id.
      returned: always
      type: str
      sample: null
    status:
      description:
        - Status of the pending subscription
      returned: always
      type: str
      sample: null
    status_detail:
      description:
        - Status Detail of the pending subscription
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
    from azure.mgmt.subscriptions import SubscriptionClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSubscriptionOperations(AzureRMModuleBaseExt):
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSubscriptionOperations, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Subscription,
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
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.subscription_operations.create()
            else:
                response = self.mgmt_client.subscription_operations.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SubscriptionOperation instance.')
            self.fail('Error creating the SubscriptionOperation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the SubscriptionOperation instance {0}'.format(self.))
        try:
            response = self.mgmt_client.subscription_operations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the SubscriptionOperation instance.')
            self.fail('Error deleting the SubscriptionOperation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the SubscriptionOperation instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.subscription_operations.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSubscriptionOperations()


if __name__ == '__main__':
    main()