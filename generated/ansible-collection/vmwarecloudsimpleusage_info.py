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
module: vmwarecloudsimpleusage_info
version_added: '2.9'
short_description: Get Usage info.
description:
  - Get info of Usage.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListUsages
  azure.rm.vmwarecloudsimpleusage.info:
    region_id: myLocation

'''

RETURN = '''
usages:
  description: >-
    A list of dict results where the key is the name of the Usage and the values
    are the facts for that Usage.
  returned: always
  type: complex
  contains:
    usage_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
                  limit of a given sku in a region for a subscription. The
                  maximum permitted value for the usage quota. If there is no
                  limit, this value will be -1
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
                    - >-
                      resource type or resource type sku name, e.g.
                      virtualMachines
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMUsagesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=true
            )
        )

        self.region_id = None
        self.next_link = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMUsagesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None):
            self.results['usages'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.VMwareCloudSimple' +
                    '/locations' +
                    '/{{ location_name }}' +
                    '/usages')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ location_name }}', self.name)

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
    AzureRMUsagesInfo()


if __name__ == '__main__':
    main()
