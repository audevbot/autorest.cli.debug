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
module: azure_rm_servicebuseventhub_info
version_added: '2.9'
short_description: Get EventHub info.
description:
  - Get info of EventHub.
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
  name:
    description:
      - The namespace name
    required: true
  value:
    description:
      - Result of the List EventHubs operation.
    type: list
    suboptions:
      id:
        description:
          - Resource Id
      name:
        description:
          - Resource name
      type:
        description:
          - Resource type
      partition_ids:
        description:
          - Current number of shards on the Event Hub.
        type: list
      created_at:
        description:
          - Exact time the Event Hub was created.
      updated_at:
        description:
          - The exact time the message was updated.
      message_retention_in_days:
        description:
          - >-
            Number of days to retain the events for this Event Hub, value should
            be 1 to 7 days
      partition_count:
        description:
          - >-
            Number of partitions created for the Event Hub, allowed values are
            from 1 to 32 partitions.
      status:
        description:
          - Enumerates the possible values for the status of the Event Hub.
      capture_description:
        description:
          - Properties of capture description
        suboptions:
          enabled:
            description:
              - 'A value that indicates whether capture description is enabled. '
          encoding:
            description:
              - >-
                Enumerates the possible values for the encoding format of
                capture description.
          interval_in_seconds:
            description:
              - >-
                The time window allows you to set the frequency with which the
                capture to Azure Blobs will happen, value should between 60 to
                900 seconds
          size_limit_in_bytes:
            description:
              - >-
                The size window defines the amount of data built up in your
                Event Hub before an capture operation, value should be between
                10485760 and 524288000 bytes
          destination:
            description:
              - >-
                Properties of Destination where capture will be stored. (Storage
                Account, Blob Names)
            suboptions:
              name:
                description:
                  - Name for capture destination
  next_link:
    description:
      - >-
        Link to the next set of results. Not empty if Value contains incomplete
        list of EventHubs.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: RulesCreateOrUpdate
  azure_rm_servicebuseventhub_info:
    resource_group: myResourceGroup
    name: my

'''

RETURN = '''
event_hubs:
  description: >-
    A list of dict results where the key is the name of the EventHub and the
    values are the facts for that EventHub.
  returned: always
  type: complex
  contains:
    eventhub_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Result of the List EventHubs operation.
          returned: always
          type: dict
          sample: null
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
            properties:
              description:
                - >-
                  Properties supplied to the Create Or Update Event Hub
                  operation.
              returned: always
              type: dict
              sample: null
            partition_ids:
              description:
                - Current number of shards on the Event Hub.
              returned: always
              type: str
              sample: null
            created_at:
              description:
                - Exact time the Event Hub was created.
              returned: always
              type: datetime
              sample: null
            updated_at:
              description:
                - The exact time the message was updated.
              returned: always
              type: datetime
              sample: null
            message_retention_in_days:
              description:
                - >-
                  Number of days to retain the events for this Event Hub, value
                  should be 1 to 7 days
              returned: always
              type: number
              sample: null
            partition_count:
              description:
                - >-
                  Number of partitions created for the Event Hub, allowed values
                  are from 1 to 32 partitions.
              returned: always
              type: number
              sample: null
            status:
              description:
                - >-
                  Enumerates the possible values for the status of the Event
                  Hub.
              returned: always
              type: str
              sample: null
            capture_description:
              description:
                - Properties of capture description
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - >-
                      A value that indicates whether capture description is
                      enabled. 
                  returned: always
                  type: boolean
                  sample: null
                encoding:
                  description:
                    - >-
                      Enumerates the possible values for the encoding format of
                      capture description.
                  returned: always
                  type: str
                  sample: null
                interval_in_seconds:
                  description:
                    - >-
                      The time window allows you to set the frequency with which
                      the capture to Azure Blobs will happen, value should
                      between 60 to 900 seconds
                  returned: always
                  type: number
                  sample: null
                size_limit_in_bytes:
                  description:
                    - >-
                      The size window defines the amount of data built up in
                      your Event Hub before an capture operation, value should
                      be between 10485760 and 524288000 bytes
                  returned: always
                  type: number
                  sample: null
                destination:
                  description:
                    - >-
                      Properties of Destination where capture will be stored.
                      (Storage Account, Blob Names)
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    name:
                      description:
                        - Name for capture destination
                      returned: always
                      type: str
                      sample: null
                    properties:
                      description:
                        - >-
                          Properties describing the storage account, blob
                          container and archive name format for capture
                          destination
                      returned: always
                      type: dict
                      sample: null
        next_link:
          description:
            - >-
              Link to the next set of results. Not empty if Value contains
              incomplete list of EventHubs.
          returned: always
          type: str
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMEventHubsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str',
                required=true
            )
        )

        self.resource_group = None
        self.name = None
        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEventHubsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['event_hubs'] = self.format_item(self.listbynamespace())
        return self.results

    def listbynamespace(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ServiceBus' +
                    '/namespaces' +
                    '/{{ namespace_name }}' +
                    '/eventhubs')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.name)

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
    AzureRMEventHubsInfo()


if __name__ == '__main__':
    main()
