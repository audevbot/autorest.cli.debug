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
module: azure_rm_subscriptionssubscriptionfactory
version_added: '2.9'
short_description: Manage Azure SubscriptionFactory instance.
description:
  - 'Create, update and delete instance of Azure SubscriptionFactory.'
options:
  enrollment_account_name:
    description:
      - >-
        The name of the enrollment account to which the subscription will be
        billed.
    required: true
    type: str
  name:
    description:
      - The display name of the subscription.
    type: str
  owners:
    description:
      - >-
        The list of principals that should be granted Owner access on the
        subscription. Principals should be of type User, Service Principal or
        Security Group.
    type: list
    suboptions:
      object_id:
        description:
          - Object id of the Principal
        required: true
        type: str
  offer_type:
    description:
      - >-
        The offer type of the subscription. For example, MS-AZR-0017P
        (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement devTest) are
        available. Only valid when creating a subscription in a enrollment
        account scope.
    type: str
  additional_parameters:
    description:
      - >-
        Additional, untyped parameters to support custom subscription creation
        scenarios.
    type: >-
      unknown[DictionaryType
      {"$id":"45","$type":"DictionaryType","valueType":{"$id":"46","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"47","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"48","fixed":false},"deprecated":false}]
  subscription_link:
    description:
      - The link to the new subscription.
    type: str
  state:
    description:
      - Assert the state of the SubscriptionFactory.
      - >-
        Use C(present) to create or update an SubscriptionFactory and C(absent)
        to delete it.
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
- name: createSubscription
  azure_rm_subscriptionssubscriptionfactory:
    enrollment_account_name: myEnrollmentAccount
    body:
      offerType: MS-AZR-0017P
      displayName: Test Ea Azure Sub
      owners:
        - objectId: 973034ff-acb7-409c-b731-e789672c7b31
        - objectId: 67439a9e-8519-4016-a630-f5f805eba567
      additionalParameters:
        customData:
          key1: value1
          key2: true

'''

RETURN = '''
subscription_link:
  description:
    - The link to the new subscription.
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


class AzureRMSubscriptionFactory(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            enrollment_account_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            owners=dict(
                type='list',
                disposition='/',
                options=dict(
                    object_id=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            offer_type=dict(
                type='str',
                updatable=False,
                disposition='/',
                choices=['MS-AZR-0017P',
                         'MS-AZR-0148P']
            ),
            additional_parameters=dict(
                type='unknown[DictionaryType {"$id":"45","$type":"DictionaryType","valueType":{"$id":"46","$type":"PrimaryType","knownPrimaryType":"object","name":{"$id":"47","fixed":false,"raw":"Object"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"48","fixed":false},"deprecated":false}]',
                updatable=False,
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.enrollment_account_name = None
        self.subscription_link = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSubscriptionFactory, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["subscription_link"] = response["subscription_link"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.subscription_factory.create()
            else:
                response = self.mgmt_client.subscription_factory.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SubscriptionFactory instance.')
            self.fail('Error creating the SubscriptionFactory instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the SubscriptionFactory instance {0}'.format(self.))
        try:
            response = self.mgmt_client.subscription_factory.delete()
        except CloudError as e:
            self.log('Error attempting to delete the SubscriptionFactory instance.')
            self.fail('Error deleting the SubscriptionFactory instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the SubscriptionFactory instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.subscription_factory.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSubscriptionFactory()


if __name__ == '__main__':
    main()
