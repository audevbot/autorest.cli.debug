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
module: azure_rm_vmwarecloudsimplevirtualmachinetemplate
version_added: '2.9'
short_description: Manage Azure VirtualMachineTemplate instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineTemplate.'
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
    type: str
  guest_ostype:
    description:
      - The Guest OS types
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
          - Virtual Network
        required: true
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
  state:
    description:
      - Assert the state of the VirtualMachineTemplate.
      - >-
        Use C(present) to create or update an VirtualMachineTemplate and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
[]

'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualMachineTemplates(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            pc_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            region_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='resource_pool_name',
                required=true
            ),
            amount_of_ram=dict(
                type='number',
                disposition='/'
            ),
            controllers=dict(
                type='list',
                disposition='/',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    name=dict(
                        type='str'
                    ),
                    sub_type=dict(
                        type='str'
                    ),
                    type=dict(
                        type='str'
                    )
                )
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            disks=dict(
                type='list',
                disposition='/',
                options=dict(
                    controller_id=dict(
                        type='str',
                        required=true
                    ),
                    independence_mode=dict(
                        type='str',
                        choices=['persistent',
                                 'independent_persistent',
                                 'independent_nonpersistent'],
                        required=true
                    ),
                    total_size=dict(
                        type='number',
                        required=true
                    ),
                    virtual_disk_id=dict(
                        type='str'
                    ),
                    virtual_disk_name=dict(
                        type='str'
                    )
                )
            ),
            expose_to_guest_vm=dict(
                type='boolean',
                disposition='/'
            ),
            guest_os=dict(
                type='str',
                disposition='/'
            ),
            guest_ostype=dict(
                type='str',
                disposition='/'
            ),
            nics=dict(
                type='list',
                disposition='/',
                options=dict(
                    ip_addresses=dict(
                        type='list'
                    ),
                    mac_address=dict(
                        type='str'
                    ),
                    network=dict(
                        type='dict',
                        required=true,
                        options=dict(
                            assignable=dict(
                                type='boolean'
                            ),
                            id=dict(
                                type='str',
                                required=true
                            ),
                            location=dict(
                                type='str',
                                updatable=False
                            ),
                            name=dict(
                                type='str'
                            ),
                            private_cloud_id=dict(
                                type='str'
                            ),
                            type=dict(
                                type='str'
                            )
                        )
                    ),
                    nic_type=dict(
                        type='str',
                        choices=['E1000',
                                 'E1000E',
                                 'PCNET32',
                                 'VMXNET',
                                 'VMXNET2',
                                 'VMXNET3'],
                        required=true
                    ),
                    power_on_boot=dict(
                        type='boolean'
                    ),
                    virtual_nic_id=dict(
                        type='str'
                    ),
                    virtual_nic_name=dict(
                        type='str'
                    )
                )
            ),
            number_of_cores=dict(
                type='number',
                disposition='/'
            ),
            path=dict(
                type='str',
                disposition='/'
            ),
            private_cloud_id=dict(
                type='str',
                disposition='/',
                required=true
            ),
            v_sphere_networks=dict(
                type='list',
                disposition='/'
            ),
            v_sphere_tags=dict(
                type='list',
                disposition='/'
            ),
            vmwaretools=dict(
                type='str',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.pc_name = None
        self.region_id = None
        self.name = None
        self.id = None
        self.location = None
        self.name = None
        self.properties = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineTemplates, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if self.location is None:
            self.location = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["location"] = response["location"]
           self.results["name"] = response["name"]
           self.results["properties"] = response["properties"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.virtual_machine_templates.create()
            else:
                response = self.mgmt_client.virtual_machine_templates.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineTemplate instance.')
            self.fail('Error creating the VirtualMachineTemplate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the VirtualMachineTemplate instance {0}'.format(self.))
        try:
            response = self.mgmt_client.virtual_machine_templates.delete()
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineTemplate instance.')
            self.fail('Error deleting the VirtualMachineTemplate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the VirtualMachineTemplate instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.virtual_machine_templates.get(region_id=self.region_id,
                                                                      pc_name=self.pc_name,
                                                                      virtual_machine_template_name=self.virtualMachineTemplateName)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineTemplates()


if __name__ == '__main__':
    main()
