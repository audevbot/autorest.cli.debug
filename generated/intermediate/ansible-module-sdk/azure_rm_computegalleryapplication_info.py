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
module: azure_rm_computegalleryapplication_info
version_added: '2.9'
short_description: Get GalleryApplication info.
description:
  - Get info of GalleryApplication.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  gallery_name:
    description:
      - >-
        The name of the Shared Application Gallery from which the Application
        Definitions are to be retrieved.
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
  description:
    description:
      - >-
        The description of this gallery Application Definition resource. This
        property is updatable.
  eula:
    description:
      - The Eula agreement for the gallery Application Definition.
  privacy_statement_uri:
    description:
      - The privacy statement uri.
  release_note_uri:
    description:
      - The release note uri.
  end_of_life_date:
    description:
      - >-
        The end of life date of the gallery Application Definition. This
        property can be used for decommissioning purposes. This property is
        updatable.
  supported_ostype:
    description:
      - >-
        This property allows you to specify the supported type of the OS that
        application is built for. <br><br> Possible values are: <br><br>
        **Windows** <br><br> **Linux**
    required: true
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List gallery Applications in a gallery.
  azure_rm_computegalleryapplication_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
- name: Get a gallery Application.
  azure_rm_computegalleryapplication_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    name: myApplication

'''

RETURN = '''
gallery_applications:
  description: >-
    A list of dict results where the key is the name of the GalleryApplication
    and the values are the facts for that GalleryApplication.
  returned: always
  type: complex
  contains:
    galleryapplication_name:
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


class AzureRMGalleryApplicationsInfo(AzureRMModuleBase):
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
        super(AzureRMGalleryApplicationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SharedImageGalleryServiceClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.name is not None):
            self.results['gallery_applications'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None):
            self.results['gallery_applications'] = self.format_item(self.listbygallery())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_applications.get(resource_group_name=self.resource_group,
                                                                 gallery_name=self.gallery_name,
                                                                 gallery_application_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbygallery(self):
        response = None

        try:
            response = self.mgmt_client.gallery_applications.list_by_gallery(resource_group_name=self.resource_group,
                                                                             gallery_name=self.gallery_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMGalleryApplicationsInfo()


if __name__ == '__main__':
    main()
