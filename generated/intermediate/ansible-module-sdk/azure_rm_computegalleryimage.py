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
module: azure_rm_computegalleryimage
version_added: '2.9'
short_description: Manage Azure GalleryImage instance.
description:
  - 'Create, update and delete instance of Azure GalleryImage.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Image Gallery in which the Image Definition is to
        be created.
    required: true
    type: str
  gallery_image_name:
    description:
      - >-
        The name of the gallery Image Definition to be created or updated. The
        allowed characters are alphabets and numbers with dots, dashes, and
        periods allowed in the middle. The maximum length is 80 characters.
    required: true
    type: str
  location:
    description:
      - Resource location
    required: true
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
      - Assert the state of the GalleryImage.
      - >-
        Use C(present) to create or update an GalleryImage and C(absent) to
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
- name: Create or update a simple gallery image.
  azure_rm_computegalleryimage:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
    gallery_image:
      location: West US
      properties:
        osType: Windows
        osState: Generalized
        identifier:
          publisher: myPublisherName
          offer: myOfferName
          sku: mySkuName
- name: Delete a gallery image.
  azure_rm_computegalleryimage:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myImage
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
    description:
      description:
        - >-
          The description of this gallery Image Definition resource. This
          property is updatable.
      returned: always
      type: str
      sample: null
    eula:
      description:
        - The Eula agreement for the gallery Image Definition.
      returned: always
      type: str
      sample: null
    privacy_statement_uri:
      description:
        - The privacy statement uri.
      returned: always
      type: str
      sample: null
    release_note_uri:
      description:
        - The release note uri.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - >-
          This property allows you to specify the type of the OS that is
          included in the disk when creating a VM from a managed image. <br><br>
          Possible values are: <br><br> **Windows** <br><br> **Linux**
      returned: always
      type: str
      sample: null
    os_state:
      description:
        - >-
          This property allows the user to specify whether the virtual machines
          created under this image are 'Generalized' or 'Specialized'.
      returned: always
      type: str
      sample: null
    end_of_life_date:
      description:
        - >-
          The end of life date of the gallery Image Definition. This property
          can be used for decommissioning purposes. This property is updatable.
      returned: always
      type: datetime
      sample: null
    identifier:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        publisher:
          description:
            - The name of the gallery Image Definition publisher.
          returned: always
          type: str
          sample: null
        offer:
          description:
            - The name of the gallery Image Definition offer.
          returned: always
          type: str
          sample: null
        sku:
          description:
            - The name of the gallery Image Definition SKU.
          returned: always
          type: str
          sample: null
    recommended:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        v_cpus:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            min:
              description:
                - The minimum number of the resource.
              returned: always
              type: number
              sample: null
            max:
              description:
                - The maximum number of the resource.
              returned: always
              type: number
              sample: null
        memory:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            min:
              description:
                - The minimum number of the resource.
              returned: always
              type: number
              sample: null
            max:
              description:
                - The maximum number of the resource.
              returned: always
              type: number
              sample: null
    disallowed:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        disk_types:
          description:
            - A list of disk types.
          returned: always
          type: str
          sample: null
    purchase_plan:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - The plan ID.
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - The publisher ID.
          returned: always
          type: str
          sample: null
        product:
          description:
            - The product ID.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
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
    from azure.mgmt.compute import SharedImageGalleryServiceClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGalleryImages(AzureRMModuleBaseExt):
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
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            eula=dict(
                type='str',
                disposition='/'
            ),
            privacy_statement_uri=dict(
                type='str',
                disposition='/'
            ),
            release_note_uri=dict(
                type='str',
                disposition='/'
            ),
            os_type=dict(
                type='str',
                disposition='/',
                choices=['Windows',
                         'Linux'],
                required=true
            ),
            os_state=dict(
                type='str',
                disposition='/',
                choices=['Generalized',
                         'Specialized'],
                required=true
            ),
            end_of_life_date=dict(
                type='datetime',
                disposition='/'
            ),
            identifier=dict(
                type='dict',
                disposition='/',
                required=true,
                options=dict(
                    publisher=dict(
                        type='str',
                        required=true
                    ),
                    offer=dict(
                        type='str',
                        required=true
                    ),
                    sku=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            recommended=dict(
                type='dict',
                disposition='/',
                options=dict(
                    v_cpus=dict(
                        type='dict',
                        options=dict(
                            min=dict(
                                type='number'
                            ),
                            max=dict(
                                type='number'
                            )
                        )
                    ),
                    memory=dict(
                        type='dict',
                        options=dict(
                            min=dict(
                                type='number'
                            ),
                            max=dict(
                                type='number'
                            )
                        )
                    )
                )
            ),
            disallowed=dict(
                type='dict',
                disposition='/',
                options=dict(
                    disk_types=dict(
                        type='list'
                    )
                )
            ),
            purchase_plan=dict(
                type='dict',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str'
                    ),
                    publisher=dict(
                        type='str'
                    ),
                    product=dict(
                        type='str'
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
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImages, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.gallery_images.create_or_update(resource_group_name=self.resource_group,
                                                                        gallery_name=self.gallery_name,
                                                                        gallery_image_name=self.gallery_image_name,
                                                                        gallery_image=self.galleryImage)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImage instance.')
            self.fail('Error creating the GalleryImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the GalleryImage instance {0}'.format(self.))
        try:
            response = self.mgmt_client.gallery_images.delete(resource_group_name=self.resource_group,
                                                              gallery_name=self.gallery_name,
                                                              gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImage instance.')
            self.fail('Error deleting the GalleryImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the GalleryImage instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.gallery_images.get(resource_group_name=self.resource_group,
                                                           gallery_name=self.gallery_name,
                                                           gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImages()


if __name__ == '__main__':
    main()
