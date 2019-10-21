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
module: azure_rm_frontdoorfrontendendpoint
version_added: '2.9'
short_description: Manage Azure FrontendEndpoint instance.
description:
  - 'Create, update and delete instance of Azure FrontendEndpoint.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
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
  host_name:
    description:
      - The host name of the frontendEndpoint. Must be a domain name.
    type: str
  session_affinity_enabled_state:
    description:
      - >-
        Whether to allow session affinity on this host. Valid options are
        'Enabled' or 'Disabled'
    type: str
  session_affinity_ttl_seconds:
    description:
      - >-
        UNUSED. This field will be ignored. The TTL to use in seconds for
        session affinity, if applicable.
    type: number
  web_application_firewall_policy_link:
    description:
      - >-
        Defines the Web Application Firewall policy for each host (if
        applicable)
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
  custom_https_provisioning_state:
    description:
      - Provisioning status of Custom Https of the frontendEndpoint.
    type: str
  custom_https_provisioning_substate:
    description:
      - >-
        Provisioning substate shows the progress of custom HTTPS
        enabling/disabling process step by step.
    type: str
  custom_https_configuration:
    description:
      - The configuration specifying how to enable HTTPS
    type: dict
    suboptions:
      certificate_source:
        description:
          - Defines the source of the SSL certificate
        type: str
      protocol_type:
        description:
          - Defines the TLS extension protocol that is used for secure delivery
        type: str
      key_vault_certificate_source_parameters:
        description:
          - >-
            KeyVault certificate source parameters (if
            certificateSource=AzureKeyVault)
        type: dict
        suboptions:
          vault:
            description:
              - The Key Vault containing the SSL certificate
            type: dict
            suboptions:
              id:
                description:
                  - Resource ID.
                type: str
          secret_name:
            description:
              - >-
                The name of the Key Vault secret representing the full
                certificate PFX
            type: str
          secret_version:
            description:
              - >-
                The version of the Key Vault secret representing the full
                certificate PFX
            type: str
      front_door_certificate_source_parameters:
        description:
          - >-
            Parameters required for enabling SSL with Front Door-managed
            certificates (if certificateSource=FrontDoor)
        type: dict
        suboptions:
          certificate_type:
            description:
              - >-
                Defines the type of the certificate used for secure connections
                to a frontendEndpoint
            type: str
  type:
    description:
      - Resource type.
    type: str
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
[]

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
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.frontdoor import FrontdoorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFrontendEndpoints(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='front_door_name',
                required=true
            ),
            host_name=dict(
                type='str',
                disposition='/'
            ),
            session_affinity_enabled_state=dict(
                type='str',
                disposition='/',
                choices=['Enabled',
                         'Disabled']
            ),
            session_affinity_ttl_seconds=dict(
                type='number',
                disposition='/'
            ),
            web_application_firewall_policy_link=dict(
                type='dict',
                disposition='/',
                options=dict(
                    id=dict(
                        type='str'
                    )
                )
            ),
            resource_state=dict(
                type='str',
                disposition='/',
                choices=['Creating',
                         'Enabling',
                         'Enabled',
                         'Disabling',
                         'Disabled',
                         'Deleting']
            ),
            custom_https_provisioning_state=dict(
                type='str',
                disposition='/',
                choices=['Enabling',
                         'Enabled',
                         'Disabling',
                         'Disabled',
                         'Failed']
            ),
            custom_https_provisioning_substate=dict(
                type='str',
                disposition='/',
                choices=['SubmittingDomainControlValidationRequest',
                         'PendingDomainControlValidationREquestApproval',
                         'DomainControlValidationRequestApproved',
                         'DomainControlValidationRequestRejected',
                         'DomainControlValidationRequestTimedOut',
                         'IssuingCertificate',
                         'DeployingCertificate',
                         'CertificateDeployed',
                         'DeletingCertificate',
                         'CertificateDeleted']
            ),
            custom_https_configuration=dict(
                type='dict',
                disposition='/',
                options=dict(
                    certificate_source=dict(
                        type='str',
                        choices=['AzureKeyVault',
                                 'FrontDoor']
                    ),
                    protocol_type=dict(
                        type='str',
                        choices=['ServerNameIndication']
                    ),
                    key_vault_certificate_source_parameters=dict(
                        type='dict',
                        options=dict(
                            vault=dict(
                                type='dict',
                                options=dict(
                                    id=dict(
                                        type='str'
                                    )
                                )
                            ),
                            secret_name=dict(
                                type='str'
                            ),
                            secret_version=dict(
                                type='str'
                            )
                        )
                    ),
                    front_door_certificate_source_parameters=dict(
                        type='dict',
                        options=dict(
                            certificate_type=dict(
                                type='str',
                                choices=['Dedicated']
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

        self.resource_group = None
        self.name = None
        self.id = None
        self.properties = None
        self.name = None
        self.type = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

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

        self.mgmt_client = self.get_mgmt_svc_client(FrontdoorClient,
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
           self.results["properties"] = response["properties"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.frontend_endpoints.create()
            else:
                response = self.mgmt_client.frontend_endpoints.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the FrontendEndpoint instance.')
            self.fail('Error creating the FrontendEndpoint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the FrontendEndpoint instance {0}'.format(self.))
        try:
            response = self.mgmt_client.frontend_endpoints.delete()
        except CloudError as e:
            self.log('Error attempting to delete the FrontendEndpoint instance.')
            self.fail('Error deleting the FrontendEndpoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the FrontendEndpoint instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.frontend_endpoints.get(resource_group_name=self.resource_group,
                                                               front_door_name=self.name,
                                                               frontend_endpoint_name=self.frontendEndpointName)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFrontendEndpoints()


if __name__ == '__main__':
    main()
