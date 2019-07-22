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
module: eventgridtopictype_info
version_added: '2.9'
short_description: Get TopicType info.
description:
  - Get info of TopicType.
options:
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
  provider:
    description:
      - Namespace of the provider of the topic type.
    type: str
  display_name:
    description:
      - Display Name for the topic type.
    type: str
  description:
    description:
      - Description of the topic type.
    type: str
  resource_region_type:
    description:
      - Region type of the resource.
    type: str
  provisioning_state:
    description:
      - Provisioning state of the topic type
    type: str
  supported_locations:
    description:
      - List of locations supported by this topic type.
    type: list
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: TopicTypes_List
  azure.rm.eventgridtopictype.info: {}
- name: TopicTypes_Get
  azure.rm.eventgridtopictype.info:
    name: myTopicType
- name: TopicTypes_ListEventTypes
  azure.rm.eventgridtopictype.info:
    name: myTopicType

'''

RETURN = '''
topic_types:
  description: >-
    A list of dict results where the key is the name of the TopicType and the
    values are the facts for that TopicType.
  returned: always
  type: complex
  contains:
    topictype_name:
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
        properties:
          description:
            - Properties of the topic type info
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


class AzureRMTopicTypesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str'
            )
        )

        self.name = None
        self.id = None
        self.name = None
        self.type = None
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
        super(AzureRMTopicTypesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.name is not None):
            self.results['topic_types'] = self.format_item(self.listeventtypes())
        elif (self.name is not None):
            self.results['topic_types'] = self.format_item(self.get())
        else:
            self.results['topic_types'] = [self.format_item(self.list())]
        return self.results

    def listeventtypes(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/providers' +
                    '/Microsoft.EventGrid' +
                    '/topicTypes' +
                    '/{{ topic_type_name }}' +
                    '/eventTypes')
        self.url = self.url.replace('{{ topic_type_name }}', self.name)

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
        self.url = ('/providers' +
                    '/Microsoft.EventGrid' +
                    '/topicTypes' +
                    '/{{ topic_type_name }}')
        self.url = self.url.replace('{{ topic_type_name }}', self.name)

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

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/providers' +
                    '/Microsoft.EventGrid' +
                    '/topicTypes')
        self.url = self.url.replace('{{ topic_type_name }}', self.name)

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
    AzureRMTopicTypesInfo()


if __name__ == '__main__':
    main()
