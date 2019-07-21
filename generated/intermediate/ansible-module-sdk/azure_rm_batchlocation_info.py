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
module: azure_rm_batchlocation_info
version_added: '2.9'
short_description: Get Location info.
description:
  - Get info of Location.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: LocationGetQuotas
  azure_rm_batchlocation_info:
    name: myLocation

'''

RETURN = '''
location:
  description: >-
    A list of dict results where the key is the name of the Location and the
    values are the facts for that Location.
  returned: always
  type: complex
  contains:
    location_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        account_quota:
          description:
            - >-
              The number of Batch accounts that may be created under the
              subscription in the specified region.
          returned: always
          type: number
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.batch import BatchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLocationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str',
                required=true
            )
        )

        self.name = None
        self.account_quota = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLocationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.name is not None):
            self.results['location'] = self.format_item(self.getquotas())
        return self.results

    def getquotas(self):
        response = None

        try:
            response = self.mgmt_client.location.get_quotas(location_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMLocationInfo()


if __name__ == '__main__':
    main()
