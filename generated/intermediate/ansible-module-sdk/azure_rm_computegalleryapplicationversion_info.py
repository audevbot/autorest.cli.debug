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
module: azure_rm_computegalleryapplicationversion_info
version_added: '2.9'
short_description: Get GalleryApplicationVersion info.
description:
  - Get info of GalleryApplicationVersion.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  gallery_name:
    description:
      - >-
        The name of the Shared Application Gallery in which the Application
        Definition resides.
    required: true
  gallery_application_name:
    description:
      - >-
        The name of the gallery Application Definition in which the Application
        Version resides.
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
          file_name:
            description:
              - Required. The fileName of the artifact.
            required: true
          media_link:
            description:
              - >-
                Required. The mediaLink of the artifact, must be a readable
                storage blob.
            required: true
      content_type:
        description:
          - >-
            Optional. May be used to help process this file. The type of file
            contained in the source, e.g. zip, json, etc.
      enable_health_check:
        description:
          - Optional. Whether or not this application reports health.
  provisioning_state:
    description:
      - 'The provisioning state, which only appears in the response.'
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
- name: List gallery Application Versions in a gallery Application Definition.
  azure_rm_computegalleryapplicationversion_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_application_name: myApplication
- name: Get a gallery Application Version.
  azure_rm_computegalleryapplicationversion_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_application_name: myApplication
    name: myVersion
- name: Get a gallery Application Version with replication status.
  azure_rm_computegalleryapplicationversion_info:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_application_name: myApplication
    name: myVersion

'''

RETURN = '''
gallery_application_versions:
  description: >-
    A list of dict results where the key is the name of the
    GalleryApplicationVersion and the values are the facts for that
    GalleryApplicationVersion.
  returned: always
  type: complex
  contains:
    galleryapplicationversion_name:
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


class AzureRMGalleryApplicationVersionsInfo(AzureRMModuleBase):
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
            gallery_application_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_application_name = None
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
        super(AzureRMGalleryApplicationVersionsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SharedImageGalleryServiceClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_application_name is not None and
            self.name is not None):
            self.results['gallery_application_versions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None and
              self.gallery_application_name is not None):
            self.results['gallery_application_versions'] = self.format_item(self.listbygalleryapplication())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_application_versions.get(resource_group_name=self.resource_group,
                                                                         gallery_name=self.gallery_name,
                                                                         gallery_application_name=self.gallery_application_name,
                                                                         gallery_application_version_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbygalleryapplication(self):
        response = None

        try:
            response = self.mgmt_client.gallery_application_versions.list_by_gallery_application(resource_group_name=self.resource_group,
                                                                                                 gallery_name=self.gallery_name,
                                                                                                 gallery_application_name=self.gallery_application_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMGalleryApplicationVersionsInfo()


if __name__ == '__main__':
    main()
