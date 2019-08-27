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
module: azure_rm_computedisk_info
version_added: '2.9'
short_description: Get Disk info.
description:
  - Get info of Disk.
options:
  resource_group:
    description:
      - The name of the resource group.
    type: str
  name:
    description:
      - Resource name
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  location:
    description:
      - Resource location
    type: str
  managed_by:
    description:
      - A relative URI containing the ID of the VM that has the disk attached.
    type: str
  sku:
    description:
      - undefined
    type: dict
    suboptions:
      name:
        description:
          - The sku name.
        type: str
      tier:
        description:
          - The sku tier.
        type: str
  zones:
    description:
      - The Logical zone list for Disk.
    type: list
  time_created:
    description:
      - The time when the disk was created.
    type: datetime
  os_type:
    description:
      - The Operating System type.
    type: str
  hyper_vgeneration:
    description:
      - >-
        The hypervisor generation of the Virtual Machine. Applicable to OS disks
        only.
    type: str
  creation_data:
    description:
      - >-
        Disk source information. CreationData information cannot be changed
        after the disk has been created.
    required: true
    type: dict
    suboptions:
      create_option:
        description:
          - This enumerates the possible sources of a disk's creation.
        required: true
        type: str
      storage_account_id:
        description:
          - >-
            If createOption is Import, the Azure Resource Manager identifier of
            the storage account containing the blob to import as a disk.
            Required only if the blob is in a different subscription
        type: str
      image_reference:
        description:
          - Disk source information.
        type: dict
        suboptions:
          id:
            description:
              - >-
                A relative uri containing either a Platform Image Repository or
                user image reference.
            required: true
            type: str
          lun:
            description:
              - >-
                If the disk is created from an image's data disk, this is an
                index that indicates which of the data disks in the image to
                use. For OS disks, this field is null.
            type: number
      source_uri:
        description:
          - >-
            If createOption is Import, this is the URI of a blob to be imported
            into a managed disk.
        type: str
      source_resource_id:
        description:
          - >-
            If createOption is Copy, this is the ARM id of the source snapshot
            or disk.
        type: str
  disk_size_gb:
    description:
      - >-
        If creationData.createOption is Empty, this field is mandatory and it
        indicates the size of the VHD to create. If this field is present for
        updates or creation with other options, it indicates a resize. Resizes
        are only allowed if the disk is not attached to a running VM, and can
        only increase the disk's size.
    type: number
  encryption_settings_collection:
    description:
      - >-
        Encryption settings collection used for Azure Disk Encryption, can
        contain multiple encryption settings per disk or snapshot.
    type: dict
    suboptions:
      enabled:
        description:
          - >-
            Set this flag to true and provide DiskEncryptionKey and optional
            KeyEncryptionKey to enable encryption. Set this flag to false and
            remove DiskEncryptionKey and KeyEncryptionKey to disable encryption.
            If EncryptionSettings is null in the request object, the existing
            settings remain unchanged.
        required: true
        type: boolean
      encryption_settings:
        description:
          - 'A collection of encryption settings, one for each disk volume.'
        type: list
        suboptions:
          disk_encryption_key:
            description:
              - Key Vault Secret Url and vault id of the disk encryption key
            type: dict
            suboptions:
              source_vault:
                description:
                  - Resource id of the KeyVault containing the key or secret
                required: true
                type: dict
              secret_url:
                description:
                  - Url pointing to a key or secret in KeyVault
                required: true
                type: str
          key_encryption_key:
            description:
              - >-
                Key Vault Key Url and vault id of the key encryption key.
                KeyEncryptionKey is optional and when provided is used to unwrap
                the disk encryption key.
            type: dict
            suboptions:
              source_vault:
                description:
                  - Resource id of the KeyVault containing the key or secret
                required: true
                type: dict
              key_url:
                description:
                  - Url pointing to a key or secret in KeyVault
                required: true
                type: str
  provisioning_state:
    description:
      - The disk provisioning state.
    type: str
  disk_iopsread_write:
    description:
      - >-
        The number of IOPS allowed for this disk; only settable for UltraSSD
        disks. One operation can transfer between 4k and 256k bytes.
    type: number
  disk_mbps_read_write:
    description:
      - >-
        The bandwidth allowed for this disk; only settable for UltraSSD disks.
        MBps means millions of bytes per second - MB here uses the ISO notation,
        of powers of 10.
    type: number
  disk_state:
    description:
      - The state of the disk.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List all managed disks in a subscription.
  azure_rm_computedisk_info: {}
- name: List all managed disks in a resource group.
  azure_rm_computedisk_info:
    resource_group: myResourceGroup
- name: Get information about a managed disk.
  azure_rm_computedisk_info:
    resource_group: myResourceGroup
    name: myDisk

'''

RETURN = '''
disks:
  description: >-
    A list of dict results where the key is the name of the Disk and the values
    are the facts for that Disk.
  returned: always
  type: complex
  contains:
    disk_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"31","$type":"DictionaryType","valueType":{"$id":"32","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"33","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"34","fixed":false},"deprecated":false}]
          sample: null
        managed_by:
          description:
            - >-
              A relative URI containing the ID of the VM that has the disk
              attached.
          returned: always
          type: str
          sample: null
        sku:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The sku name.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - The sku tier.
              returned: always
              type: str
              sample: null
        zones:
          description:
            - The Logical zone list for Disk.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import DiskResourceProviderClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDisksInfo(AzureRMModuleBase):
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
        self.name = None
        self.type = None
        self.location = None
        self.tags = None
        self.managed_by = None
        self.sku = None
        self.zones = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDisksInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DiskResourceProviderClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['disks'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['disks'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['disks'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.disks.get(resource_group_name=self.resource_group,
                                                  disk_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.disks.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.disks.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMDisksInfo()


if __name__ == '__main__':
    main()
