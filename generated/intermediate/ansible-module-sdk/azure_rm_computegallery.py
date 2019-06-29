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
module: azure_rm_computegallery
version_added: '2.9'
short_description: Manage Azure Gallery instance.
description:
  - 'Create, update and delete instance of Azure Gallery.'
options:
  resource_group:
    description:
      - The name of the resource group.
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
        The description of this Shared Image Gallery resource. This property is
        updatable.
  identifier:
    description:
      - undefined
    suboptions:
      unique_name:
        description:
          - >-
            The unique name of the Shared Image Gallery. This name is generated
            automatically by Azure.
  provisioning_state:
    description:
      - 'The provisioning state, which only appears in the response.'
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource type
  state:
    description:
      - Assert the state of the Gallery.
      - >-
        Use C(present) to create or update an Gallery and C(absent) to delete
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
- name: Create or update a simple gallery.
  azure_rm_computegallery:
    resource_group: myResourceGroup
    name: myGallery
    gallery:
      location: West US
      properties:
        description: This is the gallery description.
- name: Delete a gallery.
  azure_rm_computegallery:
    resource_group: myResourceGroup
    name: myGallery
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
          The description of this Shared Image Gallery resource. This property
          is updatable.
      returned: always
      type: str
      sample: null
    identifier:
      description:
        - ''
      returned: always
      type: dict
      sample: null
      contains:
        unique_name:
          description:
            - >-
              The unique name of the Shared Image Gallery. This name is
              generated automatically by Azure.
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


class AzureRMGalleries(AzureRMModuleBaseExt):
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
                disposition='gallery_name',
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
            identifier=dict(
                type='dict',
                disposition='/',
                options=dict(
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleries, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.galleries.create_or_update(resource_group_name=self.resource_group,
                                                                   gallery_name=self.name,
                                                                   gallery=self.gallery)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Gallery instance.')
            self.fail('Error creating the Gallery instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Gallery instance {0}'.format(self.))
        try:
            response = self.mgmt_client.galleries.delete(resource_group_name=self.resource_group,
                                                         gallery_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Gallery instance.')
            self.fail('Error deleting the Gallery instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Gallery instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.galleries.get(resource_group_name=self.resource_group,
                                                      gallery_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleries()


if __name__ == '__main__':
    main()
