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
module: azure_rm_frontdoorbackendpool_info
version_added: '2.9'
short_description: Get BackendPool info.
description:
  - Get info of BackendPool.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  backends:
    description:
      - The set of backends for this pool
    type: list
    suboptions:
      address:
        description:
          - Location of the backend (IP address or FQDN)
        type: str
      http_port:
        description:
          - The HTTP TCP port number. Must be between 1 and 65535.
        type: number
      https_port:
        description:
          - The HTTPS TCP port number. Must be between 1 and 65535.
        type: number
      enabled_state:
        description:
          - >-
            Whether to enable use of this backend. Permitted values are
            'Enabled' or 'Disabled'
        type: str
      priority:
        description:
          - >-
            Priority to use for load balancing. Higher priorities will not be
            used for load balancing if any lower priority backend is healthy.
        type: number
      weight:
        description:
          - Weight of this endpoint for load balancing purposes.
        type: number
      backend_host_header:
        description:
          - >-
            The value to use as the host header sent to the backend. If blank or
            unspecified, this defaults to the incoming host.
        type: str
  load_balancing_settings:
    description:
      - Load balancing settings for a backend pool
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  health_probe_settings:
    description:
      - L7 health probe settings for a backend pool
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  resource_state:
    description:
      - Resource status.
    type: str
  type:
    description:
      - Resource type.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List Backend Pools in a Front Door
  azure_rm_frontdoorbackendpool_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
- name: Get Backend Pool
  azure_rm_frontdoorbackendpool_info:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myBackendPool

'''

RETURN = '''
backend_pools:
  description: >-
    A list of dict results where the key is the name of the BackendPool and the
    values are the facts for that BackendPool.
  returned: always
  type: complex
  contains:
    backendpool_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the Front Door Backend Pool
          returned: always
          type: dict
          sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type.
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
    from azure.mgmt.frontdoor import FrontdoorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBackendPoolsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            front_door_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.front_door_name = None
        self.name = None
        self.id = None
        self.properties = None
        self.name = None
        self.type = None

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
        super(AzureRMBackendPoolsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontdoorClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.front_door_name is not None and
            self.name is not None):
            self.results['backend_pools'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.front_door_name is not None):
            self.results['backend_pools'] = self.format_item(self.listbyfrontdoor())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.backend_pools.get(resource_group_name=self.resource_group,
                                                          front_door_name=self.front_door_name,
                                                          backend_pool_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyfrontdoor(self):
        response = None

        try:
            response = self.mgmt_client.backend_pools.list_by_front_door(resource_group_name=self.resource_group,
                                                                         front_door_name=self.front_door_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMBackendPoolsInfo()


if __name__ == '__main__':
    main()
