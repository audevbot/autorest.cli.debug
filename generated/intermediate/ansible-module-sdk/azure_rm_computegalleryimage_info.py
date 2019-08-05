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
module: azure_rm_computegalleryimage_info
version_added: '2.9'
short_description: Get GalleryImage info.
description:
  - Get info of GalleryImage.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Image Gallery from which the Image Definitions
        are to be retrieved.
    required: true
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
  description:
    description:
      - >-
        The description of this gallery Image Definition resource. This property
        is updatable.
    type: str
  eula:
    description:
      - The Eula agreement for the gallery Image Definition.
    type: str
  privacy_statement_uri:
    description:
      - The privacy statement uri.
    type: str
  release_note_uri:
    description:
      - The release note uri.
    type: str
  os_type:
    description:
      - >-
        This property allows you to specify the type of the OS that is included
        in the disk when creating a VM from a managed image. <br><br> Possible
        values are: <br><br> **Windows** <br><br> **Linux**
    required: true
    type: str
  os_state:
    description:
      - >-
        This property allows the user to specify whether the virtual machines
        created under this image are 'Generalized' or 'Specialized'.
    required: true
    type: str
  end_of_life_date:
    description:
      - >-
        The end of life date of the gallery Image Definition. This property can
        be used for decommissioning purposes. This property is updatable.
    type: datetime
  identifier:
    description:
      - undefined
    required: true
    type: dict
    suboptions:
      publisher:
        description:
          - The name of the gallery Image Definition publisher.
        required: true
        type: str
      offer:
        description:
          - The name of the gallery Image Definition offer.
        required: true
        type: str
      sku:
        description:
          - The name of the gallery Image Definition SKU.
        required: true
        type: str
  recommended:
    description:
      - undefined
    type: dict
    suboptions:
      v_cpus:
        description:
          - undefined
        type: dict
        suboptions:
          min:
            description:
              - The minimum number of the resource.
            type: number
          max:
            description:
              - The maximum number of the resource.
            type: number
      memory:
        description:
          - undefined
        type: dict
        suboptions:
          min:
            description:
              - The minimum number of the resource.
            type: number
          max:
            description:
              - The maximum number of the resource.
            type: number
  disallowed:
    description:
      - undefined
    type: dict
    suboptions:
      disk_types:
        description:
          - A list of disk types.
        type: list
  purchase_plan:
    description:
      - undefined
    type: dict
    suboptions:
      name:
        description:
          - The plan ID.
        type: str
      publisher:
        description:
          - The publisher ID.
        type: str
      product:
        description:
          - The product ID.
        type: str
  provisioning_state:
    description:
      - 'The provisioning state, which only appears in the response.'
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List gallery images in a gallery.
  azure_rm_computegalleryimage_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
- name: Get a gallery image.
  azure_rm_computegalleryimage_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    name: myImage

'''

RETURN = '''
gallery_images:
  description: >-
    A list of dict results where the key is the name of the GalleryImage and the
    values are the facts for that GalleryImage.
  returned: always
  type: complex
  contains:
    galleryimage_name:
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


class AzureRMGalleryImagesInfo(AzureRMModuleBase):
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
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.gallery_name = None
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
        super(AzureRMGalleryImagesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SharedImageGalleryServiceClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.name is not None):
            self.results['gallery_images'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None):
            self.results['gallery_images'] = self.format_item(self.listbygallery())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_images.get(resource_group_name=self.resource_group,
                                                           gallery_name=self.gallery_name,
                                                           gallery_image_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbygallery(self):
        response = None

        try:
            response = self.mgmt_client.gallery_images.list_by_gallery(resource_group_name=self.resource_group,
                                                                       gallery_name=self.gallery_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMGalleryImagesInfo()


if __name__ == '__main__':
    main()
