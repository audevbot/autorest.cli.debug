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
module: azure_rm_apimanagementusersubscription_info
version_added: '2.9'
short_description: Get UserSubscription info.
description:
  - Get info of UserSubscription.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - The name of the API Management service.
    required: true
  user_id:
    description:
      - >-
        User identifier. Must be unique in the current API Management service
        instance.
    required: true
  value:
    description:
      - Page values.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
      name:
        description:
          - Resource name.
      type:
        description:
          - Resource type for API Management resource.
      owner_id:
        description:
          - >-
            The user resource identifier of the subscription owner. The value is
            a valid relative URL in the format of /users/{userId} where {userId}
            is a user identifier.
      scope:
        description:
          - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
        required: true
      display_name:
        description:
          - >-
            The name of the subscription, or null if the subscription has no
            name.
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
      created_date:
        description:
          - >-
            Subscription creation date. The date conforms to the following
            format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
            standard.
          - ''
      start_date:
        description:
          - >-
            Subscription activation date. The setting is for audit purposes only
            and the subscription is not automatically activated. The
            subscription lifecycle can be managed by using the `state` property.
            The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.
          - ''
      expiration_date:
        description:
          - >-
            Subscription expiration date. The setting is for audit purposes only
            and the subscription is not automatically expired. The subscription
            lifecycle can be managed by using the `state` property. The date
            conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.
          - ''
      end_date:
        description:
          - >-
            Date when subscription was cancelled or expired. The setting is for
            audit purposes only and the subscription is not automatically
            cancelled. The subscription lifecycle can be managed by using the
            `state` property. The date conforms to the following format:
            `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
          - ''
      notification_date:
        description:
          - >-
            Upcoming subscription expiration notification date. The date
            conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
            specified by the ISO 8601 standard.
          - ''
      primary_key:
        description:
          - Subscription primary key.
        required: true
      secondary_key:
        description:
          - Subscription secondary key.
        required: true
      state_comment:
        description:
          - Optional subscription comment added by an administrator.
      allow_tracing:
        description:
          - Determines whether tracing is enabled
  next_link:
    description:
      - Next page link if any.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListUserSubscriptions
  azure_rm_apimanagementusersubscription_info:
    resource_group: myResourceGroup
    name: myService
    user_id: myUser

'''

RETURN = '''
user_subscription:
  description: >-
    A list of dict results where the key is the name of the UserSubscription and
    the values are the facts for that UserSubscription.
  returned: always
  type: complex
  contains:
    usersubscription_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
                  The user resource identifier of the subscription owner. The
                  value is a valid relative URL in the format of /users/{userId}
                  where {userId} is a user identifier.
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
                - >-
                  The name of the subscription, or null if the subscription has
                  no name.
              returned: always
              type: str
              sample: null
            state:
              description:
                - >-
                  Subscription state. Possible states are * active – the
                  subscription is active, * suspended – the subscription is
                  blocked, and the subscriber cannot call any APIs of the
                  product, * submitted – the subscription request has been made
                  by the developer, but has not yet been approved or rejected, *
                  rejected – the subscription request has been denied by an
                  administrator, * cancelled – the subscription has been
                  cancelled by the developer or administrator, * expired – the
                  subscription reached its expiration date and was deactivated.
              returned: always
              type: str
              sample: null
            created_date:
              description:
                - >
                  Subscription creation date. The date conforms to the following
                  format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
                  standard.
              returned: always
              type: datetime
              sample: null
            start_date:
              description:
                - >
                  Subscription activation date. The setting is for audit
                  purposes only and the subscription is not automatically
                  activated. The subscription lifecycle can be managed by using
                  the `state` property. The date conforms to the following
                  format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
                  standard.
              returned: always
              type: datetime
              sample: null
            expiration_date:
              description:
                - >
                  Subscription expiration date. The setting is for audit
                  purposes only and the subscription is not automatically
                  expired. The subscription lifecycle can be managed by using
                  the `state` property. The date conforms to the following
                  format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
                  standard.
              returned: always
              type: datetime
              sample: null
            end_date:
              description:
                - >
                  Date when subscription was cancelled or expired. The setting
                  is for audit purposes only and the subscription is not
                  automatically cancelled. The subscription lifecycle can be
                  managed by using the `state` property. The date conforms to
                  the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
                  the ISO 8601 standard.
              returned: always
              type: datetime
              sample: null
            notification_date:
              description:
                - >
                  Upcoming subscription expiration notification date. The date
                  conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
                  specified by the ISO 8601 standard.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMUserSubscriptionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            ),
            user_id=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.user_id = None
        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMUserSubscriptionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.user_id is not None):
            self.results['user_subscription'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.user_subscription.list(resource_group_name=self.resource_group,
                                                               service_name=self.name,
                                                               user_id=self.user_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMUserSubscriptionInfo()


if __name__ == '__main__':
    main()
