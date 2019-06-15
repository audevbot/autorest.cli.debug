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
module: azure_rm_cosmosdbdatabaseaccount
version_added: '2.9'
short_description: Manage Azure DatabaseAccount instance.
description:
  - 'Create, update and delete instance of Azure DatabaseAccount.'
options:
  resource_group:
    description:
      - Name of an Azure resource group.
    required: true
  name:
    description:
      - The name of the database account.
  location:
    description:
      - The location of the resource group to which the resource belongs.
  kind:
    description:
      - >-
        Indicates the type of database account. This can only be set at database
        account creation.
  consistency_policy:
    description:
      - The consistency policy for the Cosmos DB account.
    suboptions:
      default_consistency_level:
        description:
          - >-
            The default consistency level and configuration settings of the
            Cosmos DB account.
        required: true
      max_staleness_prefix:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the number of stale requests tolerated. Accepted range
            for this value is 1 – 2,147,483,647. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
      max_interval_in_seconds:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the time amount of staleness (in seconds) tolerated.
            Accepted range for this value is 5 - 86400. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
  locations:
    description:
      - >-
        An array that contains the georeplication locations enabled for the
        Cosmos DB account.
    required: true
    type: list
    suboptions:
      location_name:
        description:
          - The name of the region.
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  database_account_offer_type:
    description:
      - The offer type for the database
    required: true
  ip_range_filter:
    description:
      - >-
        Cosmos DB Firewall Support: This value specifies the set of IP addresses
        or IP address ranges in CIDR form to be included as the allowed list of
        client IPs for a given database account. IP addresses/ranges must be
        comma separated and must not contain any spaces.
  is_virtual_network_filter_enabled:
    description:
      - Flag to indicate whether to enable/disable Virtual Network ACL rules.
  enable_automatic_failover:
    description:
      - >-
        Enables automatic failover of the write region in the rare event that
        the region is unavailable due to an outage. Automatic failover will
        result in a new write region for the account and is chosen based on the
        failover priorities configured for the account.
  capabilities:
    description:
      - List of Cosmos DB capabilities for the account
    type: list
    suboptions:
      name:
        description:
          - >-
            Name of the Cosmos DB capability. For example, "name":
            "EnableCassandra". Current values also include "EnableTable" and
            "EnableGremlin".
  virtual_network_rules:
    description:
      - List of Virtual Network ACL rules configured for the Cosmos DB account.
    type: list
    suboptions:
      id:
        description:
          - >-
            Resource ID of a subnet, for example:
            /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
      ignore_missing_vnet_service_endpoint:
        description:
          - >-
            Create firewall rule before the virtual network has vnet service
            endpoint enabled.
  enable_multiple_write_locations:
    description:
      - Enables the account to write in multiple locations
  provisioning_state:
    description:
      - undefined
  document_endpoint:
    description:
      - The connection endpoint for the Cosmos DB database account.
  write_locations:
    description:
      - An array that contains the write location for the Cosmos DB account.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region within the database account.
            Example: &lt;accountName&gt;-&lt;locationName&gt;.
      location_name:
        description:
          - The name of the region.
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
      provisioning_state:
        description:
          - undefined
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  read_locations:
    description:
      - >-
        An array that contains of the read locations enabled for the Cosmos DB
        account.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region within the database account.
            Example: &lt;accountName&gt;-&lt;locationName&gt;.
      location_name:
        description:
          - The name of the region.
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
      provisioning_state:
        description:
          - undefined
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  failover_policies:
    description:
      - An array that contains the regions ordered by their failover priorities.
    type: list
    suboptions:
      id:
        description:
          - >-
            The unique identifier of the region in which the database account
            replicates to. Example: &lt;accountName&gt;-&lt;locationName&gt;.
      location_name:
        description:
          - The name of the region in which the database account exists.
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
  id:
    description:
      - The unique resource identifier of the database account.
  type:
    description:
      - The type of Azure resource.
  state:
    description:
      - Assert the state of the DatabaseAccount.
      - >-
        Use C(present) to create or update an DatabaseAccount and C(absent) to
        delete it.
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
- name: CosmosDBDatabaseAccountCreateMin
  azure_rm_cosmosdbdatabaseaccount:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBDatabaseAccountCreateMax
  azure_rm_cosmosdbdatabaseaccount:
    resource_group: myResourceGroup
    name: myDatabaseAccount
- name: CosmosDBDatabaseAccountDelete
  azure_rm_cosmosdbdatabaseaccount:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    state: absent

'''

RETURN = '''
id:
  description:
    - The unique resource identifier of the database account.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the database account.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of Azure resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource group to which the resource belongs.
  returned: always
  type: str
  sample: null
tags:
  description:
    - !<tag:yaml.org,2002:js/undefined> ''
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"229","$type":"DictionaryType","valueType":{"$id":"230","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"231","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"232","fixed":false},"deprecated":false}]
  sample: null
kind:
  description:
    - >-
      Indicates the type of database account. This can only be set at database
      account creation.
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
    provisioning_state:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: str
      sample: null
    document_endpoint:
      description:
        - The connection endpoint for the Cosmos DB database account.
      returned: always
      type: str
      sample: null
    database_account_offer_type:
      description:
        - >-
          The offer type for the Cosmos DB database account. Default value:
          Standard.
      returned: always
      type: str
      sample: null
    ip_range_filter:
      description:
        - >-
          Cosmos DB Firewall Support: This value specifies the set of IP
          addresses or IP address ranges in CIDR form to be included as the
          allowed list of client IPs for a given database account. IP
          addresses/ranges must be comma separated and must not contain any
          spaces.
      returned: always
      type: str
      sample: null
    is_virtual_network_filter_enabled:
      description:
        - Flag to indicate whether to enable/disable Virtual Network ACL rules.
      returned: always
      type: boolean
      sample: null
    enable_automatic_failover:
      description:
        - >-
          Enables automatic failover of the write region in the rare event that
          the region is unavailable due to an outage. Automatic failover will
          result in a new write region for the account and is chosen based on
          the failover priorities configured for the account.
      returned: always
      type: boolean
      sample: null
    consistency_policy:
      description:
        - The consistency policy for the Cosmos DB database account.
      returned: always
      type: dict
      sample: null
      contains:
        default_consistency_level:
          description:
            - >-
              The default consistency level and configuration settings of the
              Cosmos DB account.
          returned: always
          type: str
          sample: null
        max_staleness_prefix:
          description:
            - >-
              When used with the Bounded Staleness consistency level, this value
              represents the number of stale requests tolerated. Accepted range
              for this value is 1 – 2,147,483,647. Required when
              defaultConsistencyPolicy is set to 'BoundedStaleness'.
          returned: always
          type: number
          sample: null
        max_interval_in_seconds:
          description:
            - >-
              When used with the Bounded Staleness consistency level, this value
              represents the time amount of staleness (in seconds) tolerated.
              Accepted range for this value is 5 - 86400. Required when
              defaultConsistencyPolicy is set to 'BoundedStaleness'.
          returned: always
          type: number
          sample: null
    capabilities:
      description:
        - List of Cosmos DB capabilities for the account
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              Name of the Cosmos DB capability. For example, "name":
              "EnableCassandra". Current values also include "EnableTable" and
              "EnableGremlin".
          returned: always
          type: str
          sample: null
    write_locations:
      description:
        - An array that contains the write location for the Cosmos DB account.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region within the database account.
              Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region.
          returned: always
          type: str
          sample: null
        document_endpoint:
          description:
            - >-
              The connection endpoint for the specific region. Example:
              https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: number
          sample: null
    read_locations:
      description:
        - >-
          An array that contains of the read locations enabled for the Cosmos DB
          account.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region within the database account.
              Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region.
          returned: always
          type: str
          sample: null
        document_endpoint:
          description:
            - >-
              The connection endpoint for the specific region. Example:
              https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: number
          sample: null
    failover_policies:
      description:
        - >-
          An array that contains the regions ordered by their failover
          priorities.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              The unique identifier of the region in which the database account
              replicates to. Example: &lt;accountName&gt;-&lt;locationName&gt;.
          returned: always
          type: str
          sample: null
        location_name:
          description:
            - The name of the region in which the database account exists.
          returned: always
          type: str
          sample: null
        failover_priority:
          description:
            - >-
              The failover priority of the region. A failover priority of 0
              indicates a write region. The maximum value for a failover
              priority = (total number of regions - 1). Failover priority values
              must be unique for each of the regions in which the database
              account exists.
          returned: always
          type: number
          sample: null
    virtual_network_rules:
      description:
        - >-
          List of Virtual Network ACL rules configured for the Cosmos DB
          account.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - >-
              Resource ID of a subnet, for example:
              /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}.
          returned: always
          type: str
          sample: null
        ignore_missing_vnet_service_endpoint:
          description:
            - >-
              Create firewall rule before the virtual network has vnet service
              endpoint enabled.
          returned: always
          type: boolean
          sample: null
    enable_multiple_write_locations:
      description:
        - Enables the account to write in multiple locations
      returned: always
      type: boolean
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.cosmosdb import CosmosDBClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMDatabaseAccounts(AzureRMModuleBaseExt):
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
                disposition='account_name',
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            kind=dict(
                type='str',
                updatable=False,
                disposition='/',
                choices=['GlobalDocumentDB',
                         'MongoDB',
                         'Parse']
            ),
            consistency_policy=dict(
                type='dict',
                disposition='/',
                options=dict(
                    default_consistency_level=dict(
                        type='str',
                        choices=['Eventual',
                                 'Session',
                                 'BoundedStaleness',
                                 'Strong',
                                 'ConsistentPrefix'],
                        required=true
                    ),
                    max_staleness_prefix=dict(
                        type='number'
                    ),
                    max_interval_in_seconds=dict(
                        type='number'
                    )
                )
            ),
            locations=dict(
                type='list',
                disposition='/',
                required=true,
                options=dict(
                    location_name=dict(
                        type='str'
                    ),
                    failover_priority=dict(
                        type='number'
                    )
                )
            ),
            database_account_offer_type=dict(
                type='str',
                disposition='/',
                required=true
            ),
            ip_range_filter=dict(
                type='str',
                disposition='/'
            ),
            is_virtual_network_filter_enabled=dict(
                type='boolean',
                disposition='/'
            ),
            enable_automatic_failover=dict(
                type='boolean',
                disposition='/'
            ),
            capabilities=dict(
                type='list',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str'
                    )
                )
            ),
            virtual_network_rules=dict(
                type='list',
                disposition='/',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    ignore_missing_vnet_service_endpoint=dict(
                        type='boolean'
                    )
                )
            ),
            enable_multiple_write_locations=dict(
                type='boolean',
                disposition='/'
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
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDatabaseAccounts, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(CosmosDB,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if 'location' not in self.body:
            self.body['location'] = resource_group.location

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
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["kind"] = response["kind"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.database_accounts.create_or_update(resource_group_name=self.resource_group,
                                                                           account_name=self.name,
                                                                           create_update_parameters=self.createUpdateParameters)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DatabaseAccount instance.')
            self.fail('Error creating the DatabaseAccount instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the DatabaseAccount instance {0}'.format(self.))
        try:
            response = self.mgmt_client.database_accounts.delete(resource_group_name=self.resource_group,
                                                                 account_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the DatabaseAccount instance.')
            self.fail('Error deleting the DatabaseAccount instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the DatabaseAccount instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.database_accounts.get(resource_group_name=self.resource_group,
                                                              account_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDatabaseAccounts()


if __name__ == '__main__':
    main()
