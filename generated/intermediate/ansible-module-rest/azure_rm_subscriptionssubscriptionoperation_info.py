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
      status:
        description:
          - Status of the pending subscription
      status_detail:
        description:
          - Status Detail of the pending subscription
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        else:
            self.results['subscription_operations'] = [self.format_item(self.list())]
        return self.results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/providers' +
                    '/Microsoft.Subscription' +
                    '/subscriptionOperations')

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMSubscriptionOperationsInfo()


if __name__ == '__main__':
    main()
