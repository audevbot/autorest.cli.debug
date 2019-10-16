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
module: azure_rm_healthcareapisservice
version_added: '2.9'
short_description: Manage Azure Service instance.
description:
  - 'Create, update and delete instance of Azure Service.'
options:
  resource_group:
    description:
      - The name of the resource group that contains the service instance.
    required: true
    type: str
  name:
    description:
      - The resource name.
    type: str
  kind:
    description:
      - The kind of the service.
    required: true
    type: str
  location:
    description:
      - The resource location.
    required: true
    type: str
  etag:
    description:
      - >-
        An etag associated with the resource, used for optimistic concurrency
        when editing it.
    type: str
  access_policies_object_id:
    description:
      - >-
        An Azure AD object ID (User or Apps) that is allowed access to the FHIR
        service.
    required: true
    type: str
  cosmos_db_offer_throughput:
    description:
      - The provisioned throughput for the backing database.
    type: number
  authentication_authority:
    description:
      - The authority url for the service
    type: str
  authentication_audience:
    description:
      - The audience url for the service
    type: str
  authentication_smart_proxy_enabled:
    description:
      - If the SMART on FHIR proxy is enabled
    type: boolean
  cors_origins:
    description:
      - The origins to be allowed via CORS.
    type: list
  cors_headers:
    description:
      - The headers to be allowed via CORS.
    type: list
  cors_methods:
    description:
      - The methods to be allowed via CORS.
    type: list
  cors_max_age:
    description:
      - The max age to be allowed via CORS.
    type: number
  cors_allow_credentials:
    description:
      - If credentials are allowed via CORS.
    type: boolean
  provisioning_state:
    description:
      - The provisioning state.
    type: str
  id:
    description:
      - The resource identifier.
    type: str
  type:
    description:
      - The resource type.
    type: str
  state:
    description:
      - Assert the state of the Service.
      - >-
        Use C(present) to create or update an Service and C(absent) to delete
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
- name: Create or Update a service with all parameters
  azure_rm_healthcareapisservice:
    resource_group: myResourceGroup
    name: myService
    service_description:
      location: westus2
      tags: {}
      kind: fhir-R4
      properties:
        accessPolicies:
          - object_id: c487e7d1-3210-41a3-8ccc-e9372b78da47
          - object_id: 5b307da8-43d4-492b-8b66-b0294ade872f
        cosmosDbConfiguration:
          offerThroughput: '1000'
        authenticationConfiguration:
          authority: >-
            https://login.microsoftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc
          audience: 'https://azurehealthcareapis.com'
          smartProxyEnabled: true
        corsConfiguration:
          origins:
            - '*'
          headers:
            - '*'
          methods:
            - DELETE
            - GET
            - OPTIONS
            - PATCH
            - POST
            - PUT
          maxAge: '1440'
          allowCredentials: false
- name: Create or Update a service with minimum parameters
  azure_rm_healthcareapisservice:
    resource_group: myResourceGroup
    name: myService
    service_description:
      location: westus2
      tags: {}
      kind: fhir-R4
      properties:
        accessPolicies:
          - object_id: c487e7d1-3210-41a3-8ccc-e9372b78da47
- name: Patch service
  azure_rm_healthcareapisservice:
    resource_group: myResourceGroup
    name: myService
- name: Delete service
  azure_rm_healthcareapisservice:
    resource_group: myResourceGroup
    name: myService
    state: absent

'''

RETURN = '''
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
kind:
  description:
    - The kind of the service.
  returned: always
  type: str
  sample: null
location:
  description:
    - The resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: >-
    unknown[DictionaryType
    {"$id":"158","$type":"DictionaryType","valueType":{"$id":"159","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"160","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"161","fixed":false},"deprecated":false}]
  sample: null
etag:
  description:
    - >-
      An etag associated with the resource, used for optimistic concurrency when
      editing it.
  returned: always
  type: str
  sample: null
properties:
  description:
    - The common properties of a service.
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_state:
      description:
        - The provisioning state.
      returned: always
      type: str
      sample: null
    access_policies:
      description:
        - The access policies of the service instance.
      returned: always
      type: dict
      sample: null
      contains:
        object_id:
          description:
            - >-
              An Azure AD object ID (User or Apps) that is allowed access to the
              FHIR service.
          returned: always
          type: str
          sample: null
    cosmos_db_configuration:
      description:
        - The settings for the Cosmos DB database backing the service.
      returned: always
      type: dict
      sample: null
      contains:
        offer_throughput:
          description:
            - The provisioned throughput for the backing database.
          returned: always
          type: number
          sample: null
    authentication_configuration:
      description:
        - The authentication configuration for the service instance.
      returned: always
      type: dict
      sample: null
      contains:
        authority:
          description:
            - The authority url for the service
          returned: always
          type: str
          sample: null
        audience:
          description:
            - The audience url for the service
          returned: always
          type: str
          sample: null
        smart_proxy_enabled:
          description:
            - If the SMART on FHIR proxy is enabled
          returned: always
          type: boolean
          sample: null
    cors_configuration:
      description:
        - The settings for the CORS configuration of the service instance.
      returned: always
      type: dict
      sample: null
      contains:
        origins:
          description:
            - The origins to be allowed via CORS.
          returned: always
          type: str
          sample: null
        headers:
          description:
            - The headers to be allowed via CORS.
          returned: always
          type: str
          sample: null
        methods:
          description:
            - The methods to be allowed via CORS.
          returned: always
          type: str
          sample: null
        max_age:
          description:
            - The max age to be allowed via CORS.
          returned: always
          type: number
          sample: null
        allow_credentials:
          description:
            - If credentials are allowed via CORS.
          returned: always
          type: boolean
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


class AzureRMServices(AzureRMModuleBaseExt):
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
                disposition='resourceName',
                required=true
            ),
            kind=dict(
                type='str',
                updatable=False,
                disposition='/',
                choices=['fhir',
                         'fhir-Stu3',
                         'fhir-R4'],
                required=true
            ),
            location=dict(
                type='str',
                updatable=False,
                disposition='/',
                required=true
            ),
            etag=dict(
                type='str',
                updatable=False,
                disposition='/'
            ),
            access_policies_object_id=dict(
                type='str',
                disposition='/properties/accessPolicies/objectId',
                required=true
            ),
            cosmos_db_offer_throughput=dict(
                type='number',
                disposition='/properties/cosmosDbConfiguration/offerThroughput'
            ),
            authentication_authority=dict(
                type='str',
                disposition='/properties/authenticationConfiguration/authority'
            ),
            authentication_audience=dict(
                type='str',
                disposition='/properties/authenticationConfiguration/audience'
            ),
            authentication_smart_proxy_enabled=dict(
                type='boolean',
                disposition='/properties/authenticationConfiguration/smartProxyEnabled'
            ),
            cors_origins=dict(
                type='list',
                disposition='/properties/corsConfiguration/origins'
            ),
            cors_headers=dict(
                type='list',
                disposition='/properties/corsConfiguration/headers'
            ),
            cors_methods=dict(
                type='list',
                disposition='/properties/corsConfiguration/methods'
            ),
            cors_max_age=dict(
                type='number',
                disposition='/properties/corsConfiguration/maxAge'
            ),
            cors_allow_credentials=dict(
                type='boolean',
                disposition='/properties/corsConfiguration/allowCredentials'
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
        self.query_parameters['api-version'] = '2019-09-16'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMServices, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/Microsoft.HealthcareApis' +
                    '/services' +
                    '/{{ service_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("Service instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Service instance already exists')

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
            self.log('Need to Create / Update the Service instance')

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
            self.log('Service instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Service instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["kind"] = response["kind"]
           self.results["location"] = response["location"]
           self.results["tags"] = response["tags"]
           self.results["etag"] = response["etag"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Service instance {0}'.format(self.))

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
            self.log('Error attempting to create the Service instance.')
            self.fail('Error creating the Service instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Service instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Service instance.')
            self.fail('Error deleting the Service instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Service instance {0} is present'.format(self.))
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
            # self.log("Service instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Service instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMServices()


if __name__ == '__main__':
    main()
