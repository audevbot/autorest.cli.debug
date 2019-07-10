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
module: azure_rm_computegalleryapplication
version_added: '2.9'
short_description: Manage Azure GalleryApplication instance.
description:
  - 'Create, update and delete instance of Azure GalleryApplication.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
  gallery_name:
    description:
      - >-
        The name of the Shared Application Gallery in which the Application
        Definition is to be created.
    required: true
  name:
    description:
      - Resource name
  location:
    description:
      - Resource location
    required: true
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
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  state:
    description:
      - Assert the state of the GalleryApplication.
      - >-
        Use C(present) to create or update an GalleryApplication and C(absent)
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
- name: Create or update a simple gallery Application.
  azure_rm_computegalleryapplication:
    resource_group: myResourceGroup
    gallery_name: myGallery
    name: myApplication
    gallery_application:
      location: West US
      properties:
        description: This is the gallery application description.
        eula: This is the gallery application EULA.
        privacyStatementUri: 'myPrivacyStatementUri}'
        releaseNoteUri: myReleaseNoteUri
        supportedOSType: Windows
- name: Delete a gallery Application.
  azure_rm_computegalleryapplication:
    resource_group: myResourceGroup
    gallery_name: myGallery
    name: myApplication
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
          The description of this gallery Application Definition resource. This
          property is updatable.
      returned: always
      type: str
      sample: null
    eula:
      description:
        - The Eula agreement for the gallery Application Definition.
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
    end_of_life_date:
      description:
        - >-
          The end of life date of the gallery Application Definition. This
          property can be used for decommissioning purposes. This property is
          updatable.
      returned: always
      type: datetime
      sample: null
    supported_ostype:
      description:
        - >-
          This property allows you to specify the supported type of the OS that
          application is built for. <br><br> Possible values are: <br><br>
          **Windows** <br><br> **Linux**
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


class AzureRMGalleryApplications(AzureRMModuleBaseExt):
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
            name=dict(
                type='str',
                updatable=False,
                disposition='gallery_application_name',
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
            end_of_life_date=dict(
                type='datetime',
                disposition='/'
            ),
            supported_ostype=dict(
                type='str',
                disposition='/',
                choices=['Windows',
                         'Linux'],
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryApplications, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.gallery_applications.create_or_update(resource_group_name=self.resource_group,
                                                                              gallery_name=self.gallery_name,
                                                                              gallery_application_name=self.name,
                                                                              gallery_application=self.galleryApplication)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryApplication instance.')
            self.fail('Error creating the GalleryApplication instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the GalleryApplication instance {0}'.format(self.))
        try:
            response = self.mgmt_client.gallery_applications.delete(resource_group_name=self.resource_group,
                                                                    gallery_name=self.gallery_name,
                                                                    gallery_application_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryApplication instance.')
            self.fail('Error deleting the GalleryApplication instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the GalleryApplication instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.gallery_applications.get(resource_group_name=self.resource_group,
                                                                 gallery_name=self.gallery_name,
                                                                 gallery_application_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryApplications()


if __name__ == '__main__':
    main()
