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
module: azure_rm_apimanagementapirevision
version_added: '2.9'
short_description: Manage Azure ApiRevision instance.
description:
  - 'Create, update and delete instance of Azure ApiRevision.'
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
  api_id:
    description:
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
      api_id:
        description:
          - Identifier of the API Revision.
        type: str
      api_revision:
        description:
          - Revision number of API.
        type: str
      created_date_time:
        description:
          - >-
            The time the API Revision was created. The date conforms to the
            following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601
            standard.
        type: datetime
      updated_date_time:
        description:
          - >-
            The time the API Revision were updated. The date conforms to the
            following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601
            standard.
        type: datetime
      description:
        description:
          - Description of the API Revision.
        type: str
      private_url:
        description:
          - Gateway URL for accessing the non-current API Revision.
        type: str
      is_online:
        description:
          - Indicates if API revision is the current api revision.
        type: boolean
      is_current:
        description:
          - Indicates if API revision is accessible via the gateway.
        type: boolean
  next_link:
    description:
      - Next page link if any.
    type: str
  state:
    description:
      - Assert the state of the ApiRevision.
      - >-
        Use C(present) to create or update an ApiRevision and C(absent) to
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
[]

'''

RETURN = '''
value:
  description:
    - Page values.
  returned: always
  type: dict
  sample: null
  contains:
    api_id:
      description:
        - Identifier of the API Revision.
      returned: always
      type: str
      sample: null
    api_revision:
      description:
        - Revision number of API.
      returned: always
      type: str
      sample: null
    created_date_time:
      description:
        - >-
          The time the API Revision was created. The date conforms to the
          following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601
          standard.
      returned: always
      type: datetime
      sample: null
    updated_date_time:
      description:
        - >-
          The time the API Revision were updated. The date conforms to the
          following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601
          standard.
      returned: always
      type: datetime
      sample: null
    description:
      description:
        - Description of the API Revision.
      returned: always
      type: str
      sample: null
    private_url:
      description:
        - Gateway URL for accessing the non-current API Revision.
      returned: always
      type: str
      sample: null
    is_online:
      description:
        - Indicates if API revision is the current api revision.
      returned: always
      type: boolean
      sample: null
    is_current:
      description:
        - Indicates if API revision is accessible via the gateway.
      returned: always
      type: boolean
      sample: null
next_link:
  description:
    - Next page link if any.
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMApiRevision(AzureRMModuleBaseExt):
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
            api_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.value = None
        self.next_link = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMApiRevision, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["value"] = response["value"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.api_revision.create()
            else:
                response = self.mgmt_client.api_revision.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ApiRevision instance.')
            self.fail('Error creating the ApiRevision instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ApiRevision instance {0}'.format(self.))
        try:
            response = self.mgmt_client.api_revision.delete()
        except CloudError as e:
            self.log('Error attempting to delete the ApiRevision instance.')
            self.fail('Error deleting the ApiRevision instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ApiRevision instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.api_revision.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMApiRevision()


if __name__ == '__main__':
    main()
