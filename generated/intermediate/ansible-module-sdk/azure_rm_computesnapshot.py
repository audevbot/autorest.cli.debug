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
module: azure_rm_computesnapshot
version_added: '2.9'
short_description: Manage Azure Snapshot instance.
description:
  - 'Create, update and delete instance of Azure Snapshot.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - Resource name
    type: str
  location:
    description:
      - Resource location
    required: true
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
        Encryption settings collection used be Azure Disk Encryption, can
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
  time_created:
    description:
      - The time when the disk was created.
    type: datetime
  provisioning_state:
    description:
      - The disk provisioning state.
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  managed_by:
    description:
      - Unused. Always Null.
    type: str
  state:
    description:
      - Assert the state of the Snapshot.
      - >-
        Use C(present) to create or update an Snapshot and C(absent) to delete
        it.
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
- name: >-
    Create a snapshot from an existing snapshot in the same or a different
    subscription.
  azure_rm_computesnapshot:
    resource_group: myResourceGroup
    name: mySnapshot
    snapshot:
      name: mySnapshot2
      location: West US
      properties:
        creationData:
          createOption: Copy
          sourceResourceId: >-
            subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot1
- name: Create a snapshot by importing an unmanaged blob from the same subscription.
  azure_rm_computesnapshot:
    resource_group: myResourceGroup
    name: mySnapshot
    snapshot:
      name: mySnapshot1
      location: West US
      properties:
        creationData:
          createOption: Import
          sourceUri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
- name: >-
    Create a snapshot by importing an unmanaged blob from a different
    subscription.
  azure_rm_computesnapshot:
    resource_group: myResourceGroup
    name: mySnapshot
    snapshot:
      name: mySnapshot1
      location: West US
      properties:
        creationData:
          createOption: Import
          storageAccountId: >-
            subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount
          sourceUri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'

'''

RETURN = '''
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
    - Unused. Always Null.
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
properties:
  description:
    - ''
  returned: always
  type: dict
  sample: null
  contains:
    time_created:
      description:
        - The time when the disk was created.
      returned: always
      type: datetime
      sample: null
    os_type:
      description:
        - The Operating System type.
      returned: always
      type: str
      sample: null
    hyper_vgeneration:
      description:
        - >-
          The hypervisor generation of the Virtual Machine. Applicable to OS
          disks only.
      returned: always
      type: str
      sample: null
    creation_data:
      description:
        - >-
          Disk source information. CreationData information cannot be changed
          after the disk has been created.
      returned: always
      type: dict
      sample: null
      contains:
        create_option:
          description:
            - This enumerates the possible sources of a disk's creation.
          returned: always
          type: str
          sample: null
        storage_account_id:
          description:
            - >-
              If createOption is Import, the Azure Resource Manager identifier
              of the storage account containing the blob to import as a disk.
              Required only if the blob is in a different subscription
          returned: always
          type: str
          sample: null
        image_reference:
          description:
            - Disk source information.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - >-
                  A relative uri containing either a Platform Image Repository
                  or user image reference.
              returned: always
              type: str
              sample: null
            lun:
              description:
                - >-
                  If the disk is created from an image's data disk, this is an
                  index that indicates which of the data disks in the image to
                  use. For OS disks, this field is null.
              returned: always
              type: number
              sample: null
        source_uri:
          description:
            - >-
              If createOption is Import, this is the URI of a blob to be
              imported into a managed disk.
          returned: always
          type: str
          sample: null
        source_resource_id:
          description:
            - >-
              If createOption is Copy, this is the ARM id of the source snapshot
              or disk.
          returned: always
          type: str
          sample: null
    disk_size_gb:
      description:
        - >-
          If creationData.createOption is Empty, this field is mandatory and it
          indicates the size of the VHD to create. If this field is present for
          updates or creation with other options, it indicates a resize. Resizes
          are only allowed if the disk is not attached to a running VM, and can
          only increase the disk's size.
      returned: always
      type: number
      sample: null
    encryption_settings_collection:
      description:
        - >-
          Encryption settings collection used be Azure Disk Encryption, can
          contain multiple encryption settings per disk or snapshot.
      returned: always
      type: dict
      sample: null
      contains:
        enabled:
          description:
            - >-
              Set this flag to true and provide DiskEncryptionKey and optional
              KeyEncryptionKey to enable encryption. Set this flag to false and
              remove DiskEncryptionKey and KeyEncryptionKey to disable
              encryption. If EncryptionSettings is null in the request object,
              the existing settings remain unchanged.
          returned: always
          type: boolean
          sample: null
        encryption_settings:
          description:
            - 'A collection of encryption settings, one for each disk volume.'
          returned: always
          type: dict
          sample: null
          contains:
            disk_encryption_key:
              description:
                - Key Vault Secret Url and vault id of the disk encryption key
              returned: always
              type: dict
              sample: null
              contains:
                source_vault:
                  description:
                    - Resource id of the KeyVault containing the key or secret
                  returned: always
                  type: dict
                  sample: null
                secret_url:
                  description:
                    - Url pointing to a key or secret in KeyVault
                  returned: always
                  type: str
                  sample: null
            key_encryption_key:
              description:
                - >-
                  Key Vault Key Url and vault id of the key encryption key.
                  KeyEncryptionKey is optional and when provided is used to
                  unwrap the disk encryption key.
              returned: always
              type: dict
              sample: null
              contains:
                source_vault:
                  description:
                    - Resource id of the KeyVault containing the key or secret
                  returned: always
                  type: dict
                  sample: null
                key_url:
                  description:
                    - Url pointing to a key or secret in KeyVault
                  returned: always
                  type: str
                  sample: null
    provisioning_state:
      description:
        - The disk provisioning state.
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
    from azure.mgmt.compute import DiskResourceProviderClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSnapshots(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='snapshot_name',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            sku=dict(
                type='dict',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str',
                        choices=['Standard_LRS',
                                 'Premium_LRS',
                                 'Standard_ZRS']
                    )
                )
            ),
            os_type=dict(
                type='str',
                disposition='/',
                choices=['Windows',
                         'Linux']
            ),
            hyper_vgeneration=dict(
                type='str',
                disposition='/',
                choices=['V1',
                         'V2']
            ),
            creation_data=dict(
                type='dict',
                disposition='/',
                required=true,
                options=dict(
                    create_option=dict(
                        type='str',
                        choices=['Empty',
                                 'Attach',
                                 'FromImage',
                                 'Import',
                                 'Copy',
                                 'Restore',
                                 'Upload'],
                        required=true
                    ),
                    storage_account_id=dict(
                        type='str'
                    ),
                    image_reference=dict(
                        type='dict',
                        options=dict(
                            id=dict(
                                type='str',
                                required=true
                            ),
                            lun=dict(
                                type='number'
                            )
                        )
                    ),
                    source_uri=dict(
                        type='str'
                    ),
                    source_resource_id=dict(
                        type='str'
                    )
                )
            ),
            disk_size_gb=dict(
                type='number',
                disposition='/'
            ),
            encryption_settings_collection=dict(
                type='dict',
                disposition='/',
                options=dict(
                    enabled=dict(
                        type='boolean',
                        required=true
                    ),
                    encryption_settings=dict(
                        type='list',
                        options=dict(
                            disk_encryption_key=dict(
                                type='dict',
                                options=dict(
                                    source_vault=dict(
                                        type='dict',
                                        required=true
                                    ),
                                    secret_url=dict(
                                        type='str',
                                        required=true
                                    )
                                )
                            ),
                            key_encryption_key=dict(
                                type='dict',
                                options=dict(
                                    source_vault=dict(
                                        type='dict',
                                        required=true
                                    ),
                                    key_url=dict(
                                        type='str',
                                        required=true
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.managed_by = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSnapshots, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DiskResourceProviderClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

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
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["managed_by"] = response["managed_by"]
           self.results["sku"] = response["sku"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.snapshots.create_or_update(resource_group_name=self.resource_group,
                                                                   snapshot_name=self.name,
                                                                   snapshot=self.snapshot)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Snapshot instance.')
            self.fail('Error creating the Snapshot instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Snapshot instance {0}'.format(self.))
        try:
            response = self.mgmt_client.snapshots.delete(resource_group_name=self.resource_group,
                                                         snapshot_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Snapshot instance.')
            self.fail('Error deleting the Snapshot instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Snapshot instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.snapshots.get(resource_group_name=self.resource_group,
                                                      snapshot_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSnapshots()


if __name__ == '__main__':
    main()
