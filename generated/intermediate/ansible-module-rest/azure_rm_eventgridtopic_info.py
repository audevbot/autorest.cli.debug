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
    type: str
  topic_name:
    description:
      - Name of the topic
    type: str
  provider_namespace:
    description:
      - Namespace of the provider of the topic
    type: str
  resource_type_name:
    description:
      - Name of the topic type
    type: str
  name:
    description:
      - Name of the resource
    type: str
  id:
    description:
      - Fully qualified identifier of the resource
    type: str
  type:
    description:
      - Type of the resource
    type: str
  location:
    description:
      - Location of the resource
    type: str
  provisioning_state:
    description:
      - Provisioning state of the topic.
    type: str
  endpoint:
    description:
      - Endpoint for the topic.
    type: str
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
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
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/{providerNamespace}' +
                    '/{resourceTypeName}' +
                    '/{{ {resource_type_name}_name }}' +
                    '/providers' +
                    '/Microsoft.EventGrid' +
                    '/eventTypes')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ {resource_type_name}_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.EventGrid' +
                    '/topics' +
                    '/{{ topic_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ {resource_type_name}_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbyresourcegroup(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.EventGrid' +
                    '/topics')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ {resource_type_name}_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbysubscription(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.EventGrid' +
                    '/topics')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ {resource_type_name}_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMTopicsInfo()


if __name__ == '__main__':
    main()
