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
module: azure_rm_recoveryservicesoperation
version_added: '2.9'
short_description: Manage Azure Operation instance.
description:
  - 'Create, update and delete instance of Azure Operation.'
options:
  value:
    description:
      - List of available operations.
    type: list
    suboptions:
      name:
        description:
          - Name of the Operation.
        type: str
      display:
        description:
          - >-
            Contains the localized display information for this particular
            operation
        type: dict
        suboptions:
          provider:
            description:
              - Name of the provider for display purposes
            type: str
          resource:
            description:
              - ResourceType for which this Operation can be performed.
            type: str
          operation:
            description:
              - Operations Name itself.
            type: str
          description:
            description:
              - >-
                Description of the operation having details of what operation is
                about.
            type: str
      origin:
        description:
          - >-
            The intended executor of the operation;governs the display of the
            operation in the RBAC UX and the audit logs UX
        type: str
      service_specification:
        description:
          - Operation properties.
        type: dict
        suboptions:
          log_specifications:
            description:
              - List of log specifications of this operation.
            type: list
            suboptions:
              name:
                description:
                  - Name of the log.
                type: str
              display_name:
                description:
                  - Localized display name
                type: str
              blob_duration:
                description:
                  - Blobs created in customer storage account per hour
                type: str
  next_link:
    description:
      - Link to the next chunk of the response
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
value:
  description:
    - List of available operations.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of the Operation.
      returned: always
      type: str
      sample: null
    display:
      description:
        - >-
          Contains the localized display information for this particular
          operation
      returned: always
      type: dict
      sample: null
      contains:
        provider:
          description:
            - Name of the provider for display purposes
          returned: always
          type: str
          sample: null
        resource:
          description:
            - ResourceType for which this Operation can be performed.
          returned: always
          type: str
          sample: null
        operation:
          description:
            - Operations Name itself.
          returned: always
          type: str
          sample: null
        description:
          description:
            - >-
              Description of the operation having details of what operation is
              about.
          returned: always
          type: str
          sample: null
    origin:
      description:
        - >-
          The intended executor of the operation;governs the display of the
          operation in the RBAC UX and the audit logs UX
      returned: always
      type: str
      sample: null
    properties:
      description:
        - ShoeBox properties for the given operation.
      returned: always
      type: dict
      sample: null
    service_specification:
      description:
        - Operation properties.
      returned: always
      type: dict
      sample: null
      contains:
        log_specifications:
          description:
            - List of log specifications of this operation.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the log.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - Localized display name
              returned: always
              type: str
              sample: null
            blob_duration:
              description:
                - Blobs created in customer storage account per hour
              returned: always
              type: str
              sample: null
next_link:
  description:
    - Link to the next chunk of the response
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
    from azure.mgmt.recoveryservices import RecoveryServicesClient
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

        self.value = None
        self.next_link = None
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

        self.mgmt_client = self.get_mgmt_svc_client(RecoveryServices,
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
           self.results["value"] = response["value"]
           self.results["next_link"] = response["next_link"]

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
            response = self.mgmt_client.operations.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOperations()


if __name__ == '__main__':
    main()
