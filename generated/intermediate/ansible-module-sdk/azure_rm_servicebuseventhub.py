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
module: azure_rm_servicebuseventhub
version_added: '2.9'
short_description: Manage Azure EventHub instance.
description:
  - 'Create, update and delete instance of Azure EventHub.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  name:
    description:
      - The namespace name
    required: true
    type: str
  value:
    description:
      - Result of the List EventHubs operation.
    type: list
    suboptions:
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
      partition_ids:
        description:
          - Current number of shards on the Event Hub.
        type: list
      created_at:
        description:
          - Exact time the Event Hub was created.
        type: datetime
      updated_at:
        description:
          - The exact time the message was updated.
        type: datetime
      message_retention_in_days:
        description:
          - >-
            Number of days to retain the events for this Event Hub, value should
            be 1 to 7 days
        type: number
      partition_count:
        description:
          - >-
            Number of partitions created for the Event Hub, allowed values are
            from 1 to 32 partitions.
        type: number
      status:
        description:
          - Enumerates the possible values for the status of the Event Hub.
        type: str
      capture_description:
        description:
          - Properties of capture description
        type: dict
        suboptions:
          enabled:
            description:
              - 'A value that indicates whether capture description is enabled. '
            type: boolean
          encoding:
            description:
              - >-
                Enumerates the possible values for the encoding format of
                capture description.
            type: str
          interval_in_seconds:
            description:
              - >-
                The time window allows you to set the frequency with which the
                capture to Azure Blobs will happen, value should between 60 to
                900 seconds
            type: number
          size_limit_in_bytes:
            description:
              - >-
                The size window defines the amount of data built up in your
                Event Hub before an capture operation, value should be between
                10485760 and 524288000 bytes
            type: number
          destination:
            description:
              - >-
                Properties of Destination where capture will be stored. (Storage
                Account, Blob Names)
            type: dict
            suboptions:
              name:
                description:
                  - Name for capture destination
                type: str
  next_link:
    description:
      - >-
        Link to the next set of results. Not empty if Value contains incomplete
        list of EventHubs.
    type: str
  state:
    description:
      - Assert the state of the EventHub.
      - >-
        Use C(present) to create or update an EventHub and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
[]

'''

RETURN = '''
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
        - Properties supplied to the Create Or Update Event Hub operation.
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
          Number of days to retain the events for this Event Hub, value should
          be 1 to 7 days
      returned: always
      type: number
      sample: null
    partition_count:
      description:
        - >-
          Number of partitions created for the Event Hub, allowed values are
          from 1 to 32 partitions.
      returned: always
      type: number
      sample: null
    status:
      description:
        - Enumerates the possible values for the status of the Event Hub.
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
            - 'A value that indicates whether capture description is enabled. '
          returned: always
          type: boolean
          sample: null
        encoding:
          description:
            - >-
              Enumerates the possible values for the encoding format of capture
              description.
          returned: always
          type: str
          sample: null
        interval_in_seconds:
          description:
            - >-
              The time window allows you to set the frequency with which the
              capture to Azure Blobs will happen, value should between 60 to 900
              seconds
          returned: always
          type: number
          sample: null
        size_limit_in_bytes:
          description:
            - >-
              The size window defines the amount of data built up in your Event
              Hub before an capture operation, value should be between 10485760
              and 524288000 bytes
          returned: always
          type: number
          sample: null
        destination:
          description:
            - >-
              Properties of Destination where capture will be stored. (Storage
              Account, Blob Names)
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
                  Properties describing the storage account, blob container and
                  archive name format for capture destination
              returned: always
              type: dict
              sample: null
next_link:
  description:
    - >-
      Link to the next set of results. Not empty if Value contains incomplete
      list of EventHubs.
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
    from azure.mgmt.servicebus import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMEventHubs(AzureRMModuleBaseExt):
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
                disposition='namespace_name',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.value = None
        self.next_link = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEventHubs, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if self.location is None:
            self.location = resource_group.location

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
           self.results["value"] = response["value"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.event_hubs.create()
            else:
                response = self.mgmt_client.event_hubs.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the EventHub instance.')
            self.fail('Error creating the EventHub instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the EventHub instance {0}'.format(self.))
        try:
            response = self.mgmt_client.event_hubs.delete()
        except CloudError as e:
            self.log('Error attempting to delete the EventHub instance.')
            self.fail('Error deleting the EventHub instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the EventHub instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.event_hubs.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEventHubs()


if __name__ == '__main__':
    main()
