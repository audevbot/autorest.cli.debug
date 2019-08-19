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
module: azure_rm_vmwarecloudsimplevirtualmachine
version_added: '2.9'
short_description: Manage Azure VirtualMachine instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachine.'
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
  name:
    description:
      - '{virtualMachineName}'
    type: str
  location:
    description:
      - Azure region
    required: true
    type: str
  amount_of_ram:
    description:
      - The amount of memory
    required: true
    type: number
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
          id:
            description:
              - 'virtual network id (privateCloudId:vsphereId)'
            required: true
            type: str
          location:
            description:
              - Azure region
            type: str
          private_cloud_id:
            description:
              - The Private Cloud id
            type: str
          assignable:
            description:
              - can be used in vm creation/deletion
            type: boolean
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
      full_name:
        description:
          - Hierarchical resource pool name
        type: str
      name:
        description:
          - '{ResourcePoolName}'
        type: str
      private_cloud_id:
        description:
          - The Private Cloud Id
        type: str
      type:
        description:
          - '{resourceProviderNamespace}/{resourceType}'
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
  dnsname:
    description:
      - The DNS name of Virtual Machine in VCenter
    type: str
  folder:
    description:
      - The path to virtual machine folder in VCenter
    type: str
  provisioning_state:
    description:
      - The provisioning status of the resource
    type: str
  public_ip:
    description:
      - The public ip of Virtual Machine
    type: str
  status:
    description:
      - The status of Virtual machine
    type: str
  vm_id:
    description:
      - The internal id of Virtual Machine in VCenter
    type: str
  vmwaretools:
    description:
      - VMware tools version
    type: str
  id:
    description:
      - >-
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/virtualMachines/{virtualMachineName}
    type: str
  type:
    description:
      - '{resourceProviderNamespace}/{resourceType}'
    type: str
  state:
    description:
      - Assert the state of the VirtualMachine.
      - >-
        Use C(present) to create or update an VirtualMachine and C(absent) to
        delete it.
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
- name: CreateVirtualMachine
  azure_rm_vmwarecloudsimplevirtualmachine:
    resource_group: myResourceGroup
    referer: 'https://management.azure.com/'
    name: myVirtualMachine
    virtual_machine_request:
      location: westus2
      properties:
        privateCloudId: >-
          /subscriptions/{{ subscription_id
          }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name
          }}/privateClouds/{{ private_cloud_name }}
        templateId: >-
          /subscriptions/{{ subscription_id
          }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name
          }}/privateClouds/{{ private_cloud_name }}/virtualMachineTemplates/{{
          virtual_machine_template_name }}
        numberOfCores: '2'
        amountOfRam: '4096'
        disks:
          - controllerId: '1000'
            independenceMode: persistent
            totalSize: '10485760'
            virtualDiskId: '2000'
        resourcePool:
          id: >-
            /subscriptions/{{ subscription_id
            }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name
            }}/privateClouds/{{ private_cloud_name }}/resourcePools/{{
            resource_pool_name }}
        guestOS: Other (32-bit)
        guestOSType: other
        nics:
          - network:
              id: >-
                /subscriptions/{{ subscription_id
                }}/providers/Microsoft.VMwareCloudSimple/locations/{{
                location_name }}/privateClouds/{{ private_cloud_name
                }}/virtualNetworks/{{ virtual_network_name }}
            nicType: E1000
            powerOnBoot: true
            virtualNicId: '4000'
- name: PatchVirtualMachine
  azure_rm_vmwarecloudsimplevirtualmachine:
    resource_group: myResourceGroup
    name: myVirtualMachine
    virtual_machine_request:
      tags:
        myTag: tagValue
- name: DeleteVirtualMachine
  azure_rm_vmwarecloudsimplevirtualmachine:
    resource_group: myResourceGroup
    referer: 'https://management.azure.com/'
    name: myVirtualMachine
    state: absent

'''

RETURN = '''
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
  contains:
    amount_of_ram:
      description:
        - The amount of memory
      returned: always
      type: number
      sample: null
    controllers:
      description:
        - The list of Virtual Disks' Controllers
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
    dnsname:
      description:
        - The DNS name of Virtual Machine in VCenter
      returned: always
      type: str
      sample: null
    expose_to_guest_vm:
      description:
        - Expose Guest OS or not
      returned: always
      type: boolean
      sample: null
    folder:
      description:
        - The path to virtual machine folder in VCenter
      returned: always
      type: str
      sample: null
    guest_os:
      description:
        - The name of Guest OS
      returned: always
      type: str
      sample: null
    guest_ostype:
      description:
        - The Guest OS type
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
              contains:
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
    password:
      description:
        - Password for login
      returned: always
      type: str
      sample: null
    private_cloud_id:
      description:
        - Private Cloud Id
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning status of the resource
      returned: always
      type: str
      sample: null
    public_ip:
      description:
        - The public ip of Virtual Machine
      returned: always
      type: str
      sample: null
    resource_pool:
      description:
        - Virtual Machines Resource Pool
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
          contains:
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
    status:
      description:
        - The status of Virtual machine
      returned: always
      type: str
      sample: null
    template_id:
      description:
        - Virtual Machine Template Id
      returned: always
      type: str
      sample: null
    username:
      description:
        - Username for login
      returned: always
      type: str
      sample: null
    v_sphere_networks:
      description:
        - The list of Virtual VSphere Networks
      returned: always
      type: str
      sample: null
    vm_id:
      description:
        - The internal id of Virtual Machine in VCenter
      returned: always
      type: str
      sample: null
    vmwaretools:
      description:
        - VMware tools version
      returned: always
      type: str
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


class AzureRMVirtualMachine(AzureRMModuleBaseExt):
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
            name=dict(
                type='str',
                updatable=False,
                disposition='virtualMachineName',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            amount_of_ram=dict(
                type='number',
                disposition='/properties/amountOfRam',
                required=true
            ),
            disks=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    controller_id=dict(
                        type='str',
                        disposition='controllerId',
                        required=true
                    ),
                    independence_mode=dict(
                        type='str',
                        disposition='independenceMode',
                        choices=['persistent',
                                 'independent_persistent',
                                 'independent_nonpersistent'],
                        required=true
                    ),
                    total_size=dict(
                        type='number',
                        disposition='totalSize',
                        required=true
                    ),
                    virtual_disk_id=dict(
                        type='str',
                        disposition='virtualDiskId'
                    )
                )
            ),
            expose_to_guest_vm=dict(
                type='boolean',
                disposition='/properties/exposeToGuestVM'
            ),
            guest_os=dict(
                type='str',
                disposition='/properties/guestOS',
                required=true
            ),
            guest_ostype=dict(
                type='str',
                disposition='/properties/guestOSType',
                choices=['linux',
                         'windows',
                         'other'],
                required=true
            ),
            nics=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    ip_addresses=dict(
                        type='list',
                        disposition='ipAddresses'
                    ),
                    mac_address=dict(
                        type='str',
                        disposition='macAddress'
                    ),
                    network=dict(
                        type='dict',
                        options=dict(
                            id=dict(
                                type='str',
                                required=true
                            ),
                            location=dict(
                                type='str',
                                updatable=False
                            )
                        )
                    ),
                    nic_type=dict(
                        type='str',
                        disposition='nicType',
                        choices=['E1000',
                                 'E1000E',
                                 'PCNET32',
                                 'VMXNET',
                                 'VMXNET2',
                                 'VMXNET3'],
                        required=true
                    ),
                    power_on_boot=dict(
                        type='boolean',
                        disposition='powerOnBoot'
                    ),
                    virtual_nic_id=dict(
                        type='str',
                        disposition='virtualNicId'
                    )
                )
            ),
            number_of_cores=dict(
                type='number',
                disposition='/properties/numberOfCores',
                required=true
            ),
            password=dict(
                type='str',
                no_log=True,
                disposition='/properties/*'
            ),
            private_cloud_id=dict(
                type='str',
                disposition='/properties/privateCloudId',
                required=true
            ),
            resource_pool=dict(
                type='dict',
                disposition='/properties/resourcePool',
                options=dict(
                    id=dict(
                        type='str',
                        required=true
                    ),
                    location=dict(
                        type='str',
                        updatable=False
                    )
                )
            ),
            template_id=dict(
                type='str',
                disposition='/properties/templateId'
            ),
            username=dict(
                type='str',
                disposition='/properties/*'
            ),
            v_sphere_networks=dict(
                type='list',
                disposition='/properties/vSphereNetworks'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.referer = None
        self.name = None
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

        super(AzureRMVirtualMachine, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/virtualMachines' +
                    '/{{ virtual_machine_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ virtual_machine_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("VirtualMachine instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('VirtualMachine instance already exists')

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
            self.log('Need to Create / Update the VirtualMachine instance')

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
            self.log('VirtualMachine instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('VirtualMachine instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["location"] = response["location"]
           self.results["name"] = response["name"]
           self.results["properties"] = response["properties"]
           self.results["tags"] = response["tags"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the VirtualMachine instance {0}'.format(self.))

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
            self.log('Error attempting to create the VirtualMachine instance.')
            self.fail('Error creating the VirtualMachine instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the VirtualMachine instance {0}'.format(self.))
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
            self.log('Error attempting to delete the VirtualMachine instance.')
            self.fail('Error deleting the VirtualMachine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the VirtualMachine instance {0} is present'.format(self.))
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
            # self.log("VirtualMachine instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the VirtualMachine instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMVirtualMachine()


if __name__ == '__main__':
    main()
