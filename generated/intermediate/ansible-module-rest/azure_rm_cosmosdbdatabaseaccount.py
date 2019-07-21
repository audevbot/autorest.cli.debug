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
    type: str
  name:
    description:
      - The name of the database account.
    type: str
  location:
    description:
      - The location of the resource group to which the resource belongs.
    type: str
  kind:
    description:
      - >-
        Indicates the type of database account. This can only be set at database
        account creation.
    type: str
  consistency_policy:
    description:
      - The consistency policy for the Cosmos DB account.
    type: dict
    suboptions:
      default_consistency_level:
        description:
          - >-
            The default consistency level and configuration settings of the
            Cosmos DB account.
        required: true
        type: str
      max_staleness_prefix:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the number of stale requests tolerated. Accepted range
            for this value is 1 – 2,147,483,647. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
        type: number
      max_interval_in_seconds:
        description:
          - >-
            When used with the Bounded Staleness consistency level, this value
            represents the time amount of staleness (in seconds) tolerated.
            Accepted range for this value is 5 - 86400. Required when
            defaultConsistencyPolicy is set to 'BoundedStaleness'.
        type: number
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
        type: str
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
        type: number
      is_zone_redundant:
        description:
          - >-
            Flag to indicate whether or not this region is an AvailabilityZone
            region
        type: boolean
  database_account_offer_type:
    description:
      - The offer type for the database
    required: true
    type: str
  ip_range_filter:
    description:
      - >-
        Cosmos DB Firewall Support: This value specifies the set of IP addresses
        or IP address ranges in CIDR form to be included as the allowed list of
        client IPs for a given database account. IP addresses/ranges must be
        comma separated and must not contain any spaces.
    type: str
  is_virtual_network_filter_enabled:
    description:
      - Flag to indicate whether to enable/disable Virtual Network ACL rules.
    type: boolean
  enable_automatic_failover:
    description:
      - >-
        Enables automatic failover of the write region in the rare event that
        the region is unavailable due to an outage. Automatic failover will
        result in a new write region for the account and is chosen based on the
        failover priorities configured for the account.
    type: boolean
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
        type: str
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
        type: str
      ignore_missing_vnet_service_endpoint:
        description:
          - >-
            Create firewall rule before the virtual network has vnet service
            endpoint enabled.
        type: boolean
  enable_multiple_write_locations:
    description:
      - Enables the account to write in multiple locations
    type: boolean
  enable_cassandra_connector:
    description:
      - Enables the cassandra connector on the Cosmos DB C* account
    type: boolean
  connector_offer:
    description:
      - >-
        The cassandra connector offer type for the Cosmos DB database C*
        account.
    type: str
  provisioning_state:
    description:
      - undefined
    type: str
  document_endpoint:
    description:
      - The connection endpoint for the Cosmos DB database account.
    type: str
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
        type: str
      location_name:
        description:
          - The name of the region.
        type: str
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
        type: str
      provisioning_state:
        description:
          - undefined
        type: str
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
        type: number
      is_zone_redundant:
        description:
          - >-
            Flag to indicate whether or not this region is an AvailabilityZone
            region
        type: boolean
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
        type: str
      location_name:
        description:
          - The name of the region.
        type: str
      document_endpoint:
        description:
          - >-
            The connection endpoint for the specific region. Example:
            https://&lt;accountName&gt;-&lt;locationName&gt;.documents.azure.com:443/
        type: str
      provisioning_state:
        description:
          - undefined
        type: str
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
        type: number
      is_zone_redundant:
        description:
          - >-
            Flag to indicate whether or not this region is an AvailabilityZone
            region
        type: boolean
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
        type: str
      location_name:
        description:
          - The name of the region in which the database account exists.
        type: str
      failover_priority:
        description:
          - >-
            The failover priority of the region. A failover priority of 0
            indicates a write region. The maximum value for a failover priority
            = (total number of regions - 1). Failover priority values must be
            unique for each of the regions in which the database account exists.
        type: number
  id:
    description:
      - The unique resource identifier of the database account.
    type: str
  type:
    description:
      - The type of Azure resource.
    type: str
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
    create_update_parameters:
      location: westus
      properties:
        databaseAccountOfferType: Standard
        locations:
          - failoverPriority: '0'
            locationName: southcentralus
            isZoneRedundant: false
- name: CosmosDBDatabaseAccountCreateMax
  azure_rm_cosmosdbdatabaseaccount:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    create_update_parameters:
      location: westus
      tags: {}
      kind: GlobalDocumentDB
      properties:
        databaseAccountOfferType: Standard
        ipRangeFilter: 10.10.10.10
        isVirtualNetworkFilterEnabled: true
        virtualNetworkRules:
          - id: >-
              /subscriptions/{{ subscription_id }}/resourceGroups/{{
              resource_group }}/providers/Microsoft.Network/virtualNetworks/{{
              virtual_network_name }}/subnets/{{ subnet_name }}
            ignoreMissingVNetServiceEndpoint: false
        locations:
          - failoverPriority: '0'
            locationName: southcentralus
            isZoneRedundant: false
          - failoverPriority: '1'
            locationName: eastus
            isZoneRedundant: false
        consistencyPolicy:
          defaultConsistencyLevel: BoundedStaleness
          maxIntervalInSeconds: '10'
          maxStalenessPrefix: '200'
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
    - ''
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"250","$type":"DictionaryType","valueType":{"$id":"251","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"252","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"253","fixed":false},"deprecated":false}]
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
    - ''
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_state:
      description:
        - ''
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
            - ''
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
        is_zone_redundant:
          description:
            - >-
              Flag to indicate whether or not this region is an AvailabilityZone
              region
          returned: always
          type: boolean
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
            - ''
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
        is_zone_redundant:
          description:
            - >-
              Flag to indicate whether or not this region is an AvailabilityZone
              region
          returned: always
          type: boolean
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
    enable_cassandra_connector:
      description:
        - Enables the cassandra connector on the Cosmos DB C* account
      returned: always
      type: boolean
      sample: null
    connector_offer:
      description:
        - >-
          The cassandra connector offer type for the Cosmos DB database C*
          account.
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


class AzureRMDatabaseAccounts(AzureRMModuleBaseExt):
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
                disposition='accountName',
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
                disposition='/properties/consistencyPolicy',
                options=dict(
                    default_consistency_level=dict(
                        type='str',
                        disposition='defaultConsistencyLevel',
                        choices=['Eventual',
                                 'Session',
                                 'BoundedStaleness',
                                 'Strong',
                                 'ConsistentPrefix'],
                        required=true
                    ),
                    max_staleness_prefix=dict(
                        type='number',
                        disposition='maxStalenessPrefix'
                    ),
                    max_interval_in_seconds=dict(
                        type='number',
                        disposition='maxIntervalInSeconds'
                    )
                )
            ),
            locations=dict(
                type='list',
                disposition='/properties/*',
                required=true,
                options=dict(
                    location_name=dict(
                        type='str',
                        disposition='locationName'
                    ),
                    failover_priority=dict(
                        type='number',
                        disposition='failoverPriority'
                    ),
                    is_zone_redundant=dict(
                        type='boolean',
                        disposition='isZoneRedundant'
                    )
                )
            ),
            database_account_offer_type=dict(
                type='str',
                disposition='/properties/databaseAccountOfferType',
                required=true
            ),
            ip_range_filter=dict(
                type='str',
                disposition='/properties/ipRangeFilter'
            ),
            is_virtual_network_filter_enabled=dict(
                type='boolean',
                disposition='/properties/isVirtualNetworkFilterEnabled'
            ),
            enable_automatic_failover=dict(
                type='boolean',
                disposition='/properties/enableAutomaticFailover'
            ),
            capabilities=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    name=dict(
                        type='str'
                    )
                )
            ),
            virtual_network_rules=dict(
                type='list',
                disposition='/properties/virtualNetworkRules',
                options=dict(
                    id=dict(
                        type='str'
                    ),
                    ignore_missing_vnet_service_endpoint=dict(
                        type='boolean',
                        disposition='ignoreMissingVNetServiceEndpoint'
                    )
                )
            ),
            enable_multiple_write_locations=dict(
                type='boolean',
                disposition='/properties/enableMultipleWriteLocations'
            ),
            enable_cassandra_connector=dict(
                type='boolean',
                disposition='/properties/enableCassandraConnector'
            ),
            connector_offer=dict(
                type='str',
                disposition='/properties/connectorOffer',
                choices=['Small']
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
        self.query_parameters['api-version'] = '2015-04-08'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

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
                    '/Microsoft.DocumentDB' +
                    '/databaseAccounts' +
                    '/{{ database_account_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ database_account_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("DatabaseAccount instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('DatabaseAccount instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the DatabaseAccount instance')

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
            self.log('DatabaseAccount instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('DatabaseAccount instance unchanged')
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
        # self.log('Creating / Updating the DatabaseAccount instance {0}'.format(self.))

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
            self.log('Error attempting to create the DatabaseAccount instance.')
            self.fail('Error creating the DatabaseAccount instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the DatabaseAccount instance {0}'.format(self.))
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
            self.log('Error attempting to delete the DatabaseAccount instance.')
            self.fail('Error deleting the DatabaseAccount instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the DatabaseAccount instance {0} is present'.format(self.))
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
            # self.log("DatabaseAccount instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the DatabaseAccount instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMDatabaseAccounts()


if __name__ == '__main__':
    main()
