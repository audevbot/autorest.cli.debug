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
module: azure_rm_managementgroup_info
version_added: '2.9'
short_description: Get ManagementGroup info.
description:
  - Get info of ManagementGroup.
options:
  group_id:
    description:
      - Management Group ID.
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
  name:
    description:
      - >-
        The name of the management group. For example,
        00000000-0000-0000-0000-000000000000
  tenant_id:
    description:
      - >-
        The AAD Tenant ID associated with the management group. For example,
        00000000-0000-0000-0000-000000000000
  display_name:
    description:
      - The friendly name of the management group.
  roles:
    description:
      - The role definitions associated with the management group.
    type: list
  details:
    description:
      - undefined
    suboptions:
      version:
        description:
          - The version number of the object.
      updated_time:
        description:
          - The date and time when this object was last updated.
      updated_by:
        description:
          - The identity of the principal or process that updated the object.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListManagementGroups
  azure_rm_managementgroup_info: {}
- name: GetManagementGroup
  azure_rm_managementgroup_info:
    group_id: myManagementGroup
- name: GetManagementGroupWithExpand
  azure_rm_managementgroup_info:
    group_id: myManagementGroup
- name: GetManagementGroupsWithExpandAndRecurse
  azure_rm_managementgroup_info:
    group_id: myManagementGroup

'''

RETURN = '''
management_groups:
  description: >-
    A list of dict results where the key is the name of the ManagementGroup and
    the values are the facts for that ManagementGroup.
  returned: always
  type: complex
  contains:
    managementgroup_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
            - ''
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


class AzureRMManagementGroupsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            group_id=dict(
                type='str'
            )
        )

        self.group_id = None
        self.id = None
        self.type = None
        self.name = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagementGroupsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.group_id is not None):
            self.results['management_groups'] = self.format_item(self.get())
        else:
            self.results['management_groups'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/providers' +
                    '/Microsoft.Management' +
                    '/managementGroups' +
                    '/{{ management_group_name }}')
        self.url = self.url.replace('{{ management_group_name }}', self.name)

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
                    '/Microsoft.Management' +
                    '/managementGroups')
        self.url = self.url.replace('{{ management_group_name }}', self.name)

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
    AzureRMManagementGroupsInfo()


if __name__ == '__main__':
    main()
