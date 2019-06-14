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
module: azure_rm_managementgroup
version_added: '2.9'
short_description: Manage Azure ManagementGroup instance.
description:
  - 'Create, update and delete instance of Azure ManagementGroup.'
options:
  group_id:
    description:
      - Management Group ID.
    required: true
  create_management_group_request:
    description:
      - Management group creation parameters.
    required: true
  name:
    description:
      - >-
        The name of the management group. For example,
        00000000-0000-0000-0000-000000000000
  display_name:
    description:
      - >-
        The friendly name of the management group. If no value is passed then
        this  field will be set to the groupId.
  details:
    description:
      - undefined
    suboptions:
      parent:
        description:
          - undefined
        suboptions:
          id:
            description:
              - >-
                The fully qualified ID for the parent management group.  For
                example,
                /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
          name:
            description:
              - The name of the parent management group
          display_name:
            description:
              - The friendly name of the parent management group.
      version:
        description:
          - The version number of the object.
      updated_time:
        description:
          - The date and time when this object was last updated.
      updated_by:
        description:
          - The identity of the principal or process that updated the object.
  tenant_id:
    description:
      - >-
        The AAD Tenant ID associated with the management group. For example,
        00000000-0000-0000-0000-000000000000
  roles:
    description:
      - The role definitions associated with the management group.
    type: list
  children:
    description:
      - The list of children.
    type: list
    suboptions:
      type:
        description:
          - >-
            The fully qualified resource type which includes provider namespace
            (e.g. /providers/Microsoft.Management/managementGroups)
      id:
        description:
          - >-
            The fully qualified ID for the child resource (management group or
            subscription).  For example,
            /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
      name:
        description:
          - The name of the child entity.
      display_name:
        description:
          - The friendly name of the child resource.
      roles:
        description:
          - The roles definitions associated with the management group.
        type: list
      children:
        description:
          - The list of children.
        type: list
        suboptions:
          type:
            description:
              - >-
                The fully qualified resource type which includes provider
                namespace (e.g.
                /providers/Microsoft.Management/managementGroups)
          id:
            description:
              - >-
                The fully qualified ID for the child resource (management group
                or subscription).  For example,
                /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
          name:
            description:
              - The name of the child entity.
          display_name:
            description:
              - The friendly name of the child resource.
          roles:
            description:
              - The roles definitions associated with the management group.
            type: list
          children:
            description:
              - The list of children.
            type: list
            suboptions:
              type:
                description:
                  - >-
                    The fully qualified resource type which includes provider
                    namespace (e.g.
                    /providers/Microsoft.Management/managementGroups)
              id:
                description:
                  - >-
                    The fully qualified ID for the child resource (management
                    group or subscription).  For example,
                    /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
              name:
                description:
                  - The name of the child entity.
              display_name:
                description:
                  - The friendly name of the child resource.
              roles:
                description:
                  - The roles definitions associated with the management group.
                type: list
              children:
                description:
                  - The list of children.
                type: list
  id:
    description:
      - >-
        The fully qualified ID for the management group.  For example,
        /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
  type:
    description:
      - >-
        The type of the resource.  For example,
        /providers/Microsoft.Management/managementGroups
  state:
    description:
      - Assert the state of the ManagementGroup.
      - >-
        Use C(present) to create or update an ManagementGroup and C(absent) to
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
- name: PutManagementGroup
  azure_rm_managementgroup:
    group_id: myManagementGroup
    create_management_group_request:
      id: /providers/Microsoft.Management/managementGroups/ChildGroup
      type: /providers/Microsoft.Management/managementGroups
      name: ChildGroup
      properties:
        tenantId: 20000000-0000-0000-0000-000000000000
        displayName: ChildGroup
        details:
          parent:
            id: /providers/Microsoft.Management/managementGroups/RootGroup
- name: PatchManagementGroup
  azure_rm_managementgroup:
    group_id: myManagementGroup
- name: DeleteManagementGroup
  azure_rm_managementgroup:
    group_id: myManagementGroup
    state: absent

'''

RETURN = '''
id:
  description:
    - >-
      The fully qualified ID for the management group.  For example,
      /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource.  For example,
      /providers/Microsoft.Management/managementGroups
  returned: always
  type: str
  sample: null
name:
  description:
    - >-
      The name of the management group. For example,
      00000000-0000-0000-0000-000000000000
  returned: always
  type: str
  sample: null
properties:
  description:
    - !<tag:yaml.org,2002:js/undefined> ''
  returned: always
  type: dict
  sample: null
  contains:
    tenant_id:
      description:
        - >-
          The AAD Tenant ID associated with the management group. For example,
          00000000-0000-0000-0000-000000000000
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - The friendly name of the management group.
      returned: always
      type: str
      sample: null
    roles:
      description:
        - The role definitions associated with the management group.
      returned: always
      type: str
      sample: null
    details:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        version:
          description:
            - The version number of the object.
          returned: always
          type: number
          sample: null
        updated_time:
          description:
            - The date and time when this object was last updated.
          returned: always
          type: datetime
          sample: null
        updated_by:
          description:
            - The identity of the principal or process that updated the object.
          returned: always
          type: str
          sample: null
        parent:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - >-
                  The fully qualified ID for the parent management group.  For
                  example,
                  /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the parent management group
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The friendly name of the parent management group.
              returned: always
              type: str
              sample: null
    children:
      description:
        - The list of children.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - >-
              The fully qualified resource type which includes provider
              namespace (e.g. /providers/Microsoft.Management/managementGroups)
          returned: always
          type: str
          sample: null
        id:
          description:
            - >-
              The fully qualified ID for the child resource (management group or
              subscription).  For example,
              /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the child entity.
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - The friendly name of the child resource.
          returned: always
          type: str
          sample: null
        roles:
          description:
            - The roles definitions associated with the management group.
          returned: always
          type: str
          sample: null
        children:
          description:
            - The list of children.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - >-
                  The fully qualified resource type which includes provider
                  namespace (e.g.
                  /providers/Microsoft.Management/managementGroups)
              returned: always
              type: str
              sample: null
            id:
              description:
                - >-
                  The fully qualified ID for the child resource (management
                  group or subscription).  For example,
                  /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the child entity.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - The friendly name of the child resource.
              returned: always
              type: str
              sample: null
            roles:
              description:
                - The roles definitions associated with the management group.
              returned: always
              type: str
              sample: null
            children:
              description:
                - The list of children.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - >-
                      The fully qualified resource type which includes provider
                      namespace (e.g.
                      /providers/Microsoft.Management/managementGroups)
                  returned: always
                  type: str
                  sample: null
                id:
                  description:
                    - >-
                      The fully qualified ID for the child resource (management
                      group or subscription).  For example,
                      /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The name of the child entity.
                  returned: always
                  type: str
                  sample: null
                display_name:
                  description:
                    - The friendly name of the child resource.
                  returned: always
                  type: str
                  sample: null
                roles:
                  description:
                    - >-
                      The roles definitions associated with the management
                      group.
                  returned: always
                  type: str
                  sample: null
                children:
                  description:
                    - The list of children.
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
    from azure.mgmt.managementgroups import ManagementGroupsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagementGroups(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            group_id=dict(
                type='str',
                updatable=False,
                required=true
            ),
            create_management_group_request=dict(
                type='dict',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            display_name=dict(
                type='str',
                disposition='/'
            ),
            details=dict(
                type='dict',
                disposition='/',
                options=dict(
                    parent=dict(
                        type='dict',
                        options=dict(
                            id=dict(
                                type='str'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.group_id = None
        self.create_management_group_request = None
        self.id = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMManagementGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ManagementGroupsClient,
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
           self.results["id"] = response["id"]
           self.results["type"] = response["type"]
           self.results["name"] = response["name"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.management_groups.create_or_update(group_id=self.group_id,
                                                                           create_management_group_request=self.create_management_group_request)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ManagementGroup instance.')
            self.fail('Error creating the ManagementGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the ManagementGroup instance {0}'.format(self.))
        try:
            response = self.mgmt_client.management_groups.delete(group_id=self.group_id)
        except CloudError as e:
            self.log('Error attempting to delete the ManagementGroup instance.')
            self.fail('Error deleting the ManagementGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ManagementGroup instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.management_groups.get(group_id=self.group_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMManagementGroups()


if __name__ == '__main__':
    main()
