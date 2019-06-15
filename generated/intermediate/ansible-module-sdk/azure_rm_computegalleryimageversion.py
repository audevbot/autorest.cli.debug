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
module: azure_rm_computegalleryimageversion
version_added: '2.9'
short_description: Manage Azure GalleryImageVersion instance.
description:
  - 'Create, update and delete instance of Azure GalleryImageVersion.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  gallery_name:
    description:
      - >-
        The name of the Shared Image Gallery in which the Image Definition
        resides.
    required: true
  gallery_image_name:
    description:
      - >-
        The name of the gallery Image Definition in which the Image Version is
        to be created.
    required: true
  name:
    description:
      - Resource name
  location:
    description:
      - Resource location
    required: true
  publishing_profile:
    description:
      - undefined
    required: true
    suboptions:
      target_regions:
        description:
          - >-
            The target regions where the Image Version is going to be replicated
            to. This property is updatable.
        type: list
        suboptions:
          name:
            description:
              - The name of the region.
            required: true
          regional_replica_count:
            description:
              - >-
                The number of replicas of the Image Version to be created per
                region. This property is updatable.
          storage_account_type:
            description:
              - >-
                Specifies the storage account type to be used to store the
                image. This property is not updatable.
      source:
        description:
          - undefined
        required: true
        suboptions:
          managed_image:
            description:
              - undefined
            required: true
            suboptions:
              id:
                description:
                  - The managed artifact id.
                required: true
      replica_count:
        description:
          - >-
            The number of replicas of the Image Version to be created per
            region. This property would take effect for a region when
            regionalReplicaCount is not specified. This property is updatable.
      exclude_from_latest:
        description:
          - >-
            If set to true, Virtual Machines deployed from the latest version of
            the Image Definition won't use this Image Version.
      end_of_life_date:
        description:
          - >-
            The end of life date of the gallery Image Version. This property can
            be used for decommissioning purposes. This property is updatable.
      storage_account_type:
        description:
          - >-
            Specifies the storage account type to be used to store the image.
            This property is not updatable.
      published_date:
        description:
          - The timestamp for when the gallery Image Version is published.
  provisioning_state:
    description:
      - 'The provisioning state, which only appears in the response.'
  storage_profile:
    description:
      - undefined
    suboptions:
      os_disk_image:
        description:
          - undefined
        suboptions:
          size_in_gb:
            description:
              - This property indicates the size of the VHD to be created.
          host_caching:
            description:
              - >-
                The host caching of the disk. Valid values are 'None',
                'ReadOnly', and 'ReadWrite'
      data_disk_images:
        description:
          - A list of data disk images.
        type: list
        suboptions:
          size_in_gb:
            description:
              - This property indicates the size of the VHD to be created.
          host_caching:
            description:
              - >-
                The host caching of the disk. Valid values are 'None',
                'ReadOnly', and 'ReadWrite'
          lun:
            description:
              - >-
                This property specifies the logical unit number of the data
                disk. This value is used to identify data disks within the
                Virtual Machine and therefore must be unique for each data disk
                attached to the Virtual Machine.
  replication_status:
    description:
      - undefined
    suboptions:
      aggregated_state:
        description:
          - >-
            This is the aggregated replication status based on all the regional
            replication status flags.
      summary:
        description:
          - This is a summary of replication status for each region.
        type: list
        suboptions:
          region:
            description:
              - >-
                The region to which the gallery Image Version is being
                replicated to.
          state:
            description:
              - This is the regional replication state.
          details:
            description:
              - The details of the replication status.
          progress:
            description:
              - It indicates progress of the replication job.
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  state:
    description:
      - Assert the state of the GalleryImageVersion.
      - >-
        Use C(present) to create or update an GalleryImageVersion and C(absent)
        to delete it.
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
- name: Create or update a simple gallery Image Version.
  azure_rm_computegalleryimageversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
    name: myVersion
    gallery_image_version:
      location: West US
      properties:
        publishingProfile:
          targetRegions:
            - name: West US
              regionalReplicaCount: '1'
            - name: East US
              regionalReplicaCount: '2'
              storageAccountType: Standard_ZRS
          source:
            managedImage:
              id: >-
                /subscriptions/{{ subscription_id }}/resourceGroups/{{
                resource_group }}/providers/Microsoft.Compute/images/{{
                image_name }}
- name: Delete a gallery Image Version.
  azure_rm_computegalleryimageversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
    name: myVersion
    state: absent

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
    {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - !<tag:yaml.org,2002:js/undefined> ''
  returned: always
  type: dict
  sample: null
  contains:
    publishing_profile:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        target_regions:
          description:
            - >-
              The target regions where the Image Version is going to be
              replicated to. This property is updatable.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The name of the region.
              returned: always
              type: str
              sample: null
            regional_replica_count:
              description:
                - >-
                  The number of replicas of the Image Version to be created per
                  region. This property is updatable.
              returned: always
              type: number
              sample: null
            storage_account_type:
              description:
                - >-
                  Specifies the storage account type to be used to store the
                  image. This property is not updatable.
              returned: always
              type: str
              sample: null
        source:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: dict
          sample: null
          contains:
            managed_image:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - The managed artifact id.
                  returned: always
                  type: str
                  sample: null
        replica_count:
          description:
            - >-
              The number of replicas of the Image Version to be created per
              region. This property would take effect for a region when
              regionalReplicaCount is not specified. This property is updatable.
          returned: always
          type: number
          sample: null
        exclude_from_latest:
          description:
            - >-
              If set to true, Virtual Machines deployed from the latest version
              of the Image Definition won't use this Image Version.
          returned: always
          type: boolean
          sample: null
        published_date:
          description:
            - The timestamp for when the gallery Image Version is published.
          returned: always
          type: datetime
          sample: null
        end_of_life_date:
          description:
            - >-
              The end of life date of the gallery Image Version. This property
              can be used for decommissioning purposes. This property is
              updatable.
          returned: always
          type: datetime
          sample: null
        storage_account_type:
          description:
            - >-
              Specifies the storage account type to be used to store the image.
              This property is not updatable.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    storage_profile:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        os_disk_image:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: dict
          sample: null
          contains:
            size_in_gb:
              description:
                - This property indicates the size of the VHD to be created.
              returned: always
              type: number
              sample: null
            host_caching:
              description:
                - >-
                  The host caching of the disk. Valid values are 'None',
                  'ReadOnly', and 'ReadWrite'
              returned: always
              type: str
              sample: null
        data_disk_images:
          description:
            - A list of data disk images.
          returned: always
          type: dict
          sample: null
          contains:
            size_in_gb:
              description:
                - This property indicates the size of the VHD to be created.
              returned: always
              type: number
              sample: null
            host_caching:
              description:
                - >-
                  The host caching of the disk. Valid values are 'None',
                  'ReadOnly', and 'ReadWrite'
              returned: always
              type: str
              sample: null
            lun:
              description:
                - >-
                  This property specifies the logical unit number of the data
                  disk. This value is used to identify data disks within the
                  Virtual Machine and therefore must be unique for each data
                  disk attached to the Virtual Machine.
              returned: always
              type: number
              sample: null
    replication_status:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        aggregated_state:
          description:
            - >-
              This is the aggregated replication status based on all the
              regional replication status flags.
          returned: always
          type: str
          sample: null
        summary:
          description:
            - This is a summary of replication status for each region.
          returned: always
          type: dict
          sample: null
          contains:
            region:
              description:
                - >-
                  The region to which the gallery Image Version is being
                  replicated to.
              returned: always
              type: str
              sample: null
            state:
              description:
                - This is the regional replication state.
              returned: always
              type: str
              sample: null
            details:
              description:
                - The details of the replication status.
              returned: always
              type: str
              sample: null
            progress:
              description:
                - It indicates progress of the replication job.
              returned: always
              type: number
              sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import SharedImageGalleryServiceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGalleryImageVersions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            gallery_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            gallery_image_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='gallery_image_version_name',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            publishing_profile=dict(
                type='dict',
                disposition='/',
                required=true,
                options=dict(
                    target_regions=dict(
                        type='list',
                        options=dict(
                            name=dict(
                                type='str',
                                required=true
                            ),
                            regional_replica_count=dict(
                                type='number'
                            ),
                            storage_account_type=dict(
                                type='str',
                                choices=['Standard_LRS',
                                         'Standard_ZRS']
                            )
                        )
                    ),
                    source=dict(
                        type='dict',
                        required=true,
                        options=dict(
                            managed_image=dict(
                                type='dict',
                                required=true,
                                options=dict(
                                    id=dict(
                                        type='str',
                                        required=true
                                    )
                                )
                            )
                        )
                    ),
                    replica_count=dict(
                        type='number'
                    ),
                    exclude_from_latest=dict(
                        type='boolean'
                    ),
                    end_of_life_date=dict(
                        type='datetime'
                    ),
                    storage_account_type=dict(
                        type='str',
                        choices=['Standard_LRS',
                                 'Standard_ZRS']
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
        self.gallery_name = None
        self.gallery_image_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImageVersions, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SharedImageGalleryServiceClient,
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
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.gallery_image_versions.create_or_update(resource_group_name=self.resource_group,
                                                                                gallery_name=self.gallery_name,
                                                                                gallery_image_name=self.gallery_image_name,
                                                                                gallery_image_version_name=self.name,
                                                                                gallery_image_version=self.galleryImageVersion)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImageVersion instance.')
            self.fail('Error creating the GalleryImageVersion instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the GalleryImageVersion instance {0}'.format(self.))
        try:
            response = self.mgmt_client.gallery_image_versions.delete(resource_group_name=self.resource_group,
                                                                      gallery_name=self.gallery_name,
                                                                      gallery_image_name=self.gallery_image_name,
                                                                      gallery_image_version_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImageVersion instance.')
            self.fail('Error deleting the GalleryImageVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the GalleryImageVersion instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.gallery_image_versions.get(resource_group_name=self.resource_group,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery_image_name=self.gallery_image_name,
                                                                   gallery_image_version_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImageVersions()


if __name__ == '__main__':
    main()
