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
module: azure_rm_vmwarecloudsimplededicatedcloudnode_info
version_added: '2.9'
short_description: Get DedicatedCloudNode info.
description:
  - Get info of DedicatedCloudNode.
options:
  resource_group:
    description:
      - The name of the resource group
    type: str
  name:
    description:
      - '{dedicatedCloudNodeName}'
    type: str
  id:
    description:
      - >-
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName}
    type: str
  location:
    description:
      - Azure region
    type: str
  availability_zone_id:
    description:
      - 'Availability Zone id, e.g. "az1"'
    required: true
    type: str
  availability_zone_name:
    description:
      - 'Availability Zone name, e.g. "Availability Zone 1"'
    type: str
  cloud_rack_name:
    description:
      - VMWare Cloud Rack Name
    type: str
  created:
    description:
      - date time the resource was created
    type: 'unknown-primary[object]'
  nodes_count:
    description:
      - count of nodes to create
    required: true
    type: number
  placement_group_id:
    description:
      - 'Placement Group id, e.g. "n1"'
    required: true
    type: str
  placement_group_name:
    description:
      - 'Placement Name, e.g. "Placement Group 1"'
    type: str
  private_cloud_id:
    description:
      - Private Cloud Id
    type: str
  private_cloud_name:
    description:
      - Resource Pool Name
    type: str
  provisioning_state:
    description:
      - The provisioning status of the resource
    type: str
  purchase_id:
    description:
      - purchase id
    required: true
    type: 'unknown-primary[uuid]'
  sku_description:
    description:
      - >-
        dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon® Processor E5-2640
        v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz DDR4 ECC
        Registered DIMM, ...
    type: str
  status:
    description:
      - 'Node status, indicates is private cloud set up on this node or not'
    type: str
  vmware_cluster_name:
    description:
      - VMWare Cluster Name
    type: str
  sku_capacity:
    description:
      - The capacity of the SKU
    type: str
  sku_family:
    description:
      - >-
        If the service has different generations of hardware, for the same SKU,
        then that can be captured here
    type: str
  sku_name:
    description:
      - The name of the SKU for VMWare CloudSimple Node
    required: true
    type: str
  sku_tier:
    description:
      - The tier of the SKU
    type: str
  type:
    description:
      - '{resourceProviderNamespace}/{resourceType}'
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListDedicatedCloudNodes
  azure_rm_vmwarecloudsimplededicatedcloudnode_info: {}
- name: ListRGDedicatedCloudNodes
  azure_rm_vmwarecloudsimplededicatedcloudnode_info:
    resource_group: myResourceGroup
- name: GetDedicatedCloudNode
  azure_rm_vmwarecloudsimplededicatedcloudnode_info:
    resource_group: myResourceGroup
    name: myDedicatedCloudNode

'''

RETURN = '''
dedicated_cloud_nodes:
  description: >-
    A list of dict results where the key is the name of the DedicatedCloudNode
    and the values are the facts for that DedicatedCloudNode.
  returned: always
  type: complex
  contains:
    dedicatedcloudnode_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - >-
              /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName}
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure region
          returned: always
          type: str
          sample: null
        name:
          description:
            - '{dedicatedCloudNodeName}'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Dedicated Cloud Nodes properties
          returned: always
          type: dict
          sample: null
        sku:
          description:
            - Dedicated Cloud Nodes SKU
          returned: always
          type: dict
          sample: null
        tags:
          description:
            - Dedicated Cloud Nodes tags
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"322","$type":"DictionaryType","valueType":{"$id":"323","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"324","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"325","fixed":false},"deprecated":false}]
          sample: null
        type:
          description:
            - '{resourceProviderNamespace}/{resourceType}'
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
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDedicatedCloudNodesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.location = None
        self.name = None
        self.properties = None
        self.sku = None
        self.tags = None
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
        super(AzureRMDedicatedCloudNodesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['dedicated_cloud_nodes'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['dedicated_cloud_nodes'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['dedicated_cloud_nodes'] = [self.format_item(self.listbysubscription())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_nodes.get(resource_group_name=self.resource_group,
                                                                  dedicated_cloud_node_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_nodes.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_cloud_nodes.list_by_subscription()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMDedicatedCloudNodesInfo()


if __name__ == '__main__':
    main()
