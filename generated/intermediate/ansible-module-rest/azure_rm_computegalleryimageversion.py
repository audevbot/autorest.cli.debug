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
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Image Gallery in which the Image Definition
        resides.
    required: true
    type: str
  gallery_image_name:
    description:
      - >-
        The name of the gallery Image Definition in which the Image Version is
        to be created.
    required: true
    type: str
  gallery_image_version_name:
    description:
      - >-
        The name of the gallery Image Version to be created. Needs to follow
        semantic version name pattern: The allowed characters are digit and
        period. Digits must be within the range of a 32-bit integer. Format:
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
          managed_image:
            description:
              - undefined
            required: true
            type: dict
            suboptions:
              id:
                description:
                  - The managed artifact id.
                required: true
                type: str
      published_date:
        description:
          - The timestamp for when the gallery Image Version is published.
        type: datetime
  provisioning_state:
    description:
      - 'The provisioning state, which only appears in the response.'
    type: str
  storage_profile:
    description:
      - undefined
    type: dict
    suboptions:
      os_disk_image:
        description:
          - undefined
        type: dict
        suboptions:
          size_in_gb:
            description:
              - This property indicates the size of the VHD to be created.
            type: number
          host_caching:
            description:
              - >-
                The host caching of the disk. Valid values are 'None',
                'ReadOnly', and 'ReadWrite'
            type: str
      data_disk_images:
        description:
          - A list of data disk images.
        type: list
        suboptions:
          size_in_gb:
            description:
              - This property indicates the size of the VHD to be created.
            type: number
          host_caching:
            description:
              - >-
                The host caching of the disk. Valid values are 'None',
                'ReadOnly', and 'ReadWrite'
            type: str
          lun:
            description:
              - >-
                This property specifies the logical unit number of the data
                disk. This value is used to identify data disks within the
                Virtual Machine and therefore must be unique for each data disk
                attached to the Virtual Machine.
            type: number
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
- name: Create or update a simple Gallery Image Version.
  azure_rm_computegalleryimageversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
    gallery_image_version_name: myVersion
    gallery_image_version:
      location: West US
      properties:
        publishingProfile:
          targetRegions:
            - name: West US
              regional_replica_count: '1'
            - name: East US
              regional_replica_count: '2'
              storage_account_type: Standard_ZRS
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
    gallery_image_version_name: myVersion
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
            managed_image:
              description:
                - ''
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
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    storage_profile:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        os_disk_image:
          description:
            - ''
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGalleryImageVersions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            gallery_name=dict(
                type='str',
                updatable=False,
                disposition='galleryName',
                required=true
            ),
            gallery_image_name=dict(
                type='str',
                updatable=False,
                disposition='galleryImageName',
                required=true
            ),
            gallery_image_version_name=dict(
                type='str',
                updatable=False,
                disposition='galleryImageVersionName',
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
                disposition='/properties/publishingProfile',
                required=true,
                options=dict(
                    target_regions=dict(
                        type='list',
                        disposition='targetRegions',
                        options=dict(
                            name=dict(
                                type='str',
                                required=true
                            ),
                            regional_replica_count=dict(
                                type='number',
                                disposition='regionalReplicaCount'
                            ),
                            storage_account_type=dict(
                                type='str',
                                disposition='storageAccountType',
                                choices=['Standard_LRS',
                                         'Standard_ZRS']
                            )
                        )
                    ),
                    replica_count=dict(
                        type='number',
                        disposition='replicaCount'
                    ),
                    exclude_from_latest=dict(
                        type='boolean',
                        disposition='excludeFromLatest'
                    ),
                    end_of_life_date=dict(
                        type='datetime',
                        disposition='endOfLifeDate'
                    ),
                    storage_account_type=dict(
                        type='str',
                        disposition='storageAccountType',
                        choices=['Standard_LRS',
                                 'Standard_ZRS']
                    ),
                    source=dict(
                        type='dict',
                        required=true,
                        options=dict(
                            managed_image=dict(
                                type='dict',
                                disposition='managedImage',
                                required=true,
                                options=dict(
                                    id=dict(
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
        self.gallery_name = None
        self.gallery_image_name = None
        self.gallery_image_version_name = None
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
        self.query_parameters['api-version'] = '2019-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

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
                    '/Microsoft.Compute' +
                    '/galleries' +
                    '/{{ gallery_name }}' +
                    '/images' +
                    '/{{ image_name }}' +
                    '/versions' +
                    '/{{ version_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ gallery_name }}', self.gallery_name)
        self.url = self.url.replace('{{ image_name }}', self.image_name)
        self.url = self.url.replace('{{ version_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("GalleryImageVersion instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('GalleryImageVersion instance already exists')

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
            self.log('Need to Create / Update the GalleryImageVersion instance')

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
            self.log('GalleryImageVersion instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('GalleryImageVersion instance unchanged')
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
        # self.log('Creating / Updating the GalleryImageVersion instance {0}'.format(self.))

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
            self.log('Error attempting to create the GalleryImageVersion instance.')
            self.fail('Error creating the GalleryImageVersion instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the GalleryImageVersion instance {0}'.format(self.))
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
            self.log('Error attempting to delete the GalleryImageVersion instance.')
            self.fail('Error deleting the GalleryImageVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the GalleryImageVersion instance {0} is present'.format(self.))
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
            # self.log("GalleryImageVersion instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the GalleryImageVersion instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMGalleryImageVersions()


if __name__ == '__main__':
    main()
