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
module: azure_rm_apimanagementnotification_info
version_added: '2.9'
short_description: Get Notification info.
description:
  - Get info of Notification.
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  title:
    description:
      - Title of the Notification.
    required: true
    type: str
  description:
    description:
      - Description of the Notification.
    type: str
  recipients:
    description:
      - Recipient Parameter values.
    type: dict
    suboptions:
      emails:
        description:
          - List of Emails subscribed for the notification.
        type: list
      users:
        description:
          - List of Users subscribed for the notification.
        type: list
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListNotifications
  azure_rm_apimanagementnotification_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetNotification
  azure_rm_apimanagementnotification_info:
    resource_group: myResourceGroup
    service_name: myService
    name: myNotification

'''

RETURN = '''
notification:
  description: >-
    A list of dict results where the key is the name of the Notification and the
    values are the facts for that Notification.
  returned: always
  type: complex
  contains:
    notification_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type for API Management resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Notification entity contract properties.
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNotificationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            service_name=dict(
                type='str',
                required=true
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
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
        super(AzureRMNotificationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClientClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.name is not None):
            self.results['notification'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['notification'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.notification.get(resource_group_name=self.resource_group,
                                                         service_name=self.service_name,
                                                         notification_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.notification.list_by_service(resource_group_name=self.resource_group,
                                                                     service_name=self.service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMNotificationInfo()


if __name__ == '__main__':
    main()
