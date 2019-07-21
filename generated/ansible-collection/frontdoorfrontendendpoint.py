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
module: frontdoorfrontendendpoint
version_added: '2.9'
short_description: Manage Azure FrontendEndpoint instance.
description:
  - 'Create, update and delete instance of Azure FrontendEndpoint.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
  front_door_name:
    description:
      - Name of the Front Door which is globally unique.
    required: true
  name:
    description:
      - Resource name.
  id:
    description:
      - Resource ID.
  host_name:
    description:
      - The host name of the frontendEndpoint. Must be a domain name.
  session_affinity_enabled_state:
    description:
      - >-
        Whether to allow session affinity on this host. Valid options are
        'Enabled' or 'Disabled'
  session_affinity_ttl_seconds:
    description:
      - >-
        UNUSED. This field will be ignored. The TTL to use in seconds for
        session affinity, if applicable.
  web_application_firewall_policy_link:
    description:
      - >-
        Defines the Web Application Firewall policy for each host (if
        applicable)
    suboptions:
      id:
        description:
          - Resource ID.
  resource_state:
    description:
      - Resource status.
  custom_https_provisioning_state:
    description:
      - Provisioning status of Custom Https of the frontendEndpoint.
  custom_https_provisioning_substate:
    description:
      - >-
        Provisioning substate shows the progress of custom HTTPS
        enabling/disabling process step by step.
  custom_https_configuration:
    description:
      - The configuration specifying how to enable HTTPS
    suboptions:
      certificate_source:
        description:
          - Defines the source of the SSL certificate
      protocol_type:
        description:
          - Defines the TLS extension protocol that is used for secure delivery
      key_vault_certificate_source_parameters:
        description:
          - >-
            KeyVault certificate source parameters (if
            certificateSource=AzureKeyVault)
        suboptions:
          vault:
            description:
              - The Key Vault containing the SSL certificate
            suboptions:
              id:
                description:
                  - Resource ID.
          secret_name:
            description:
              - >-
                The name of the Key Vault secret representing the full
                certificate PFX
          secret_version:
            description:
              - >-
                The version of the Key Vault secret representing the full
                certificate PFX
      front_door_certificate_source_parameters:
        description:
          - >-
            Parameters required for enabling SSL with Front Door-managed
            certificates (if certificateSource=FrontDoor)
        suboptions:
          certificate_type:
            description:
              - >-
                Defines the type of the certificate used for secure connections
                to a frontendEndpoint
  type:
    description:
      - Resource type.
  state:
    description:
      - Assert the state of the FrontendEndpoint.
      - >-
        Use C(present) to create or update an FrontendEndpoint and C(absent) to
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
- name: Create or update specific Frontend Endpoint
  azure.rm.frontdoorfrontendendpoint:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myFrontendEndpoint
    frontend_endpoint_parameters:
      name: frontendEndpoint1
      properties:
        hostName: www.contoso.com
        sessionAffinityEnabledState: Enabled
        sessionAffinityTtlSeconds: '60'
        webApplicationFirewallPolicyLink:
          id: >-
            /subscriptions/{{ subscription_id }}/resourceGroups/{{
            resource_group
            }}/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/{{
            front_door_web_application_firewall_policy_name }}
- name: Delete Backend Pool
  azure.rm.frontdoorfrontendendpoint:
    resource_group: myResourceGroup
    front_door_name: myFrontDoor
    name: myFrontendEndpoint
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
    - Properties of the Frontend endpoint
  returned: always
  type: dict
  sample: null
  contains:
    host_name:
      description:
        - The host name of the frontendEndpoint. Must be a domain name.
      returned: always
      type: str
      sample: null
    session_affinity_enabled_state:
      description:
        - >-
          Whether to allow session affinity on this host. Valid options are
          'Enabled' or 'Disabled'
      returned: always
      type: str
      sample: null
    session_affinity_ttl_seconds:
      description:
        - >-
          UNUSED. This field will be ignored. The TTL to use in seconds for
          session affinity, if applicable.
      returned: always
      type: number
      sample: null
    web_application_firewall_policy_link:
      description:
        - >-
          Defines the Web Application Firewall policy for each host (if
          applicable)
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
    custom_https_provisioning_state:
      description:
        - Provisioning status of Custom Https of the frontendEndpoint.
      returned: always
      type: str
      sample: null
    custom_https_provisioning_substate:
      description:
        - >-
          Provisioning substate shows the progress of custom HTTPS
          enabling/disabling process step by step.
      returned: always
      type: str
      sample: null
    custom_https_configuration:
      description:
        - The configuration specifying how to enable HTTPS
      returned: always
      type: dict
      sample: null
      contains:
        certificate_source:
          description:
            - Defines the source of the SSL certificate
          returned: always
          type: str
          sample: null
        protocol_type:
          description:
            - >-
              Defines the TLS extension protocol that is used for secure
              delivery
          returned: always
          type: str
          sample: null
        key_vault_certificate_source_parameters:
          description:
            - >-
              KeyVault certificate source parameters (if
              certificateSource=AzureKeyVault)
          returned: always
          type: dict
          sample: null
          contains:
            vault:
              description:
                - The Key Vault containing the SSL certificate
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
            secret_name:
              description:
                - >-
                  The name of the Key Vault secret representing the full
                  certificate PFX
              returned: always
              type: str
              sample: null
            secret_version:
              description:
                - >-
                  The version of the Key Vault secret representing the full
                  certificate PFX
              returned: always
              type: str
              sample: null
        front_door_certificate_source_parameters:
          description:
            - >-
              Parameters required for enabling SSL with Front Door-managed
              certificates (if certificateSource=FrontDoor)
          returned: always
          type: dict
          sample: null
          contains:
            certificate_type:
              description:
                - >-
                  Defines the type of the certificate used for secure
                  connections to a frontendEndpoint
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


class AzureRMFrontendEndpoints(AzureRMModuleBaseExt):
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
                disposition='frontendEndpointName',
                required=true
            ),
            id=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            host_name=dict(
                type='str',
                disposition='/properties/hostName'
            ),
            session_affinity_enabled_state=dict(
                type='str',
                disposition='/properties/sessionAffinityEnabledState',
                choices=['Enabled',
                         'Disabled']
            ),
            session_affinity_ttl_seconds=dict(
                type='number',
                disposition='/properties/sessionAffinityTtlSeconds'
            ),
            web_application_firewall_policy_link=dict(
                type='dict',
                disposition='/properties/webApplicationFirewallPolicyLink',
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

        super(AzureRMFrontendEndpoints, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/frontendEndpoints' +
                    '/{{ frontend_endpoint_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ front_door_name }}', self.front_door_name)
        self.url = self.url.replace('{{ frontend_endpoint_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("FrontendEndpoint instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('FrontendEndpoint instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the FrontendEndpoint instance')

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
            self.log('FrontendEndpoint instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('FrontendEndpoint instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["properties"] = response["properties"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the FrontendEndpoint instance {0}'.format(self.))

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
            self.log('Error attempting to create the FrontendEndpoint instance.')
            self.fail('Error creating the FrontendEndpoint instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the FrontendEndpoint instance {0}'.format(self.))
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
            self.log('Error attempting to delete the FrontendEndpoint instance.')
            self.fail('Error deleting the FrontendEndpoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the FrontendEndpoint instance {0} is present'.format(self.))
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
            # self.log("FrontendEndpoint instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the FrontendEndpoint instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMFrontendEndpoints()


if __name__ == '__main__':
    main()
