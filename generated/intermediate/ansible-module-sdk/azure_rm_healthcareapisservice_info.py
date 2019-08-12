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
module: azure_rm_healthcareapisservice_info
version_added: '2.9'
short_description: Get Service info.
description:
  - Get info of Service.
options:
  resource_group:
    description:
      - The name of the resource group that contains the service instance.
    type: str
  name:
    description:
      - The resource name.
    type: str
  id:
    description:
      - The resource identifier.
    type: str
  type:
    description:
      - The resource type.
    type: str
  kind:
    description:
      - 'The kind of the service. Valid values are: fhir, fhir-Stu3 and fhir-R4.'
    type: str
  location:
    description:
      - The resource location.
    type: str
  etag:
    description:
      - >-
        An etag associated with the resource, used for optimistic concurrency
        when editing it.
    type: str
  provisioning_state:
    description:
      - The provisioning state.
    type: str
  access_policies_object_id:
    description:
      - An object ID that is allowed access to the FHIR service.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ServiceList
  azure_rm_healthcareapisservice_info: {}
- name: ServiceListByResourceGroup
  azure_rm_healthcareapisservice_info:
    resource_group: myResourceGroup
- name: ServiceGet
  azure_rm_healthcareapisservice_info:
    resource_group: myResourceGroup
    name: myService

'''

RETURN = '''
services:
  description: >-
    A list of dict results where the key is the name of the Service and the
    values are the facts for that Service.
  returned: always
  type: complex
  contains:
    service_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
            - >-
              The kind of the service. Valid values are: fhir, fhir-Stu3 and
              fhir-R4.
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
              An etag associated with the resource, used for optimistic
              concurrency when editing it.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The common properties of a service.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.healthcareapis import HealthCareApisClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMServicesInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.kind = None
        self.location = None
        self.tags = None
        self.etag = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-08-20-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMServicesInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(HealthCareApisClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['services'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['services'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['services'] = [self.format_item(self.list())]
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.services.get(resource_group_name=self.resource_group,
                                                     resource_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.services.list_by_resource_group(resource_group_name=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def list(self):
        response = None

        try:
            response = self.mgmt_client.services.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMServicesInfo()


if __name__ == '__main__':
    main()
