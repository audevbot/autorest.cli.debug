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
module: azure_rm_frontdoor
version_added: '2.9'
short_description: Manage Azure FrontDoor instance.
description:
  - 'Create, update and delete instance of Azure FrontDoor.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
  name:
    description:
      - Resource name.
  location:
    description:
      - Resource location.
  friendly_name:
    description:
      - A friendly name for the frontDoor
  routing_rules:
    description:
      - Routing rules associated with this Front Door.
    type: list
  load_balancing_settings:
    description:
      - Load balancing settings associated with this Front Door instance.
    type: list
  health_probe_settings:
    description:
      - Health probe settings associated with this Front Door instance.
    type: list
  backend_pools:
    description:
      - Backend pools available to routing rules.
    type: list
  frontend_endpoints:
    description:
      - Frontend endpoints available to routing rules.
    type: list
  backend_pools_settings:
    description:
      - Settings for all backendPools
  enabled_state:
    description:
      - >-
        Operational status of the Front Door load balancer. Permitted values are
        'Enabled' or 'Disabled'
  resource_state:
    description:
      - Resource status of the Front Door.
  provisioning_state:
    description:
      - Provisioning state of the Front Door.
  cname:
    description:
      - The host that each frontendEndpoint must CNAME to.
  id:
    description:
      - Resource ID.
  type:
    description:
      - Resource type.
  state:
    description:
      - Assert the state of the FrontDoor.
      - >-
        Use C(present) to create or update an FrontDoor and C(absent) to delete
        it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
  - azure_tags
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Create or update specific Front Door
  azure_rm_frontdoor:
    resource_group: myResourceGroup
    name: myFrontDoor
- name: Delete Front Door
  azure_rm_frontdoor:
    resource_group: myResourceGroup
    name: myFrontDoor
    state: absent

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
    - Resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"539","$type":"DictionaryType","valueType":{"$id":"540","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"541","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"542","fixed":false},"deprecated":false}]
  sample: null
properties:
  description:
    - Properties of the Front Door Load Balancer
  returned: always
  type: dict
  sample: null
  contains:
    friendly_name:
      description:
        - A friendly name for the frontDoor
      returned: always
      type: str
      sample: null
    routing_rules:
      description:
        - Routing rules associated with this Front Door.
      returned: always
      type: dict
      sample: null
    load_balancing_settings:
      description:
        - Load balancing settings associated with this Front Door instance.
      returned: always
      type: dict
      sample: null
    health_probe_settings:
      description:
        - Health probe settings associated with this Front Door instance.
      returned: always
      type: dict
      sample: null
    backend_pools:
      description:
        - Backend pools available to routing rules.
      returned: always
      type: dict
      sample: null
    frontend_endpoints:
      description:
        - Frontend endpoints available to routing rules.
      returned: always
      type: dict
      sample: null
    backend_pools_settings:
      description:
        - Settings for all backendPools
      returned: always
      type: dict
      sample: null
    enabled_state:
      description:
        - >-
          Operational status of the Front Door load balancer. Permitted values
          are 'Enabled' or 'Disabled'
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status of the Front Door.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the Front Door.
      returned: always
      type: str
      sample: null
    cname:
      description:
        - The host that each frontendEndpoint must CNAME to.
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


class AzureRMFrontDoors(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='frontDoorName',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            friendly_name=dict(
                type='str',
                disposition='/properties/friendlyName'
            ),
            routing_rules=dict(
                type='list',
                disposition='/properties/routingRules'
            ),
            load_balancing_settings=dict(
                type='list',
                disposition='/properties/loadBalancingSettings'
            ),
            health_probe_settings=dict(
                type='list',
                disposition='/properties/healthProbeSettings'
            ),
            backend_pools=dict(
                type='list',
                disposition='/properties/backendPools'
            ),
            frontend_endpoints=dict(
                type='list',
                disposition='/properties/frontendEndpoints'
            ),
            backend_pools_settings=dict(
                type='dict',
                disposition='/properties/backendPoolsSettings'
            ),
            enabled_state=dict(
                type='str',
                disposition='/properties/enabledState',
                choices=['Enabled',
                         'Disabled']
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
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
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

        super(AzureRMFrontDoors, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Network' +
                    '/frontDoors' +
                    '/{{ front_door_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("FrontDoor instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('FrontDoor instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the FrontDoor instance')

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
            self.log('FrontDoor instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('FrontDoor instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the FrontDoor instance {0}'.format(self.))

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
            self.log('Error attempting to create the FrontDoor instance.')
            self.fail('Error creating the FrontDoor instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the FrontDoor instance {0}'.format(self.))
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
            self.log('Error attempting to delete the FrontDoor instance.')
            self.fail('Error deleting the FrontDoor instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the FrontDoor instance {0} is present'.format(self.))
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
            # self.log("FrontDoor instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the FrontDoor instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMFrontDoors()


if __name__ == '__main__':
    main()
