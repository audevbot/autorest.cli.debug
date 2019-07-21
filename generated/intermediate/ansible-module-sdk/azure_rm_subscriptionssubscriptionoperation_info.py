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
module: azure_rm_subscriptionssubscriptionoperation_info
version_added: '2.9'
short_description: Get SubscriptionOperation info.
description:
  - Get info of SubscriptionOperation.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: getPendingSubscriptionOperations
  azure_rm_subscriptionssubscriptionoperation_info: {}

'''

RETURN = '''
subscription_operations:
  description: >-
    A list of dict results where the key is the name of the
    SubscriptionOperation and the values are the facts for that
    SubscriptionOperation.
  returned: always
  type: complex
  contains:
    subscriptionoperation_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.subscriptions import SubscriptionClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSubscriptionOperationsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )

        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSubscriptionOperationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SubscriptionClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        else:
            self.results['subscription_operations'] = [self.format_item(self.list())]
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.subscription_operations.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMSubscriptionOperationsInfo()


if __name__ == '__main__':
    main()
