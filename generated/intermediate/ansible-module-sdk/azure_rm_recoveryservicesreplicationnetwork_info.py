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
module: azure_rm_recoveryservicesreplicationnetwork_info
version_added: '2.9'
short_description: Get ReplicationNetwork info.
description:
  - Get info of ReplicationNetwork.
options:
  resource_name:
    description:
      - The name of the recovery services vault.
    required: true
  resource_group:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
  fabric_name:
    description:
      - Server Id.
  name:
    description:
      - Resource Name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource Type
  location:
    description:
      - Resource Location
  fabric_type:
    description:
      - The Fabric Type.
  subnets:
    description:
      - The List of subnets.
    type: list
    suboptions:
      name:
        description:
          - The subnet name.
      friendly_name:
        description:
          - The subnet friendly name.
      address_list:
        description:
          - The list of addresses for the subnet.
        type: list
  friendly_name:
    description:
      - The Friendly Name.
  network_type:
    description:
      - The Network Type.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of networks. View-only API.
  azure_rm_recoveryservicesreplicationnetwork_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the list of networks under a fabric.
  azure_rm_recoveryservicesreplicationnetwork_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
- name: Gets a network with specified server id and network name.
  azure_rm_recoveryservicesreplicationnetwork_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    name: myReplicationNetwork

'''

RETURN = '''
replication_networks:
  description: >-
    A list of dict results where the key is the name of the ReplicationNetwork
    and the values are the facts for that ReplicationNetwork.
  returned: always
  type: complex
  contains:
    replicationnetwork_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource Name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource Type
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource Location
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The Network Properties.
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
    from azure.mgmt.recoveryservices import RecoveryServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReplicationNetworksInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                required=true
            ),
            resource_group=dict(
                type='str',
                required=true
            ),
            fabric_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.fabric_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-10'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReplicationNetworksInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.name is not None):
            self.results['replication_networks'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None):
            self.results['replication_networks'] = self.format_item(self.listbyreplicationfabrics())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_networks'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.replication_networks.get(resource_name=self.resource_name,
                                                                 resource_group_name=self.resource_group,
                                                                 fabric_name=self.fabric_name,
                                                                 network_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyreplicationfabrics(self):
        response = None

        try:
            response = self.mgmt_client.replication_networks.list_by_replication_fabrics(resource_name=self.resource_name,
                                                                                         resource_group_name=self.resource_group,
                                                                                         fabric_name=self.fabric_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.replication_networks.list(resource_name=self.resource_name,
                                                                  resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMReplicationNetworksInfo()


if __name__ == '__main__':
    main()
