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
module: frontdoorbackendpool
version_added: '2.9'
short_description: Manage Azure BackendPool instance.
description:
  - 'Create, update and delete instance of Azure BackendPool.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
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
  backends:
    description:
      - The set of backends for this pool
    type: list
    suboptions:
      address:
        description:
          - Location of the backend (IP address or FQDN)
        type: str
      http_port:
        description:
          - The HTTP TCP port number. Must be between 1 and 65535.
        type: number
      https_port:
        description:
          - The HTTPS TCP port number. Must be between 1 and 65535.
        type: number
      enabled_state:
        description:
          - >-
            Whether to enable use of this backend. Permitted values are
            'Enabled' or 'Disabled'
        type: str
      priority:
        description:
          - >-
            Priority to use for load balancing. Higher priorities will not be
            used for load balancing if any lower priority backend is healthy.
        type: number
      weight:
        description:
          - Weight of this endpoint for load balancing purposes.
        type: number
      backend_host_header:
        description:
          - >-
            The value to use as the host header sent to the backend. If blank or
            unspecified, this defaults to the incoming host.
        type: str
  load_balancing_settings:
    description:
      - Load balancing settings for a backend pool
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  health_probe_settings:
    description:
      - L7 health probe settings for a backend pool
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  resource_state:
    description:
      - Resource status.
    type: str
  type:
    description:
      - Resource type.
    type: str
  state:
    description:
      - Assert the state of the BackendPool.
      - >-
        Use C(present) to create or update an BackendPool and C(absent) to
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
- name: Create or update specific Backend Pool
  azure.rm.frontdoorbackendpool:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myBackendPool
    backend_pool_parameters:
      name: backendPool1
      properties:
        backends:
          - address: w3.contoso.com
            httpPort: '80'
            httpsPort: '443'
            weight: '1'
            priority: '2'
          - address: contoso.com.website-us-west-2.othercloud.net
            httpPort: '80'
            httpsPort: '443'
            weight: '2'
            priority: '1'
          - address: contoso1.azurewebsites.net
            httpPort: '80'
            httpsPort: '443'
            weight: '1'
            priority: '1'
        loadBalancingSettings:
          id: >-
            /subscriptions/{{ subscription_id }}/resourceGroups/{{
            resource_group }}/providers/Microsoft.Network/frontDoors/{{
            front_door_name }}/loadBalancingSettings/{{
            load_balancing_setting_name }}
        healthProbeSettings:
          id: >-
            /subscriptions/{{ subscription_id }}/resourceGroups/{{
            resource_group }}/providers/Microsoft.Network/frontDoors/{{
            front_door_name }}/healthProbeSettings/{{ health_probe_setting_name
            }}
- name: Delete Backend Pool
  azure.rm.frontdoorbackendpool:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myBackendPool
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties of the Front Door Backend Pool
  returned: always
  type: dict
  sample: null
  contains:
    backends:
      description:
        - The set of backends for this pool
      returned: always
      type: dict
      sample: null
      contains:
        address:
          description:
            - Location of the backend (IP address or FQDN)
          returned: always
          type: str
          sample: null
        http_port:
          description:
            - The HTTP TCP port number. Must be between 1 and 65535.
          returned: always
          type: number
          sample: null
        https_port:
          description:
            - The HTTPS TCP port number. Must be between 1 and 65535.
          returned: always
          type: number
          sample: null
        enabled_state:
          description:
            - >-
              Whether to enable use of this backend. Permitted values are
              'Enabled' or 'Disabled'
          returned: always
          type: str
          sample: null
        priority:
          description:
            - >-
              Priority to use for load balancing. Higher priorities will not be
              used for load balancing if any lower priority backend is healthy.
          returned: always
          type: number
          sample: null
        weight:
          description:
            - Weight of this endpoint for load balancing purposes.
          returned: always
          type: number
          sample: null
        backend_host_header:
          description:
            - >-
              The value to use as the host header sent to the backend. If blank
              or unspecified, this defaults to the incoming host.
          returned: always
          type: str
          sample: null
    load_balancing_settings:
      description:
        - Load balancing settings for a backend pool
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    health_probe_settings:
      description:
        - L7 health probe settings for a backend pool
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    resource_state:
      description:
        - Resource status.
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
    - Resource type.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBackendPools(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            front_door_name=dict(
                type='str',
                updatable=False,
                disposition='frontDoorName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='backendPoolName',
                required=true
            ),
            id=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            backends=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    address=dict(
                        type='str'
                    ),
                    http_port=dict(
                        type='number',
                        disposition='httpPort'
                    ),
                    https_port=dict(
                        type='number',
                        disposition='httpsPort'
                    ),
                    enabled_state=dict(
                        type='str',
                        disposition='enabledState',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    priority=dict(
                        type='number'
                    ),
                    weight=dict(
                        type='number'
                    ),
                    backend_host_header=dict(
                        type='str',
                        disposition='backendHostHeader'
                    )
                )
            ),
            load_balancing_settings=dict(
                type='dict',
                disposition='/properties/loadBalancingSettings',
                options=dict(
                    id=dict(
                        type='str'
                    )
                )
            ),
            health_probe_settings=dict(
                type='dict',
                disposition='/properties/healthProbeSettings',
                options=dict(
                    id=dict(
                        type='str'
                    )
                )
            ),
            resource_state=dict(
                type='str',
                disposition='/properties/resourceState',
                choices=['Creating',
                         'Enabling',
                         'Enabled',
                         'Disabling',
                         'Disabled',
                         'Deleting']
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.front_door_name = None
        self.name = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMBackendPools, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors' +
                    '/{{ front_door_name }}' +
                    '/backendPools' +
                    '/{{ backend_pool_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.front_door_name)
        self.url = self.url.replace('{{ backend_pool_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("BackendPool instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('BackendPool instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the BackendPool instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('BackendPool instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('BackendPool instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["properties"] = response["properties"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the BackendPool instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the BackendPool instance.')
            self.fail('Error creating the BackendPool instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the BackendPool instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the BackendPool instance.')
            self.fail('Error deleting the BackendPool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the BackendPool instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("BackendPool instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the BackendPool instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMBackendPools()


if __name__ == '__main__':
    main()
