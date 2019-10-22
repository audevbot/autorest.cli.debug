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
module: azure_rm_vmwarecloudsimpleprivatecloud
version_added: '2.9'
short_description: Manage Azure PrivateCloud instance.
description:
  - 'Create, update and delete instance of Azure PrivateCloud.'
options:
  region_id:
    description:
      - 'The region Id (westus, eastus)'
    required: true
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
      - Assert the state of the PrivateCloud.
      - >-
        Use C(present) to create or update an PrivateCloud and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
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
[]

'''

RETURN = '''
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


class AzureRMPrivateClouds(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            region_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            availability_zone_id=dict(
                type='str',
                disposition='/'
            ),
            availability_zone_name=dict(
                type='str',
                disposition='/'
            ),
            clusters_number=dict(
                type='number',
                disposition='/'
            ),
            created_by=dict(
                type='str',
                disposition='/'
            ),
            created_on=dict(
                type='datetime',
                disposition='/'
            ),
            dns_servers=dict(
                type='list',
                disposition='/'
            ),
            expires=dict(
                type='str',
                disposition='/'
            ),
            nsx_type=dict(
                type='str',
                disposition='/'
            ),
            placement_group_id=dict(
                type='str',
                disposition='/'
            ),
            placement_group_name=dict(
                type='str',
                disposition='/'
            ),
            private_cloud_id=dict(
                type='unknown-primary[uuid]',
                disposition='/'
            ),
            resource_pools=dict(
                type='list',
                disposition='/',
                options=dict(
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
                    full_name=dict(
                        type='str'
                    ),
                    type=dict(
                        type='str'
                    )
                )
            ),
            state=dict(
                type='str',
                disposition='/'
            ),
            total_cpu_cores=dict(
                type='number',
                disposition='/'
            ),
            total_nodes=dict(
                type='number',
                disposition='/'
            ),
            total_ram=dict(
                type='number',
                disposition='/'
            ),
            total_storage=dict(
                type='number',
                disposition='/'
            ),
            type=dict(
                type='str',
                disposition='/'
            ),
            v_sphere_version=dict(
                type='str',
                disposition='/'
            ),
            vcenter_fqdn=dict(
                type='str',
                disposition='/'
            ),
            vcenter_refid=dict(
                type='str',
                disposition='/'
            ),
            virtual_machine_templates=dict(
                type='list',
                disposition='/',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    location=dict(
                        type='str',
                        updatable=False
                    ),
                    name=dict(
                        type='str'
                    ),
                    amount_of_ram=dict(
                        type='number'
                    ),
                    controllers=dict(
                        type='list',
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
                        type='str'
                    ),
                    disks=dict(
                        type='list',
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
                        type='boolean'
                    ),
                    guest_os=dict(
                        type='str'
                    ),
                    guest_ostype=dict(
                        type='str'
                    ),
                    nics=dict(
                        type='list',
                        options=dict(
                            ip_addresses=dict(
                                type='list'
                            ),
                            mac_address=dict(
                                type='str'
                            ),
                            network=dict(
                                type='dict',
                                required=true
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
                        type='number'
                    ),
                    path=dict(
                        type='str'
                    ),
                    private_cloud_id=dict(
                        type='str',
                        required=true
                    ),
                    v_sphere_networks=dict(
                        type='list'
                    ),
                    v_sphere_tags=dict(
                        type='list'
                    ),
                    vmwaretools=dict(
                        type='str'
                    ),
                    type=dict(
                        type='str'
                    )
                )
            ),
            virtual_networks=dict(
                type='list',
                disposition='/',
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
            vr_ops_enabled=dict(
                type='boolean',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.region_id = None
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

        super(AzureRMPrivateClouds, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.private_clouds.create()
            else:
                response = self.mgmt_client.private_clouds.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PrivateCloud instance.')
            self.fail('Error creating the PrivateCloud instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the PrivateCloud instance {0}'.format(self.))
        try:
            response = self.mgmt_client.private_clouds.delete()
        except CloudError as e:
            self.log('Error attempting to delete the PrivateCloud instance.')
            self.fail('Error deleting the PrivateCloud instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the PrivateCloud instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.private_clouds.get(pc_name=self.pcName,
                                                           region_id=self.region_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPrivateClouds()


if __name__ == '__main__':
    main()
