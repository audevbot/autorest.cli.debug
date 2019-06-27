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
module: azure_rm_recoveryservicesreplicationlogicalnetwork_info
version_added: '2.9'
short_description: Get ReplicationLogicalNetwork info.
description:
  - Get info of ReplicationLogicalNetwork.
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
    required: true
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
  friendly_name:
    description:
      - The Friendly Name.
  network_virtualization_status:
    description:
      - >-
        A value indicating whether Network Virtualization is enabled for the
        logical network.
  logical_network_usage:
    description:
      - >-
        A value indicating whether logical network is used as private test
        network by test failover.
  logical_network_definitions_status:
    description:
      - A value indicating whether logical network definitions are isolated.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of logical networks under a fabric.
  azure_rm_recoveryservicesreplicationlogicalnetwork_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
- name: Gets a logical network with specified server id and logical network name.
  azure_rm_recoveryservicesreplicationlogicalnetwork_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    name: myReplicationLogicalNetwork

'''

RETURN = '''
replication_logical_networks:
  description: >-
    A list of dict results where the key is the name of the
    ReplicationLogicalNetwork and the values are the facts for that
    ReplicationLogicalNetwork.
  returned: always
  type: complex
  contains:
    replicationlogicalnetwork_name:
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
            - The Logical Network Properties.
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


class AzureRMReplicationLogicalNetworksInfo(AzureRMModuleBase):
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
                type='str',
                required=true
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
        super(AzureRMReplicationLogicalNetworksInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.name is not None):
            self.results['replication_logical_networks'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None):
            self.results['replication_logical_networks'] = self.format_item(self.listbyreplicationfabrics())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.replication_logical_networks.get(resource_name=self.resource_name,
                                                                         resource_group_name=self.resource_group,
                                                                         fabric_name=self.fabric_name,
                                                                         logical_network_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyreplicationfabrics(self):
        response = None

        try:
            response = self.mgmt_client.replication_logical_networks.list_by_replication_fabrics(resource_name=self.resource_name,
                                                                                                 resource_group_name=self.resource_group,
                                                                                                 fabric_name=self.fabric_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMReplicationLogicalNetworksInfo()


if __name__ == '__main__':
    main()
