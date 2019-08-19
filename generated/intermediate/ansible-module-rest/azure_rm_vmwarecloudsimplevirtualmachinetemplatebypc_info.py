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
module: azure_rm_vmwarecloudsimplevirtualmachinetemplatebypc_info
version_added: '2.9'
short_description: Get VirtualMachineTemplateByPC info.
description:
  - Get info of VirtualMachineTemplateByPC.
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
    type: str
  pc_name:
    description:
      - The private cloud name
    required: true
    type: str
  name:
    description:
      - '{virtualMachineTemplateName}'
    type: str
  id:
    description:
      - 'virtual machine template id (privateCloudId:vsphereId)'
    type: str
  location:
    description:
      - Azure region
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
          private_cloud_id:
            description:
              - The Private Cloud id
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
- name: GetVirtualMachineTemplate
  azure_rm_vmwarecloudsimplevirtualmachinetemplatebypc_info:
    region_id: myLocation
    pc_name: myPrivateCloud
    name: myVirtualMachineTemplate

'''

RETURN = '''
virtual_machine_template_by_pc:
  description: >-
    A list of dict results where the key is the name of the
    VirtualMachineTemplateByPC and the values are the facts for that
    VirtualMachineTemplateByPC.
  returned: always
  type: complex
  contains:
    virtualmachinetemplatebypc_name:
      description: The key is the name of the server that the values relate to.
      type: complex
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMVirtualMachineTemplateByPCInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                required=true
            ),
            pc_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.region_id = None
        self.pc_name = None
        self.name = None
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
        super(AzureRMVirtualMachineTemplateByPCInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.region_id is not None and
            self.pc_name is not None and
            self.name is not None):
            self.results['virtual_machine_template_by_pc'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.VMwareCloudSimple' +
                    '/locations' +
                    '/{{ location_name }}' +
                    '/privateClouds' +
                    '/{{ private_cloud_name }}' +
                    '/virtualMachineTemplates' +
                    '/{{ virtual_machine_template_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ location_name }}', self.location_name)
        self.url = self.url.replace('{{ private_cloud_name }}', self.private_cloud_name)
        self.url = self.url.replace('{{ virtual_machine_template_name }}', self.name)

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
    AzureRMVirtualMachineTemplateByPCInfo()


if __name__ == '__main__':
    main()
