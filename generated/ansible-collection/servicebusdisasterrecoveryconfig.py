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
module: servicebusdisasterrecoveryconfig
version_added: '2.9'
short_description: Manage Azure DisasterRecoveryConfig instance.
description:
  - 'Create, update and delete instance of Azure DisasterRecoveryConfig.'
options:
  resource_group:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
  alias:
    description:
      - The Disaster Recovery configuration name
    required: true
    type: str
  partner_namespace:
    description:
      - >-
        ARM Id of the Primary/Secondary eventhub namespace name, which is part
        of GEO DR pairing
    type: str
  alternate_name:
    description:
      - >-
        Primary/Secondary eventhub namespace name, which is part of GEO DR
        pairing
    type: str
  provisioning_state:
    description:
      - >-
        Provisioning state of the Alias(Disaster Recovery configuration) -
        possible values 'Accepted' or 'Succeeded' or 'Failed'
    type: str
  pending_replication_operations_count:
    description:
      - Number of entities pending to be replicated.
    type: number
  role:
    description:
      - >-
        role of namespace in GEO DR - possible values 'Primary' or
        'PrimaryNotReplicating' or 'Secondary'
    type: str
  id:
    description:
      - Resource Id
    type: str
  name:
    description:
      - Resource name
    type: str
  type:
    description:
      - Resource type
    type: str
  state:
    description:
      - Assert the state of the DisasterRecoveryConfig.
      - >-
        Use C(present) to create or update an DisasterRecoveryConfig and
        C(absent) to delete it.
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
- name: SBAliasCreate
  azure.rm.servicebusdisasterrecoveryconfig:
    resource_group: myResourceGroup
    namespace_name: my
    alias: myDisasterRecoveryConfig
    partner_namespace: sdk-Namespace-37
    alternate_name: alternameforAlias-Namespace-8860
- name: SBAliasDelete
  azure.rm.servicebusdisasterrecoveryconfig:
    resource_group: myResourceGroup
    namespace_name: my
    alias: myDisasterRecoveryConfig
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
properties:
  description:
    - >-
      Properties required to the Create Or Update Alias(Disaster Recovery
      configurations)
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_state:
      description:
        - >-
          Provisioning state of the Alias(Disaster Recovery configuration) -
          possible values 'Accepted' or 'Succeeded' or 'Failed'
      returned: always
      type: str
      sample: null
    pending_replication_operations_count:
      description:
        - Number of entities pending to be replicated.
      returned: always
      type: number
      sample: null
    partner_namespace:
      description:
        - >-
          ARM Id of the Primary/Secondary eventhub namespace name, which is part
          of GEO DR pairing
      returned: always
      type: str
      sample: null
    alternate_name:
      description:
        - >-
          Primary/Secondary eventhub namespace name, which is part of GEO DR
          pairing
      returned: always
      type: str
      sample: null
    role:
      description:
        - >-
          role of namespace in GEO DR - possible values 'Primary' or
          'PrimaryNotReplicating' or 'Secondary'
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
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDisasterRecoveryConfigs(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            namespace_name=dict(
                type='str',
                updatable=False,
                disposition='namespaceName',
                required=true
            ),
            alias=dict(
                type='str',
                updatable=False,
                required=true
            ),
            partner_namespace=dict(
                type='str',
                disposition='/properties/partnerNamespace'
            ),
            alternate_name=dict(
                type='str',
                disposition='/properties/alternateName'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.namespace_name = None
        self.alias = None
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
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMDisasterRecoveryConfigs, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/Microsoft.ServiceBus' +
                    '/namespaces' +
                    '/{{ namespace_name }}' +
                    '/disasterRecoveryConfigs' +
                    '/{{ disaster_recovery_config_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ namespace_name }}', self.namespace_name)
        self.url = self.url.replace('{{ disaster_recovery_config_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("DisasterRecoveryConfig instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('DisasterRecoveryConfig instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the DisasterRecoveryConfig instance')

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
            self.log('DisasterRecoveryConfig instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('DisasterRecoveryConfig instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the DisasterRecoveryConfig instance {0}'.format(self.))

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
            self.log('Error attempting to create the DisasterRecoveryConfig instance.')
            self.fail('Error creating the DisasterRecoveryConfig instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the DisasterRecoveryConfig instance {0}'.format(self.))
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
            self.log('Error attempting to delete the DisasterRecoveryConfig instance.')
            self.fail('Error deleting the DisasterRecoveryConfig instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the DisasterRecoveryConfig instance {0} is present'.format(self.))
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
            # self.log("DisasterRecoveryConfig instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DisasterRecoveryConfig instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMDisasterRecoveryConfigs()


if __name__ == '__main__':
    main()
