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
module: azure_rm_apimanagementtenantconfiguration
version_added: '2.9'
short_description: Manage Azure TenantConfiguration instance.
description:
  - 'Create, update and delete instance of Azure TenantConfiguration.'
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
      - The identifier of the Git Configuration Operation.
    required: true
    type: str
  branch:
    description:
      - The name of Git branch.
    type: str
  commit_id:
    description:
      - The latest commit Id.
    type: str
  is_export:
    description:
      - >-
        value indicating if last sync was save (true) or deploy (false)
        operation.
    type: boolean
  is_synced:
    description:
      - >-
        value indicating if last synchronization was later than the
        configuration change.
    type: boolean
  is_git_enabled:
    description:
      - value indicating whether Git configuration access is enabled.
    type: boolean
  sync_date:
    description:
      - >-
        The date of the latest synchronization. The date conforms to the
        following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.<br>
    type: datetime
  configuration_change_date:
    description:
      - >-
        The date of the latest configuration change. The date conforms to the
        following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.<br>
    type: datetime
  state:
    description:
      - Assert the state of the TenantConfiguration.
      - >-
        Use C(present) to create or update an TenantConfiguration and C(absent)
        to delete it.
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
branch:
  description:
    - The name of Git branch.
  returned: always
  type: str
  sample: null
commit_id:
  description:
    - The latest commit Id.
  returned: always
  type: str
  sample: null
is_export:
  description:
    - value indicating if last sync was save (true) or deploy (false) operation.
  returned: always
  type: boolean
  sample: null
is_synced:
  description:
    - >-
      value indicating if last synchronization was later than the configuration
      change.
  returned: always
  type: boolean
  sample: null
is_git_enabled:
  description:
    - value indicating whether Git configuration access is enabled.
  returned: always
  type: boolean
  sample: null
sync_date:
  description:
    - >-
      The date of the latest synchronization. The date conforms to the following
      format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
  returned: always
  type: datetime
  sample: null
configuration_change_date:
  description:
    - >-
      The date of the latest configuration change. The date conforms to the
      following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
      standard.<br>
  returned: always
  type: datetime
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


class AzureRMTenantConfiguration(AzureRMModuleBaseExt):
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
                disposition='configuration_name',
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
        self.name = None
        self.branch = None
        self.commit_id = None
        self.is_export = None
        self.is_synced = None
        self.is_git_enabled = None
        self.sync_date = None
        self.configuration_change_date = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTenantConfiguration, self).__init__(derived_arg_spec=self.module_arg_spec,
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
           self.results["branch"] = response["branch"]
           self.results["commit_id"] = response["commit_id"]
           self.results["is_export"] = response["is_export"]
           self.results["is_synced"] = response["is_synced"]
           self.results["is_git_enabled"] = response["is_git_enabled"]
           self.results["sync_date"] = response["sync_date"]
           self.results["configuration_change_date"] = response["configuration_change_date"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.tenant_configuration.create()
            else:
                response = self.mgmt_client.tenant_configuration.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the TenantConfiguration instance.')
            self.fail('Error creating the TenantConfiguration instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the TenantConfiguration instance {0}'.format(self.))
        try:
            response = self.mgmt_client.tenant_configuration.delete()
        except CloudError as e:
            self.log('Error attempting to delete the TenantConfiguration instance.')
            self.fail('Error deleting the TenantConfiguration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the TenantConfiguration instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.tenant_configuration.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTenantConfiguration()


if __name__ == '__main__':
    main()
