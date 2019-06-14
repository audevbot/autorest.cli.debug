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
module: azure_rm_apimanagementsubscription_info
version_added: '2.9'
short_description: Get Subscription info.
description:
  - Get info of Subscription.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  name:
    description:
      - Resource name.
  sid:
    description:
      - >-
        Subscription entity Identifier. The entity represents the association
        between a user and a product in API Management.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type for API Management resource.
  owner_id:
    description:
      - >-
        The user resource identifier of the subscription owner. The value is a
        valid relative URL in the format of /users/{userId} where {userId} is a
        user identifier.
  scope:
    description:
      - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
    required: true
  display_name:
    description:
      - 'The name of the subscription, or null if the subscription has no name.'
  state:
    description:
      - >-
        Subscription state. Possible states are * active – the subscription is
        active, * suspended – the subscription is blocked, and the subscriber
        cannot call any APIs of the product, * submitted – the subscription
        request has been made by the developer, but has not yet been approved or
        rejected, * rejected – the subscription request has been denied by an
        administrator, * cancelled – the subscription has been cancelled by the
        developer or administrator, * expired – the subscription reached its
        expiration date and was deactivated.
    required: true
  created_date:
    description:
      - >-
        Subscription creation date. The date conforms to the following format:
        `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
      - ''
  start_date:
    description:
      - >-
        Subscription activation date. The setting is for audit purposes only and
        the subscription is not automatically activated. The subscription
        lifecycle can be managed by using the `state` property. The date
        conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
        the ISO 8601 standard.
      - ''
  expiration_date:
    description:
      - >-
        Subscription expiration date. The setting is for audit purposes only and
        the subscription is not automatically expired. The subscription
        lifecycle can be managed by using the `state` property. The date
        conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
        the ISO 8601 standard.
      - ''
  end_date:
    description:
      - >-
        Date when subscription was cancelled or expired. The setting is for
        audit purposes only and the subscription is not automatically cancelled.
        The subscription lifecycle can be managed by using the `state` property.
        The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
        specified by the ISO 8601 standard.
      - ''
  notification_date:
    description:
      - >-
        Upcoming subscription expiration notification date. The date conforms to
        the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
        8601 standard.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListSubscriptions
  azure_rm_apimanagementsubscription_info:
    resource_group: myResourceGroup
    name: myService
- name: ApiManagementGetSubscription
  azure_rm_apimanagementsubscription_info:
    resource_group: myResourceGroup
    name: myService
    sid: 5931a769d8d14f0ad8ce13b8

'''

RETURN = '''
subscription:
  description: >-
    A list of dict results where the key is the name of the Subscription and the
    values are the facts for that Subscription.
  returned: always
  type: complex
  contains:
    subscription_name:
      description: The key is the name of the server that the values relate to.
      type: complex
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


class AzureRMSubscriptionInfo(AzureRMModuleBase):
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
            sid=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.sid = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None

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
        super(AzureRMSubscriptionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None and
            self.sid is not None):
            self.results['subscription'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.name is not None):
            self.results['subscription'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.subscription.get(resource_group_name=self.resource_group,
                                                         service_name=self.name,
                                                         sid=self.sid)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.subscription.list(resource_group_name=self.resource_group,
                                                          service_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMSubscriptionInfo()


if __name__ == '__main__':
    main()
