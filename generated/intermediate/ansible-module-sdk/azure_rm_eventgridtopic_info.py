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
module: azure_rm_eventgridtopic_info
version_added: '2.9'
short_description: Get Topic info.
description:
  - Get info of Topic.
options:
  resource_group:
    description:
      - The name of the resource group within the user's subscription.
  topic_name:
    description:
      - Name of the topic
  provider_namespace:
    description:
      - Namespace of the provider of the topic
  resource_type_name:
    description:
      - Name of the topic type
  name:
    description:
      - Name of the resource
  id:
    description:
      - Fully qualified identifier of the resource
  type:
    description:
      - Type of the resource
  location:
    description:
      - Location of the resource
  provisioning_state:
    description:
      - Provisioning state of the topic.
  endpoint:
    description:
      - Endpoint for the topic.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Topics_ListBySubscription
  azure_rm_eventgridtopic_info: {}
- name: Topics_ListByResourceGroup
  azure_rm_eventgridtopic_info:
    resource_group: myResourceGroup
- name: Topics_Get
  azure_rm_eventgridtopic_info:
    resource_group: myResourceGroup
    topic_name: myTopic
- name: Topics_ListEventTypes
  azure_rm_eventgridtopic_info:
    resource_group: myResourceGroup
    provider_namespace: Microsoft.Storage
    resource_type_name: storageAccounts
    name: myResourceType

'''

RETURN = '''
topics:
  description: >-
    A list of dict results where the key is the name of the Topic and the values
    are the facts for that Topic.
  returned: always
  type: complex
  contains:
    topic_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Fully qualified identifier of the resource
          returned: always
          type: str
          sample: null
        name:
          description:
            - Name of the resource
          returned: always
          type: str
          sample: null
        type:
          description:
            - Type of the resource
          returned: always
          type: str
          sample: null
        location:
          description:
            - Location of the resource
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Tags of the resource
          returned: always
          type: >-
            unknown[DictionaryType
            {"$id":"342","$type":"DictionaryType","valueType":{"$id":"343","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"344","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"345","fixed":false},"deprecated":false}]
          sample: null
        properties:
          description:
            - Properties of the topic
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
    from azure.mgmt.eventgrid import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTopicsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            topic_name=dict(
                type='str'
            ),
            provider_namespace=dict(
                type='str'
            ),
            resource_type_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.topic_name = None
        self.provider_namespace = None
        self.resource_type_name = None
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
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTopicsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.provider_namespace is not None and
            self.resource_type_name is not None and
            self.name is not None):
            self.results['topics'] = self.format_item(self.listeventtypes())
        elif (self.resource_group is not None and
              self.topic_name is not None):
            self.results['topics'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['topics'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['topics'] = [self.format_item(self.listbysubscription())]
        return self.results

    def listeventtypes(self):
        response = None

        try:
            response = self.mgmt_client.topics.list_event_types(resource_group_name=self.resource_group,
                                                                provider_namespace=self.provider_namespace,
                                                                resource_type_name=self.resource_type_name,
                                                                resource_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def get(self):
        response = None

        try:
            response = self.mgmt_client.topics.get(resource_group_name=self.resource_group,
                                                   topic_name=self.topic_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.topics.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.topics.list_by_subscription()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMTopicsInfo()


if __name__ == '__main__':
    main()
