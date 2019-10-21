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
module: cosmosdbcollectionpartition
version_added: '2.9'
short_description: Manage Azure CollectionPartition instance.
description:
  - 'Create, update and delete instance of Azure CollectionPartition.'
options:
  resource_group:
    description:
      - Name of an Azure resource group.
    required: true
    type: str
  account_name:
    description:
      - Cosmos DB database account name.
    required: true
    type: str
  database_rid:
    description:
      - Cosmos DB database rid.
    required: true
    type: str
  collection_rid:
    description:
      - Cosmos DB collection rid.
    required: true
    type: str
  value:
    description:
      - >-
        The list of partition-level usages for the database. A usage is a point
        in time metric
    type: list
    suboptions:
      unit:
        description:
          - The unit of the metric.
        type: str
      name:
        description:
          - The name information for the metric.
        type: dict
        suboptions:
          value:
            description:
              - The name of the metric.
            type: str
          localized_value:
            description:
              - The friendly name of the metric.
            type: str
      quota_period:
        description:
          - The quota period used to summarize the usage values.
        type: str
      limit:
        description:
          - Maximum value for this metric
        type: number
      current_value:
        description:
          - Current value for this metric
        type: number
      partition_id:
        description:
          - The partition id (GUID identifier) of the usages.
        type: str
      partition_key_range_id:
        description:
          - The partition key range id (integer identifier) of the usages.
        type: str
  state:
    description:
      - Assert the state of the CollectionPartition.
      - >-
        Use C(present) to create or update an CollectionPartition and C(absent)
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
value:
  description:
    - >-
      The list of partition-level usages for the database. A usage is a point in
      time metric
  returned: always
  type: dict
  sample: null
  contains:
    unit:
      description:
        - The unit of the metric.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name information for the metric.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - The name of the metric.
          returned: always
          type: str
          sample: null
        localized_value:
          description:
            - The friendly name of the metric.
          returned: always
          type: str
          sample: null
    quota_period:
      description:
        - The quota period used to summarize the usage values.
      returned: always
      type: str
      sample: null
    limit:
      description:
        - Maximum value for this metric
      returned: always
      type: number
      sample: null
    current_value:
      description:
        - Current value for this metric
      returned: always
      type: number
      sample: null
    partition_id:
      description:
        - The partition id (GUID identifier) of the usages.
      returned: always
      type: str
      sample: null
    partition_key_range_id:
      description:
        - The partition key range id (integer identifier) of the usages.
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


class AzureRMCollectionPartition(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            account_name=dict(
                type='str',
                updatable=False,
                disposition='accountName',
                required=true
            ),
            database_rid=dict(
                type='str',
                updatable=False,
                disposition='databaseRid',
                required=true
            ),
            collection_rid=dict(
                type='str',
                updatable=False,
                disposition='collectionRid',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.database_rid = None
        self.collection_rid = None
        self.value = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-04-08'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMCollectionPartition, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}' +
                    '/databases' +
                    '/{{ database_name }}' +
                    '/collections' +
                    '/{{ collection_name }}' +
                    '/partitions' +
                    '/{{ partition_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.database_account_name)
        self.url = self.url.replace('{{ database_name }}', self.database_name)
        self.url = self.url.replace('{{ collection_name }}', self.collection_name)
        self.url = self.url.replace('{{ partition_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("CollectionPartition instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('CollectionPartition instance already exists')

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
            self.log('Need to Create / Update the CollectionPartition instance')

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
            self.log('CollectionPartition instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('CollectionPartition instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["value"] = response["value"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the CollectionPartition instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the CollectionPartition instance.')
            self.fail('Error creating the CollectionPartition instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the CollectionPartition instance {0}'.format(self.))
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
            self.log('Error attempting to delete the CollectionPartition instance.')
            self.fail('Error deleting the CollectionPartition instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the CollectionPartition instance {0} is present'.format(self.))
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
            # self.log("CollectionPartition instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the CollectionPartition instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMCollectionPartition()


if __name__ == '__main__':
    main()
