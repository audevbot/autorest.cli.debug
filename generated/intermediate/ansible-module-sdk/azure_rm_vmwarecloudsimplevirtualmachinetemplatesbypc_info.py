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
module: azure_rm_vmwarecloudsimplevirtualmachinetemplatesbypc_info
version_added: '2.9'
short_description: Get VirtualMachineTemplatesByPC info.
description:
  - Get info of VirtualMachineTemplatesByPC.
options:
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  name:
    description:
      - Resource pool used to derive vSphere cluster which contains VM templates
    required: true
    type: str
  next_link:
    description:
      - Link for next list of VirtualMachineTemplate
    type: str
  value:
    description:
      - Results of the VM template list
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
              type:
                description:
                  - '{resourceProviderNamespace}/{resourceType}'
                type: str
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListVirtualMachineTemplates
  azure_rm_vmwarecloudsimplevirtualmachinetemplatesbypc_info:
    pc_name: myPrivateCloud
    region_id: myLocation
    name: >-
      /subscriptions/{{ subscription_id
      }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name
      }}/privateClouds/{{ private_cloud_name }}/resourcePools/{{
      resource_pool_name }}

'''

RETURN = '''
virtual_machine_templates_by_pc:
  description: >-
    A list of dict results where the key is the name of the
    VirtualMachineTemplatesByPC and the values are the facts for that
    VirtualMachineTemplatesByPC.
  returned: always
  type: complex
  contains:
    virtualmachinetemplatesbypc_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        next_link:
          description:
            - Link for next list of VirtualMachineTemplate
          returned: always
          type: str
          sample: null
        value:
          description:
            - Results of the VM template list
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
              contains:
                id:
                  description:
                    - Controller's id
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The display name of Controller
                  returned: always
                  type: str
                  sample: null
                sub_type:
                  description:
                    - >-
                      dik controller subtype (VMWARE_PARAVIRTUAL, BUS_PARALLEL,
                      LSI_PARALLEL, LSI_SAS)
                  returned: always
                  type: str
                  sample: null
                type:
                  description:
                    - disk controller type (SCSI)
                  returned: always
                  type: str
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
              contains:
                controller_id:
                  description:
                    - Disk's Controller id
                  returned: always
                  type: str
                  sample: null
                independence_mode:
                  description:
                    - Disk's independence mode type
                  returned: always
                  type: str
                  sample: null
                total_size:
                  description:
                    - Disk's total size
                  returned: always
                  type: number
                  sample: null
                virtual_disk_id:
                  description:
                    - Disk's id
                  returned: always
                  type: str
                  sample: null
                virtual_disk_name:
                  description:
                    - Disk's display name
                  returned: always
                  type: str
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
              contains:
                ip_addresses:
                  description:
                    - NIC ip address
                  returned: always
                  type: str
                  sample: null
                mac_address:
                  description:
                    - NIC MAC address
                  returned: always
                  type: str
                  sample: null
                network:
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
                    type:
                      description:
                        - '{resourceProviderNamespace}/{resourceType}'
                      returned: always
                      type: str
                      sample: null
                nic_type:
                  description:
                    - NIC type
                  returned: always
                  type: str
                  sample: null
                power_on_boot:
                  description:
                    - Is NIC powered on/off on boot
                  returned: always
                  type: boolean
                  sample: null
                virtual_nic_id:
                  description:
                    - NIC id
                  returned: always
                  type: str
                  sample: null
                virtual_nic_name:
                  description:
                    - NIC name
                  returned: always
                  type: str
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


class AzureRMVirtualMachineTemplatesByPCInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            pc_name=dict(
                type='str',
                required=true
            ),
            region_id=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='raw',
                required=true,
                pattern=('//subscriptions/{{ subscription_id }}/providers'
                         '/Microsoft.VMwareCloudSimple/locations/{{ location_name }}'
                         '/privateClouds/{{ private_cloud_name }}/resourcePools/{{ name }}')
            )
        )

        self.pc_name = None
        self.region_id = None
        self.name = None
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
        super(AzureRMVirtualMachineTemplatesByPCInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.pc_name is not None and
            self.region_id is not None and
            self.name is not None):
            self.results['virtual_machine_templates_by_pc'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_templates_by_pc.list(pc_name=self.pc_name,
                                                                             region_id=self.region_id,
                                                                             resource_pool_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMVirtualMachineTemplatesByPCInfo()


if __name__ == '__main__':
    main()
