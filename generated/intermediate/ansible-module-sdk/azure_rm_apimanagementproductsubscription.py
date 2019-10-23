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
module: azure_rm_apimanagementproductsubscription
version_added: '2.9'
short_description: Manage Azure ProductSubscription instance.
description:
  - 'Create, update and delete instance of Azure ProductSubscription.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
      name:
        description:
          - Resource name.
        type: str
      type:
        description:
          - Resource type for API Management resource.
        type: str
      owner_id:
        description:
          - >-
            The user resource identifier of the subscription owner. The value is
            a valid relative URL in the format of /users/{userId} where {userId}
            is a user identifier.
        type: str
      scope:
        description:
          - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
        required: true
        type: str
      display_name:
        description:
          - >-
            The name of the subscription, or null if the subscription has no
            name.
        type: str
      state:
        description:
          - >-
            Subscription state. Possible states are * active – the subscription
            is active, * suspended – the subscription is blocked, and the
            subscriber cannot call any APIs of the product, * submitted – the
            subscription request has been made by the developer, but has not yet
            been approved or rejected, * rejected – the subscription request has
            been denied by an administrator, * cancelled – the subscription has
            been cancelled by the developer or administrator, * expired – the
            subscription reached its expiration date and was deactivated.
        required: true
        type: str
      created_date:
        description:
          - >-
            Subscription creation date. The date conforms to the following
            format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
            standard.<br>
        type: datetime
      start_date:
        description:
          - >-
            Subscription activation date. The setting is for audit purposes only
            and the subscription is not automatically activated. The
            subscription lifecycle can be managed by using the `state` property.
            The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.<br>
        type: datetime
      expiration_date:
        description:
          - >-
            Subscription expiration date. The setting is for audit purposes only
            and the subscription is not automatically expired. The subscription
            lifecycle can be managed by using the `state` property. The date
            conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.<br>
        type: datetime
      end_date:
        description:
          - >-
            Date when subscription was cancelled or expired. The setting is for
            audit purposes only and the subscription is not automatically
            cancelled. The subscription lifecycle can be managed by using the
            `state` property. The date conforms to the following format:
            `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
        type: datetime
      notification_date:
        description:
          - >-
            Upcoming subscription expiration notification date. The date
            conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.<br>
        type: datetime
      primary_key:
        description:
          - Subscription primary key.
        required: true
        type: str
      secondary_key:
        description:
          - Subscription secondary key.
        required: true
        type: str
      state_comment:
        description:
          - Optional subscription comment added by an administrator.
        type: str
      allow_tracing:
        description:
          - Determines whether tracing is enabled
        type: boolean
  next_link:
    description:
      - Next page link if any.
    type: str
  state:
    description:
      - Assert the state of the ProductSubscription.
      - >-
        Use C(present) to create or update an ProductSubscription and C(absent)
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
[]

'''

RETURN = '''
value:
  description:
    - Page values.
  returned: always
  type: dict
  sample: null
  contains:
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
        - Subscription contract properties.
      returned: always
      type: dict
      sample: null
    owner_id:
      description:
        - >-
          The user resource identifier of the subscription owner. The value is a
          valid relative URL in the format of /users/{userId} where {userId} is
          a user identifier.
      returned: always
      type: str
      sample: null
    scope:
      description:
        - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - 'The name of the subscription, or null if the subscription has no name.'
      returned: always
      type: str
      sample: null
    state:
      description:
        - >-
          Subscription state. Possible states are * active – the subscription is
          active, * suspended – the subscription is blocked, and the subscriber
          cannot call any APIs of the product, * submitted – the subscription
          request has been made by the developer, but has not yet been approved
          or rejected, * rejected – the subscription request has been denied by
          an administrator, * cancelled – the subscription has been cancelled by
          the developer or administrator, * expired – the subscription reached
          its expiration date and was deactivated.
      returned: always
      type: str
      sample: null
    created_date:
      description:
        - >-
          Subscription creation date. The date conforms to the following format:
          `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    start_date:
      description:
        - >-
          Subscription activation date. The setting is for audit purposes only
          and the subscription is not automatically activated. The subscription
          lifecycle can be managed by using the `state` property. The date
          conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
          by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    expiration_date:
      description:
        - >-
          Subscription expiration date. The setting is for audit purposes only
          and the subscription is not automatically expired. The subscription
          lifecycle can be managed by using the `state` property. The date
          conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
          by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    end_date:
      description:
        - >-
          Date when subscription was cancelled or expired. The setting is for
          audit purposes only and the subscription is not automatically
          cancelled. The subscription lifecycle can be managed by using the
          `state` property. The date conforms to the following format:
          `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    notification_date:
      description:
        - >-
          Upcoming subscription expiration notification date. The date conforms
          to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the
          ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    primary_key:
      description:
        - Subscription primary key.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - Subscription secondary key.
      returned: always
      type: str
      sample: null
    state_comment:
      description:
        - Optional subscription comment added by an administrator.
      returned: always
      type: str
      sample: null
    allow_tracing:
      description:
        - Determines whether tracing is enabled
      returned: always
      type: boolean
      sample: null
next_link:
  description:
    - Next page link if any.
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMProductSubscriptions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            product_id=dict(
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
        self.service_name = None
        self.product_id = None
        self.value = None
        self.next_link = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMProductSubscriptions, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["value"] = response["value"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.product_subscriptions.create()
            else:
                response = self.mgmt_client.product_subscriptions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ProductSubscription instance.')
            self.fail('Error creating the ProductSubscription instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ProductSubscription instance {0}'.format(self.))
        try:
            response = self.mgmt_client.product_subscriptions.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ProductSubscription instance.')
            self.fail('Error deleting the ProductSubscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ProductSubscription instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.product_subscriptions.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMProductSubscriptions()


if __name__ == '__main__':
    main()
