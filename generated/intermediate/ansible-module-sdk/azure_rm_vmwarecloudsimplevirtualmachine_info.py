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
module: azure_rm_vmwarecloudsimplevirtualmachine_info
version_added: '2.9'
short_description: Get VirtualMachine info.
description:
  - Get info of VirtualMachine.
options:
  resource_group:
    description:
      - The name of the resource group
    type: str
  name:
    description:
      - '{virtualMachineName}'
    type: str
  id:
    description:
      - >-
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName}
    type: str
  location:
    description:
      - Azure region
    type: str
  amount_of_ram:
    description:
      - The amount of memory
    required: true
    type: number
  controllers:
    description:
      - The list of Virtual Disks' Controllers
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
  dnsname:
    description:
      - The DNS name of Virtual Machine in VCenter
    type: str
  expose_to_guest_vm:
    description:
      - Expose Guest OS or not
    type: boolean
  folder:
    description:
      - The path to virtual machine folder in VCenter
    type: str
  guest_os:
    description:
      - The name of Guest OS
    required: true
    type: str
  guest_ostype:
    description:
      - The Guest OS type
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
    required: true
    type: number
  password:
    description:
      - Password for login
    type: str
  private_cloud_id:
    description:
      - Private Cloud Id
    required: true
    type: str
  provisioning_state:
    description:
      - The provisioning status of the resource
    type: str
  public_ip:
    description:
      - The public ip of Virtual Machine
    type: str
  resource_pool:
    description:
      - Virtual Machines Resource Pool
    type: dict
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
  status:
    description:
      - The status of Virtual machine
    type: str
  template_id:
    description:
      - Virtual Machine Template Id
    type: str
  username:
    description:
      - Username for login
    type: str
  v_sphere_networks:
    description:
      - The list of Virtual VSphere Networks
    type: list
  vm_id:
    description:
      - The internal id of Virtual Machine in VCenter
    type: str
  vmwaretools:
    description:
      - VMware tools version
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
- name: ListVirtualMachines
  azure_rm_vmwarecloudsimplevirtualmachine_info: {}
- name: ListRGVirtualMachines
  azure_rm_vmwarecloudsimplevirtualmachine_info:
    resource_group: myResourceGroup
- name: GetVirtualMachine
  azure_rm_vmwarecloudsimplevirtualmachine_info:
    resource_group: myResourceGroup
    name: myVirtualMachine

'''

RETURN = '''
virtual_machine:
  description: >-
    A list of dict results where the key is the name of the VirtualMachine and
    the values are the facts for that VirtualMachine.
  returned: always
  type: complex
  contains:
    virtualmachine_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - >-
              /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName}
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
            - '{virtualMachineName}'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Virtual machine properties
          returned: always
          type: dict
          sample: null
        tags:
          description:
            - The list of tags
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"1315","$type":"DictionaryType","valueType":{"$id":"1316","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"1317","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"1318","fixed":false},"deprecated":false}]
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


class AzureRMVirtualMachineInfo(AzureRMModuleBase):
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
        super(AzureRMVirtualMachineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimpleClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['virtual_machine'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['virtual_machine'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['virtual_machine'] = [self.format_item(self.listbysubscription())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine.get(resource_group_name=self.resource_group,
                                                            virtual_machine_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine.list_by_subscription()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMVirtualMachineInfo()


if __name__ == '__main__':
    main()
