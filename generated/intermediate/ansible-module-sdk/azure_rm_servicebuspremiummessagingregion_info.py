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
module: azure_rm_servicebuspremiummessagingregion_info
version_added: '2.9'
short_description: Get PremiumMessagingRegion info.
description:
  - Get info of PremiumMessagingRegion.
options:
  value:
    description:
      - Result of the List PremiumMessagingRegions type.
    type: list
    suboptions:
      id:
        description:
          - Resource Id
      name:
        description:
          - Resource name
      type:
        description:
          - Resource type
      location:
        description:
          - Resource location
      code:
        description:
          - Region code
      full_name:
        description:
          - Full name of the region
  next_link:
    description:
      - >-
        Link to the next set of results. Not empty if Value contains incomplete
        list of PremiumMessagingRegions.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: PremiumMessagingRegionsList
  azure_rm_servicebuspremiummessagingregion_info: {}

'''

RETURN = '''
premium_messaging_regions:
  description: >-
    A list of dict results where the key is the name of the
    PremiumMessagingRegion and the values are the facts for that
    PremiumMessagingRegion.
  returned: always
  type: complex
  contains:
    premiummessagingregion_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Result of the List PremiumMessagingRegions type.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource Id
              returned: always
              type: str
              sample: null
            name:
              description:
                - Resource name
              returned: always
              type: str
              sample: null
            type:
              description:
                - Resource type
              returned: always
              type: str
              sample: null
            location:
              description:
                - Resource location
              returned: always
              type: str
              sample: null
            tags:
              description:
                - Resource tags
              returned: always
              type: >-
                unknown[DictionaryType
                {"$id":"49","$type":"DictionaryType","valueType":{"$id":"50","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"51","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"52","fixed":false},"deprecated":false}]
              sample: null
            properties:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: dict
              sample: null
            code:
              description:
                - Region code
              returned: always
              type: str
              sample: null
            full_name:
              description:
                - Full name of the region
              returned: always
              type: str
              sample: null
        next_link:
          description:
            - >-
              Link to the next set of results. Not empty if Value contains
              incomplete list of PremiumMessagingRegions.
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMPremiumMessagingRegionsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )

        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPremiumMessagingRegionsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        else:
            self.results['premium_messaging_regions'] = [self.format_item(self.list())]
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.premium_messaging_regions.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMPremiumMessagingRegionsInfo()


if __name__ == '__main__':
    main()
