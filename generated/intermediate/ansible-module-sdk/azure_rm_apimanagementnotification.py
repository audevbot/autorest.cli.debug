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
module: azure_rm_apimanagementnotification
version_added: '2.9'
short_description: Manage Azure Notification instance.
description:
  - 'Create, update and delete instance of Azure Notification.'
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
  state:
    description:
      - Assert the state of the Notification.
      - >-
        Use C(present) to create or update an Notification and C(absent) to
        delete it.
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
- name: ApiManagementCreateNotification
  azure_rm_apimanagementnotification:
    resource_group: myResourceGroup
    service_name: myService
    name: myNotification

'''

RETURN = '''
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNotification(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='notification_name',
                required=true
            ),
            title=dict(
                type='str',
                disposition='/',
                required=true
            ),
            description=dict(
                type='str',
                disposition='/'
            ),
            recipients=dict(
                type='dict',
                disposition='/',
                options=dict(
                    emails=dict(
                        type='list'
                    ),
                    users=dict(
                        type='list'
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
        self.service_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.properties = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNotification, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClient,
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
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.notification.create_or_update(resource_group_name=self.resource_group,
                                                                      service_name=self.service_name,
                                                                      notification_name=self.name)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Notification instance.')
            self.fail('Error creating the Notification instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Notification instance {0}'.format(self.))
        try:
            response = self.mgmt_client.notification.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Notification instance.')
            self.fail('Error deleting the Notification instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Notification instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.notification.get(resource_group_name=self.resource_group,
                                                         service_name=self.service_name,
                                                         notification_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNotification()


if __name__ == '__main__':
    main()
