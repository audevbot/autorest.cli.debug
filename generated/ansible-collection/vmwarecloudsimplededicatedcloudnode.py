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
module: vmwarecloudsimplededicatedcloudnode
version_added: '2.9'
short_description: Manage Azure DedicatedCloudNode instance.
description:
  - 'Create, update and delete instance of Azure DedicatedCloudNode.'
options:
  resource_group:
    description:
      - The name of the resource group
    required: true
    type: str
  referer:
    description:
      - referer url
    required: true
    type: str
  dedicated_cloud_node_name:
    description:
      - dedicated cloud node name
    required: true
    type: str
  location:
    description:
      - Azure region
    required: true
    type: str
  availability_zone_id:
    description:
      - 'Availability Zone id, e.g. "az1"'
    required: true
    type: str
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
  id:
    description:
      - >-
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName}
    type: str
  name:
    description:
      - '{dedicatedCloudNodeName}'
    type: str
  type:
    description:
      - '{resourceProviderNamespace}/{resourceType}'
    type: str
  state:
    description:
      - Assert the state of the DedicatedCloudNode.
      - >-
        Use C(present) to create or update an DedicatedCloudNode and C(absent)
        to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: CreateDedicatedCloudNode
  azure.rm.vmwarecloudsimplededicatedcloudnode:
    resource_group: myResourceGroup
    referer: 'https://management.azure.com/'
    dedicated_cloud_node_name: myDedicatedCloudNode
    dedicated_cloud_node_request:
      location: westus
      properties:
        skuDescription:
          id: general
          name: CS28-Node
        placementGroupId: n1
        availabilityZoneId: az1
        nodesCount: '1'
        purchaseId: 56acbd46-3d36-4bbf-9b08-57c30fdf6932
      sku:
        name: VMware_CloudSimple_CS28
- name: PatchDedicatedCloudNode
  azure.rm.vmwarecloudsimplededicatedcloudnode:
    resource_group: myResourceGroup
    referer: 'https://management.azure.com/'
    dedicated_cloud_node_name: myDedicatedCloudNode
    dedicated_cloud_node_request:
      tags:
        myTag: tagValue
- name: DeleteDedicatedCloudNode
  azure.rm.vmwarecloudsimplededicatedcloudnode:
    resource_group: myResourceGroup
    dedicated_cloud_node_name: myDedicatedCloudNode
    state: absent

'''

RETURN = '''
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
  contains:
    availability_zone_id:
      description:
        - 'Availability Zone id, e.g. "az1"'
      returned: always
      type: str
      sample: null
    availability_zone_name:
      description:
        - 'Availability Zone name, e.g. "Availability Zone 1"'
      returned: always
      type: str
      sample: null
    cloud_rack_name:
      description:
        - VMWare Cloud Rack Name
      returned: always
      type: str
      sample: null
    created:
      description:
        - date time the resource was created
      returned: always
      type: 'unknown-primary[object]'
      sample: null
    nodes_count:
      description:
        - count of nodes to create
      returned: always
      type: number
      sample: null
    placement_group_id:
      description:
        - 'Placement Group id, e.g. "n1"'
      returned: always
      type: str
      sample: null
    placement_group_name:
      description:
        - 'Placement Name, e.g. "Placement Group 1"'
      returned: always
      type: str
      sample: null
    private_cloud_id:
      description:
        - Private Cloud Id
      returned: always
      type: str
      sample: null
    private_cloud_name:
      description:
        - Resource Pool Name
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning status of the resource
      returned: always
      type: str
      sample: null
    purchase_id:
      description:
        - purchase id
      returned: always
      type: 'unknown-primary[uuid]'
      sample: null
    sku_description:
      description:
        - Dedicated Cloud Nodes SKU's description
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - SKU's id
          returned: always
          type: str
          sample: null
        name:
          description:
            - SKU's name
          returned: always
          type: str
          sample: null
    status:
      description:
        - 'Node status, indicates is private cloud set up on this node or not'
      returned: always
      type: str
      sample: null
    vmware_cluster_name:
      description:
        - VMWare Cluster Name
      returned: always
      type: str
      sample: null
sku:
  description:
    - Dedicated Cloud Nodes SKU
  returned: always
  type: dict
  sample: null
  contains:
    capacity:
      description:
        - The capacity of the SKU
      returned: always
      type: str
      sample: null
    description:
      description:
        - >-
          dedicatedCloudNode example: 8 x Ten-Core Intel® Xeon® Processor
          E5-2640 v4 2.40GHz 25MB Cache (90W); 12 x 64GB PC4-19200 2400MHz DDR4
          ECC Registered DIMM, ...
      returned: always
      type: str
      sample: null
    family:
      description:
        - >-
          If the service has different generations of hardware, for the same
          SKU, then that can be captured here
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the SKU for VMWare CloudSimple Node
      returned: always
      type: str
      sample: null
    tier:
      description:
        - The tier of the SKU
      returned: always
      type: str
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDedicatedCloudNodes(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            referer=dict(
                type='str',
                updatable=False,
                disposition='Referer',
                required=true
            ),
            dedicated_cloud_node_name=dict(
                type='str',
                updatable=False,
                disposition='dedicatedCloudNodeName',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            availability_zone_id=dict(
                type='str',
                disposition='/properties/availabilityZoneId',
                required=true
            ),
            nodes_count=dict(
                type='number',
                disposition='/properties/nodesCount',
                required=true
            ),
            placement_group_id=dict(
                type='str',
                disposition='/properties/placementGroupId',
                required=true
            ),
            purchase_id=dict(
                type='unknown-primary[uuid]',
                disposition='/properties/purchaseId',
                required=true
            ),
            sku_description=dict(
                type='dict',
                disposition='/properties/skuDescription',
                options=dict(
                    id=dict(
                        type='str',
                        required=true
                    ),
                    name=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            sku_capacity=dict(
                type='str',
                disposition='/sku/capacity'
            ),
            sku_description=dict(
                type='str',
                disposition='/sku/description'
            ),
            sku_family=dict(
                type='str',
                disposition='/sku/family'
            ),
            sku_name=dict(
                type='str',
                disposition='/sku/name',
                required=true
            ),
            sku_tier=dict(
                type='str',
                disposition='/sku/tier'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.referer = None
        self.dedicated_cloud_node_name = None
        self.id = None
        self.name = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMDedicatedCloudNodes, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                         supports_check_mode=True,
                                                         supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.VMwareCloudSimple' +
                    '/dedicatedCloudNodes' +
                    '/{{ dedicated_cloud_node_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ dedicated_cloud_node_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("DedicatedCloudNode instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('DedicatedCloudNode instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the DedicatedCloudNode instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('DedicatedCloudNode instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('DedicatedCloudNode instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["location"] = response["location"]
           self.results["name"] = response["name"]
           self.results["properties"] = response["properties"]
           self.results["sku"] = response["sku"]
           self.results["tags"] = response["tags"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the DedicatedCloudNode instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedCloudNode instance.')
            self.fail('Error creating the DedicatedCloudNode instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the DedicatedCloudNode instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedCloudNode instance.')
            self.fail('Error deleting the DedicatedCloudNode instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the DedicatedCloudNode instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("DedicatedCloudNode instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DedicatedCloudNode instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMDedicatedCloudNodes()


if __name__ == '__main__':
    main()
