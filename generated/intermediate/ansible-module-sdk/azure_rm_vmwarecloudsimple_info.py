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
module: azure_rm_vmwarecloudsimple_info
version_added: '2.9'
short_description: Get  info.
description:
  - Get info of .
options:
  pc_name:
    description:
      - The private cloud name
    type: str
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  referer:
    description:
      - referer url
    type: str
  operation_id:
    description:
      - operation id
    type: str
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
        suboptions:
          id:
            description:
              - Controller's id
            type: str
          name:
            description:
              - The display name of Controller
            type: str
          sub_type:
            description:
              - >-
                dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALLEL,
                LSI_PARALLEL, LSI_SAS)
            type: str
          type:
            description:
              - disk controller type (SCSI)
            type: str
      description:
        description:
          - The description of Virtual Machine Template
        type: str
      disks:
        description:
          - The list of Virtual Disks
        type: list
        suboptions:
          controller_id:
            description:
              - Disk's Controller id
            required: true
            type: str
          independence_mode:
            description:
              - Disk's independence mode type
            required: true
            type: str
          total_size:
            description:
              - Disk's total size
            required: true
            type: number
          virtual_disk_id:
            description:
              - Disk's id
            type: str
          virtual_disk_name:
            description:
              - Disk's display name
            type: str
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
        suboptions:
          ip_addresses:
            description:
              - NIC ip address
            type: list
          mac_address:
            description:
              - NIC MAC address
            type: str
          network:
            description:
              - The list of Virtual Networks
            type: dict
          nic_type:
            description:
              - NIC type
            required: true
            type: str
          power_on_boot:
            description:
              - Is NIC powered on/off on boot
            type: boolean
          virtual_nic_id:
            description:
              - NIC id
            type: str
          virtual_nic_name:
            description:
              - NIC name
            type: str
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
- name: GetPrivateCloud
  azure_rm_vmwarecloudsimple_info:
    pc_name: myPrivateCloud
    region_id: myLocation
- name: GetFailedOperationResult
  azure_rm_vmwarecloudsimple_info:
    region_id: myLocation
    referer: 'https://management.azure.com/'
    operation_id: myOperationResult
- name: GetOperationResult
  azure_rm_vmwarecloudsimple_info:
    region_id: myLocation
    referer: 'https://management.azure.com/'
    operation_id: myOperationResult

'''

RETURN = '''
'':
  description: >-
    A list of dict results where the key is the name of the  and the values are
    the facts for that .
  returned: always
  type: complex
  contains:
    _name:
      description: The key is the name of the server that the values relate to.
      type: complex
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
        type:
          description:
            - Azure Resource type
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


class AzureRMInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            pc_name=dict(
                type='str'
            ),
            region_id=dict(
                type='str',
                required=true
            ),
            referer=dict(
                type='str'
            ),
            operation_id=dict(
                type='str'
            )
        )

        self.pc_name = None
        self.region_id = None
        self.referer = None
        self.operation_id = None
        self.id = None
        self.location = None
        self.name = None
        self.properties = None
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
        super(AzureRMInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.referer is not None and
            self.operation_id is not None):
            self.results[''] = self.format_item(self.getoperationresultbyregion())
        elif (self.pc_name is not None and
              self.region_id is not None):
            self.results[''] = self.format_item(self.getprivatecloud())
        return self.results

    def getoperationresultbyregion(self):
        response = None

        try:
            response = self.mgmt_client..get_operation_result_by_region(region_id=self.region_id,
                                                                        referer=self.referer,
                                                                        operation_id=self.operation_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def getprivatecloud(self):
        response = None

        try:
            response = self.mgmt_client..get_private_cloud(pc_name=self.pc_name,
                                                           region_id=self.region_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMInfo()


if __name__ == '__main__':
    main()
