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
module: azure_rm_vmwarecloudsimpleoperation
version_added: '2.9'
short_description: Manage Azure Operation instance.
description:
  - 'Create, update and delete instance of Azure Operation.'
options:
  end_time:
    description:
      - End time of the operation
    type: datetime
  error:
    description:
      - Error Message if operation failed
    type: dict
    suboptions:
      code:
        description:
          - Error's code
        type: str
      message:
        description:
          - Error's message
        type: str
  id:
    description:
      - Operation Id
    type: str
  name:
    description:
      - Operation ID
    type: str
  start_time:
    description:
      - Start time of the operation
    type: datetime
  status:
    description:
      - Operation status
    type: str
  state:
    description:
      - Assert the state of the Operation.
      - >-
        Use C(present) to create or update an Operation and C(absent) to delete
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
end_time:
  description:
    - End time of the operation
  returned: always
  type: datetime
  sample: null
error:
  description:
    - Error Message if operation failed
  returned: always
  type: dict
  sample: null
  contains:
    code:
      description:
        - Error's code
      returned: always
      type: str
      sample: null
    message:
      description:
        - Error's message
      returned: always
      type: str
      sample: null
id:
  description:
    - Operation Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Operation ID
  returned: always
  type: str
  sample: null
start_time:
  description:
    - Start time of the operation
  returned: always
  type: datetime
  sample: null
status:
  description:
    - Operation status
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
    from azure.mgmt.vmwarecloudsimple import VMwareCloudSimpleClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOperations(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            undefined,
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.end_time = None
        self.error = None
        self.id = None
        self.name = None
        self.start_time = None
        self.status = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOperations, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(VMwareCloudSimple,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

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
           self.results["end_time"] = response["end_time"]
           self.results["error"] = response["error"]
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["start_time"] = response["start_time"]
           self.results["status"] = response["status"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.operations.create()
            else:
                response = self.mgmt_client.operations.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Operation instance.')
            self.fail('Error creating the Operation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Operation instance {0}'.format(self.))
        try:
            response = self.mgmt_client.operations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Operation instance.')
            self.fail('Error deleting the Operation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Operation instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.operations.get(region_id=self.regionId,
                                                       referer=self.Referer,
                                                       operation_id=self.operationId)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOperations()


if __name__ == '__main__':
    main()
