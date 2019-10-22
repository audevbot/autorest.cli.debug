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
module: azure_rm_apimanagementreport
version_added: '2.9'
short_description: Manage Azure Report instance.
description:
  - 'Create, update and delete instance of Azure Report.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
      name:
        description:
          - >-
            Name depending on report endpoint specifies product, API, operation
            or developer name.
        type: str
      timestamp:
        description:
          - >-
            Start of aggregation period. The date conforms to the following
            format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
            standard.<br>
        type: datetime
      interval:
        description:
          - >-
            Length of aggregation period.  Interval must be multiple of 15
            minutes and may not be zero. The value should be in ISO 8601 format
            (http://en.wikipedia.org/wiki/ISO_8601#Durations).
        type: str
      country:
        description:
          - Country to which this record data is related.
        type: str
      region:
        description:
          - Country region to which this record data is related.
        type: str
      zip:
        description:
          - Zip code to which this record data is related.
        type: str
      user_id:
        description:
          - 'User identifier path. /users/{userId}'
        type: str
      product_id:
        description:
          - 'Product identifier path. /products/{productId}'
        type: str
      api_id:
        description:
          - 'API identifier path. /apis/{apiId}'
        type: str
      operation_id:
        description:
          - 'Operation identifier path. /apis/{apiId}/operations/{operationId}'
        type: str
      api_region:
        description:
          - API region identifier.
        type: str
      subscription_id:
        description:
          - 'Subscription identifier path. /subscriptions/{subscriptionId}'
        type: str
      call_count_success:
        description:
          - >-
            Number of successful calls. This includes calls returning
            HttpStatusCode <= 301 and HttpStatusCode.NotModified and
            HttpStatusCode.TemporaryRedirect
        type: number
      call_count_blocked:
        description:
          - >-
            Number of calls blocked due to invalid credentials. This includes
            calls returning HttpStatusCode.Unauthorized and
            HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests
        type: number
      call_count_failed:
        description:
          - >-
            Number of calls failed due to proxy or backend errors. This includes
            calls returning HttpStatusCode.BadRequest(400) and any Code between
            HttpStatusCode.InternalServerError (500) and 600
        type: number
      call_count_other:
        description:
          - Number of other calls.
        type: number
      call_count_total:
        description:
          - Total number of calls.
        type: number
      bandwidth:
        description:
          - Bandwidth consumed.
        type: number
      cache_hit_count:
        description:
          - Number of times when content was served from cache policy.
        type: number
      cache_miss_count:
        description:
          - Number of times content was fetched from backend.
        type: number
      api_time_avg:
        description:
          - Average time it took to process request.
        type: number
      api_time_min:
        description:
          - Minimum time it took to process request.
        type: number
      api_time_max:
        description:
          - Maximum time it took to process request.
        type: number
      service_time_avg:
        description:
          - Average time it took to process request on backend.
        type: number
      service_time_min:
        description:
          - Minimum time it took to process request on backend.
        type: number
      service_time_max:
        description:
          - Maximum time it took to process request on backend.
        type: number
  count:
    description:
      - Total record count number across all pages.
    type: number
  next_link:
    description:
      - Next page link if any.
    type: str
  state:
    description:
      - Assert the state of the Report.
      - Use C(present) to create or update an Report and C(absent) to delete it.
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
    - Page values.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - >-
          Name depending on report endpoint specifies product, API, operation or
          developer name.
      returned: always
      type: str
      sample: null
    timestamp:
      description:
        - >-
          Start of aggregation period. The date conforms to the following
          format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
          standard.<br>
      returned: always
      type: datetime
      sample: null
    interval:
      description:
        - >-
          Length of aggregation period.  Interval must be multiple of 15 minutes
          and may not be zero. The value should be in ISO 8601 format
          (http://en.wikipedia.org/wiki/ISO_8601#Durations).
      returned: always
      type: str
      sample: null
    country:
      description:
        - Country to which this record data is related.
      returned: always
      type: str
      sample: null
    region:
      description:
        - Country region to which this record data is related.
      returned: always
      type: str
      sample: null
    zip:
      description:
        - Zip code to which this record data is related.
      returned: always
      type: str
      sample: null
    user_id:
      description:
        - 'User identifier path. /users/{userId}'
      returned: always
      type: str
      sample: null
    product_id:
      description:
        - 'Product identifier path. /products/{productId}'
      returned: always
      type: str
      sample: null
    api_id:
      description:
        - 'API identifier path. /apis/{apiId}'
      returned: always
      type: str
      sample: null
    operation_id:
      description:
        - 'Operation identifier path. /apis/{apiId}/operations/{operationId}'
      returned: always
      type: str
      sample: null
    api_region:
      description:
        - API region identifier.
      returned: always
      type: str
      sample: null
    subscription_id:
      description:
        - 'Subscription identifier path. /subscriptions/{subscriptionId}'
      returned: always
      type: str
      sample: null
    call_count_success:
      description:
        - >-
          Number of successful calls. This includes calls returning
          HttpStatusCode <= 301 and HttpStatusCode.NotModified and
          HttpStatusCode.TemporaryRedirect
      returned: always
      type: number
      sample: null
    call_count_blocked:
      description:
        - >-
          Number of calls blocked due to invalid credentials. This includes
          calls returning HttpStatusCode.Unauthorized and
          HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests
      returned: always
      type: number
      sample: null
    call_count_failed:
      description:
        - >-
          Number of calls failed due to proxy or backend errors. This includes
          calls returning HttpStatusCode.BadRequest(400) and any Code between
          HttpStatusCode.InternalServerError (500) and 600
      returned: always
      type: number
      sample: null
    call_count_other:
      description:
        - Number of other calls.
      returned: always
      type: number
      sample: null
    call_count_total:
      description:
        - Total number of calls.
      returned: always
      type: number
      sample: null
    bandwidth:
      description:
        - Bandwidth consumed.
      returned: always
      type: number
      sample: null
    cache_hit_count:
      description:
        - Number of times when content was served from cache policy.
      returned: always
      type: number
      sample: null
    cache_miss_count:
      description:
        - Number of times content was fetched from backend.
      returned: always
      type: number
      sample: null
    api_time_avg:
      description:
        - Average time it took to process request.
      returned: always
      type: number
      sample: null
    api_time_min:
      description:
        - Minimum time it took to process request.
      returned: always
      type: number
      sample: null
    api_time_max:
      description:
        - Maximum time it took to process request.
      returned: always
      type: number
      sample: null
    service_time_avg:
      description:
        - Average time it took to process request on backend.
      returned: always
      type: number
      sample: null
    service_time_min:
      description:
        - Minimum time it took to process request on backend.
      returned: always
      type: number
      sample: null
    service_time_max:
      description:
        - Maximum time it took to process request on backend.
      returned: always
      type: number
      sample: null
count:
  description:
    - Total record count number across all pages.
  returned: always
  type: number
  sample: null
next_link:
  description:
    - Next page link if any.
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
    from azure.mgmt.apimanagement import ApiManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMReports(AzureRMModuleBaseExt):
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
                disposition='service_name',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.value = None
        self.count = None
        self.next_link = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMReports, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ApiManagementClient,
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
           self.results["value"] = response["value"]
           self.results["count"] = response["count"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.reports.create()
            else:
                response = self.mgmt_client.reports.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Report instance.')
            self.fail('Error creating the Report instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Report instance {0}'.format(self.))
        try:
            response = self.mgmt_client.reports.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Report instance.')
            self.fail('Error deleting the Report instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Report instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.reports.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMReports()


if __name__ == '__main__':
    main()
