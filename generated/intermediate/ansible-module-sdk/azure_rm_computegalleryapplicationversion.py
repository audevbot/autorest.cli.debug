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
module: azure_rm_computegalleryapplicationversion
version_added: '2.9'
short_description: Manage Azure GalleryApplicationVersion instance.
description:
  - 'Create, update and delete instance of Azure GalleryApplicationVersion.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Application Gallery in which the Application
        Definition resides.
    required: true
    type: str
  gallery_application_name:
    description:
      - >-
        The name of the gallery Application Definition in which the Application
        Version is to be created.
    required: true
    type: str
  gallery_application_version_name:
    description:
      - >-
        The name of the gallery Application Version to be created. Needs to
        follow semantic version name pattern: The allowed characters are digit
        and period. Digits must be within the range of a 32-bit integer. Format:
        <MajorVersion>.<MinorVersion>.<Patch>
    required: true
    type: str
  location:
    description:
      - Resource location
    required: true
    type: str
  publishing_profile:
    description:
      - undefined
    required: true
    type: dict
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
            type: str
          regional_replica_count:
            description:
              - >-
                The number of replicas of the Image Version to be created per
                region. This property is updatable.
            type: number
          storage_account_type:
            description:
              - >-
                Specifies the storage account type to be used to store the
                image. This property is not updatable.
            type: str
      replica_count:
        description:
          - >-
            The number of replicas of the Image Version to be created per
            region. This property would take effect for a region when
            regionalReplicaCount is not specified. This property is updatable.
        type: number
      exclude_from_latest:
        description:
          - >-
            If set to true, Virtual Machines deployed from the latest version of
            the Image Definition won't use this Image Version.
        type: boolean
      end_of_life_date:
        description:
          - >-
            The end of life date of the gallery Image Version. This property can
            be used for decommissioning purposes. This property is updatable.
        type: datetime
      storage_account_type:
        description:
          - >-
            Specifies the storage account type to be used to store the image.
            This property is not updatable.
        type: str
      source:
        description:
          - undefined
        required: true
        type: dict
        suboptions:
          file_name:
            description:
              - Required. The fileName of the artifact.
            required: true
            type: str
          media_link:
            description:
              - >-
                Required. The mediaLink of the artifact, must be a readable
                storage blob.
            required: true
            type: str
      content_type:
        description:
          - >-
            Optional. May be used to help process this file. The type of file
            contained in the source, e.g. zip, json, etc.
        type: str
      enable_health_check:
        description:
          - Optional. Whether or not this application reports health.
        type: boolean
      published_date:
        description:
          - The timestamp for when the gallery Image Version is published.
        type: datetime
  provisioning_state:
    description:
      - 'The provisioning state, which only appears in the response.'
    type: str
  replication_status:
    description:
      - undefined
    type: dict
    suboptions:
      aggregated_state:
        description:
          - >-
            This is the aggregated replication status based on all the regional
            replication status flags.
        type: str
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
            type: str
          state:
            description:
              - This is the regional replication state.
            type: str
          details:
            description:
              - The details of the replication status.
            type: str
          progress:
            description:
              - It indicates progress of the replication job.
            type: number
  id:
    description:
      - Resource Id
    type: str
  name:
    description:
      - Resource name
    type: str
  type:
    description:
      - Resource type
    type: str
  state:
    description:
      - Assert the state of the GalleryApplicationVersion.
      - >-
        Use C(present) to create or update an GalleryApplicationVersion and
        C(absent) to delete it.
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
- name: Create or update a simple gallery Application Version.
  azure_rm_computegalleryapplicationversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_application_name: myApplication
    gallery_application_version_name: myVersion
    gallery_application_version:
      location: West US
      properties:
        publishingProfile:
          source:
            fileName: package.zip
            mediaLink: >-
              https://mystorageaccount.blob.core.windows.net/mycontainer/package.zip?{sasKey}
          targetRegions:
            - name: West US
              regional_replica_count: '1'
              storage_account_type: Standard_LRS
          replicaCount: '1'
          endOfLifeDate: '2019-07-01T07:00:00Z'
          storageAccountType: Standard_LRS
- name: Delete a gallery Application Version.
  azure_rm_computegalleryapplicationversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_application_name: myApplication
    gallery_application_version_name: myVersion
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
    - ''
  returned: always
  type: dict
  sample: null
  contains:
    publishing_profile:
      description:
        - ''
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
        source:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            file_name:
              description:
                - Required. The fileName of the artifact.
              returned: always
              type: str
              sample: null
            media_link:
              description:
                - >-
                  Required. The mediaLink of the artifact, must be a readable
                  storage blob.
              returned: always
              type: str
              sample: null
        content_type:
          description:
            - >-
              Optional. May be used to help process this file. The type of file
              contained in the source, e.g. zip, json, etc.
          returned: always
          type: str
          sample: null
        enable_health_check:
          description:
            - Optional. Whether or not this application reports health.
          returned: always
          type: boolean
          sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    replication_status:
      description:
        - ''
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


class AzureRMGalleryApplicationVersions(AzureRMModuleBaseExt):
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
            gallery_application_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            gallery_application_version_name=dict(
                type='str',
                updatable=False,
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
                    ),
                    source=dict(
                        type='dict',
                        required=true,
                        options=dict(
                            file_name=dict(
                                type='str',
                                required=true
                            ),
                            media_link=dict(
                                type='str',
                                required=true
                            )
                        )
                    ),
                    content_type=dict(
                        type='str'
                    ),
                    enable_health_check=dict(
                        type='boolean'
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
        self.gallery_application_name = None
        self.gallery_application_version_name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryApplicationVersions, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.gallery_application_versions.create_or_update(resource_group_name=self.resource_group,
                                                                                      gallery_name=self.gallery_name,
                                                                                      gallery_application_name=self.gallery_application_name,
                                                                                      gallery_application_version_name=self.gallery_application_version_name,
                                                                                      gallery_application_version=self.galleryApplicationVersion)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryApplicationVersion instance.')
            self.fail('Error creating the GalleryApplicationVersion instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the GalleryApplicationVersion instance {0}'.format(self.))
        try:
            response = self.mgmt_client.gallery_application_versions.delete(resource_group_name=self.resource_group,
                                                                            gallery_name=self.gallery_name,
                                                                            gallery_application_name=self.gallery_application_name,
                                                                            gallery_application_version_name=self.gallery_application_version_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryApplicationVersion instance.')
            self.fail('Error deleting the GalleryApplicationVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the GalleryApplicationVersion instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.gallery_application_versions.get(resource_group_name=self.resource_group,
                                                                         gallery_name=self.gallery_name,
                                                                         gallery_application_name=self.gallery_application_name,
                                                                         gallery_application_version_name=self.gallery_application_version_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryApplicationVersions()


if __name__ == '__main__':
    main()
