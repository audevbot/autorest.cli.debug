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
module: azure_rm_computegalleryimageversion_info
version_added: '2.9'
short_description: Get GalleryImageVersion info.
description:
  - Get info of GalleryImageVersion.
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
        The name of the gallery Image Definition in which the Image Version
        resides.
    required: true
  name:
    description:
      - Resource name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  location:
    description:
      - Resource location
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
      published_date:
        description:
          - The timestamp for when the gallery Image Version is published.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List gallery Image Versions in a gallery Image Definition.
  azure_rm_computegalleryimageversion_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
- name: Get a gallery Image Version.
  azure_rm_computegalleryimageversion_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
    name: myVersion
- name: Get a gallery Image Version with replication status.
  azure_rm_computegalleryimageversion_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
    name: myVersion

'''

RETURN = '''
gallery_image_versions:
  description: >-
    A list of dict results where the key is the name of the GalleryImageVersion
    and the values are the facts for that GalleryImageVersion.
  returned: always
  type: complex
  contains:
    galleryimageversion_name:
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
            {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
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
    from azure.mgmt.compute import SharedImageGalleryServiceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGalleryImageVersionsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            gallery_name=dict(
                type='str',
                required=true
            ),
            gallery_image_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_image_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.tags = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGalleryImageVersionsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SharedImageGalleryServiceClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_image_name is not None and
            self.name is not None):
            self.results['gallery_image_versions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None and
              self.gallery_image_name is not None):
            self.results['gallery_image_versions'] = self.format_item(self.listbygalleryimage())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_image_versions.get(resource_group_name=self.resource_group,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery_image_name=self.gallery_image_name,
                                                                   gallery_image_version_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbygalleryimage(self):
        response = None

        try:
            response = self.mgmt_client.gallery_image_versions.list_by_gallery_image(resource_group_name=self.resource_group,
                                                                                     gallery_name=self.gallery_name,
                                                                                     gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMGalleryImageVersionsInfo()


if __name__ == '__main__':
    main()
