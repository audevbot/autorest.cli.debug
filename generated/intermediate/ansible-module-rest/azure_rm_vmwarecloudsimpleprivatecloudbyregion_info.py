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
module: azure_rm_vmwarecloudsimpleprivatecloudbyregion_info
version_added: '2.9'
short_description: Get PrivateCloudByRegion info.
description:
  - Get info of PrivateCloudByRegion.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  next_link:
    description:
      - Link for next list of Private Clouds
    type: str
  value:
    description:
      - the list of private clouds
    type: list
    suboptions:
      id:
        description:
          - >-
            Azure Id, e.g.
            "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123"
        type: str
      location:
        description:
          - 'Location where private cloud created, e.g "westus"'
        type: str
      name:
        description:
          - Private cloud name
        type: str
      availability_zone_id:
        description:
          - 'Availability Zone id, e.g. "az1"'
        type: str
      availability_zone_name:
        description:
          - 'Availability Zone name, e.g. "Availability Zone 1"'
        type: str
      clusters_number:
        description:
          - Number of clusters
        type: number
      created_by:
        description:
          - User's emails who created cloud
        type: str
      created_on:
        description:
          - When private cloud was created
        type: datetime
      dns_servers:
        description:
          - Array of DNS servers
        type: list
      expires:
        description:
          - Expiration date of PC
        type: str
      nsx_type:
        description:
          - 'Nsx Type, e.g. "Advanced"'
        type: str
      placement_group_id:
        description:
          - 'Placement Group id, e.g. "n1"'
        type: str
      placement_group_name:
        description:
          - Placement Group name
        type: str
      private_cloud_id:
        description:
          - Id of a private cloud
        type: 'unknown-primary[uuid]'
      resource_pools:
        description:
          - The list of Resource Pools
        type: list
        suboptions:
          id:
            description:
              - 'resource pool id (privateCloudId:vsphereId)'
            required: true
            type: str
          location:
            description:
              - Azure region
            type: str
          name:
            description:
              - '{ResourcePoolName}'
            type: str
          private_cloud_id:
            description:
              - The Private Cloud Id
            type: str
          full_name:
            description:
              - Hierarchical resource pool name
            type: str
          type:
            description:
              - '{resourceProviderNamespace}/{resourceType}'
            type: str
      state:
        description:
          - 'Private Cloud state, e.g. "operational"'
        type: str
      total_cpu_cores:
        description:
          - Number of cores
        type: number
      total_nodes:
        description:
          - Number of nodes
        type: number
      total_ram:
        description:
          - Memory size
        type: number
      total_storage:
        description:
          - Disk space in TB
        type: number
      type:
        description:
          - Azure Resource type
        type: str
      v_sphere_version:
        description:
          - e.g. "6.5u2"
        type: str
      vcenter_fqdn:
        description:
          - FQDN for vcenter access
        type: str
      vcenter_refid:
        description:
          - Vcenter ip address
        type: str
      virtual_machine_templates:
        description:
          - The list of Virtual Machine Templates
        type: list
        suboptions:
          id:
            description:
              - 'virtual machine template id (privateCloudId:vsphereId)'
            type: str
          location:
            description:
              - Azure region
            type: str
          name:
            description:
              - '{virtualMachineTemplateName}'
            type: str
          amount_of_ram:
            description:
              - The amount of memory
            type: number
          controllers:
            description:
              - The list of Virtual Disk Controllers
            type: list
          description:
            description:
              - The description of Virtual Machine Template
            type: str
          disks:
            description:
              - The list of Virtual Disks
            type: list
          expose_to_guest_vm:
            description:
              - Expose Guest OS or not
            type: boolean
          guest_os:
            description:
              - The Guest OS
            required: true
            type: str
          guest_ostype:
            description:
              - The Guest OS types
            required: true
            type: str
          nics:
            description:
              - The list of Virtual NICs
            type: list
          number_of_cores:
            description:
              - The number of CPU cores
            type: number
          path:
            description:
              - path to folder
            type: str
          private_cloud_id:
            description:
              - The Private Cloud Id
            required: true
            type: str
          v_sphere_networks:
            description:
              - The list of VSphere networks
            type: list
          v_sphere_tags:
            description:
              - The tags from VSphere
            type: list
          vmwaretools:
            description:
              - The VMware tools version
            type: str
          type:
            description:
              - '{resourceProviderNamespace}/{resourceType}'
            type: str
      virtual_networks:
        description:
          - The list of Virtual Networks
        type: list
        suboptions:
          assignable:
            description:
              - can be used in vm creation/deletion
            type: boolean
          id:
            description:
              - 'virtual network id (privateCloudId:vsphereId)'
            required: true
            type: str
          location:
            description:
              - Azure region
            type: str
          name:
            description:
              - '{VirtualNetworkName}'
            type: str
          private_cloud_id:
            description:
              - The Private Cloud id
            type: str
          type:
            description:
              - '{resourceProviderNamespace}/{resourceType}'
            type: str
      vr_ops_enabled:
        description:
          - Is Vrops enabled/disabled
        type: boolean
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListPrivateCloudInLocation
  azure_rm_vmwarecloudsimpleprivatecloudbyregion_info:
    region_id: myLocation

'''

RETURN = '''
private_cloud_by_region:
  description: >-
    A list of dict results where the key is the name of the PrivateCloudByRegion
    and the values are the facts for that PrivateCloudByRegion.
  returned: always
  type: complex
  contains:
    privatecloudbyregion_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - Link for next list of Private Clouds
          returned: always
          type: str
          sample: null
        value:
          description:
            - the list of private clouds
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - >-
                  Azure Id, e.g.
                  "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123"
              returned: always
              type: str
              sample: null
            location:
              description:
                - 'Location where private cloud created, e.g "westus"'
              returned: always
              type: str
              sample: null
            name:
              description:
                - Private cloud name
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Private cloud properties
              returned: always
              type: dict
              sample: null
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
            clusters_number:
              description:
                - Number of clusters
              returned: always
              type: number
              sample: null
            created_by:
              description:
                - User's emails who created cloud
              returned: always
              type: str
              sample: null
            created_on:
              description:
                - When private cloud was created
              returned: always
              type: datetime
              sample: null
            dns_servers:
              description:
                - Array of DNS servers
              returned: always
              type: str
              sample: null
            expires:
              description:
                - Expiration date of PC
              returned: always
              type: str
              sample: null
            nsx_type:
              description:
                - 'Nsx Type, e.g. "Advanced"'
              returned: always
              type: str
              sample: null
            placement_group_id:
              description:
                - 'Placement Group id, e.g. "n1"'
              returned: always
              type: str
              sample: null
            placement_group_name:
              description:
                - Placement Group name
              returned: always
              type: str
              sample: null
            private_cloud_id:
              description:
                - Id of a private cloud
              returned: always
              type: 'unknown-primary[uuid]'
              sample: null
            resource_pools:
              description:
                - The list of Resource Pools
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - 'resource pool id (privateCloudId:vsphereId)'
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
                    - '{ResourcePoolName}'
                  returned: always
                  type: str
                  sample: null
                private_cloud_id:
                  description:
                    - The Private Cloud Id
                  returned: always
                  type: str
                  sample: null
                properties:
                  description:
                    - Resource pool properties
                  returned: always
                  type: dict
                  sample: null
                full_name:
                  description:
                    - Hierarchical resource pool name
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - '{resourceProviderNamespace}/{resourceType}'
                  returned: always
                  type: str
                  sample: null
            state:
              description:
                - 'Private Cloud state, e.g. "operational"'
              returned: always
              type: str
              sample: null
            total_cpu_cores:
              description:
                - Number of cores
              returned: always
              type: number
              sample: null
            total_nodes:
              description:
                - Number of nodes
              returned: always
              type: number
              sample: null
            total_ram:
              description:
                - Memory size
              returned: always
              type: number
              sample: null
            total_storage:
              description:
                - Disk space in TB
              returned: always
              type: number
              sample: null
            type:
              description:
                - Azure Resource type
              returned: always
              type: str
              sample: null
            v_sphere_version:
              description:
                - e.g. "6.5u2"
              returned: always
              type: str
              sample: null
            vcenter_fqdn:
              description:
                - FQDN for vcenter access
              returned: always
              type: str
              sample: null
            vcenter_refid:
              description:
                - Vcenter ip address
              returned: always
              type: str
              sample: null
            virtual_machine_templates:
              description:
                - The list of Virtual Machine Templates
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - 'virtual machine template id (privateCloudId:vsphereId)'
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
                    - '{virtualMachineTemplateName}'
                  returned: always
                  type: str
                  sample: null
                properties:
                  description:
                    - The Virtual Machine Template properties
                  returned: always
                  type: dict
                  sample: null
                amount_of_ram:
                  description:
                    - The amount of memory
                  returned: always
                  type: number
                  sample: null
                controllers:
                  description:
                    - The list of Virtual Disk Controllers
                  returned: always
                  type: dict
                  sample: null
                description:
                  description:
                    - The description of Virtual Machine Template
                  returned: always
                  type: str
                  sample: null
                disks:
                  description:
                    - The list of Virtual Disks
                  returned: always
                  type: dict
                  sample: null
                expose_to_guest_vm:
                  description:
                    - Expose Guest OS or not
                  returned: always
                  type: boolean
                  sample: null
                guest_os:
                  description:
                    - The Guest OS
                  returned: always
                  type: str
                  sample: null
                guest_ostype:
                  description:
                    - The Guest OS types
                  returned: always
                  type: str
                  sample: null
                nics:
                  description:
                    - The list of Virtual NICs
                  returned: always
                  type: dict
                  sample: null
                number_of_cores:
                  description:
                    - The number of CPU cores
                  returned: always
                  type: number
                  sample: null
                path:
                  description:
                    - path to folder
                  returned: always
                  type: str
                  sample: null
                private_cloud_id:
                  description:
                    - The Private Cloud Id
                  returned: always
                  type: str
                  sample: null
                v_sphere_networks:
                  description:
                    - The list of VSphere networks
                  returned: always
                  type: str
                  sample: null
                v_sphere_tags:
                  description:
                    - The tags from VSphere
                  returned: always
                  type: str
                  sample: null
                vmwaretools:
                  description:
                    - The VMware tools version
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - '{resourceProviderNamespace}/{resourceType}'
                  returned: always
                  type: str
                  sample: null
            virtual_networks:
              description:
                - The list of Virtual Networks
              returned: always
              type: dict
              sample: null
              contains:
                assignable:
                  description:
                    - can be used in vm creation/deletion
                  returned: always
                  type: boolean
                  sample: null
                id:
                  description:
                    - 'virtual network id (privateCloudId:vsphereId)'
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
                    - '{VirtualNetworkName}'
                  returned: always
                  type: str
                  sample: null
                properties:
                  description:
                    - Virtual Network properties
                  returned: always
                  type: dict
                  sample: null
                private_cloud_id:
                  description:
                    - The Private Cloud id
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - '{resourceProviderNamespace}/{resourceType}'
                  returned: always
                  type: str
                  sample: null
            vr_ops_enabled:
              description:
                - Is Vrops enabled/disabled
              returned: always
              type: boolean
              sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMPrivateCloudByRegionInfo(AzureRMModuleBase):
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
        super(AzureRMPrivateCloudByRegionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None):
            self.results['private_cloud_by_region'] = self.format_item(self.list())
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
                    '/privateClouds')
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
    AzureRMPrivateCloudByRegionInfo()


if __name__ == '__main__':
    main()
