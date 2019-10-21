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
module: apimanagementquotabycounterkey
version_added: '2.9'
short_description: Manage Azure QuotaByCounterKey instance.
description:
  - 'Create, update and delete instance of Azure QuotaByCounterKey.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  quota_counter_key:
    description:
      - >-
        Quota counter key identifier.This is the result of expression defined in
        counter-key attribute of the quota-by-key policy.For Example, if you
        specify counter-key="boo" in the policy, then it’s accessible by "boo"
        counter key. But if it’s defined as counter-key="@("b"+"a")" then it
        will be accessible by "ba" key
    required: true
    type: str
  value:
    description:
      - Quota counter values.
    type: list
    suboptions:
      counter_key:
        description:
          - The Key value of the Counter. Must not be empty.
        required: true
        type: str
      period_key:
        description:
          - >-
            Identifier of the Period for which the counter was collected. Must
            not be empty.
        required: true
        type: str
      period_start_time:
        description:
          - >-
            The date of the start of Counter Period. The date conforms to the
            following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
            8601 standard.<br>
        required: true
        type: datetime
      period_end_time:
        description:
          - >-
            The date of the end of Counter Period. The date conforms to the
            following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
            8601 standard.<br>
        required: true
        type: datetime
      value:
        description:
          - Quota Value Properties
        type: dict
        suboptions:
          calls_count:
            description:
              - Number of times Counter was called.
            type: number
          kb_transferred:
            description:
              - Data Transferred in KiloBytes.
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
      - Assert the state of the QuotaByCounterKey.
      - >-
        Use C(present) to create or update an QuotaByCounterKey and C(absent) to
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
value:
  description:
    - Quota counter values.
  returned: always
  type: dict
  sample: null
  contains:
    counter_key:
      description:
        - The Key value of the Counter. Must not be empty.
      returned: always
      type: str
      sample: null
    period_key:
      description:
        - >-
          Identifier of the Period for which the counter was collected. Must not
          be empty.
      returned: always
      type: str
      sample: null
    period_start_time:
      description:
        - >-
          The date of the start of Counter Period. The date conforms to the
          following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
          standard.<br>
      returned: always
      type: datetime
      sample: null
    period_end_time:
      description:
        - >-
          The date of the end of Counter Period. The date conforms to the
          following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
          standard.<br>
      returned: always
      type: datetime
      sample: null
    value:
      description:
        - Quota Value Properties
      returned: always
      type: dict
      sample: null
      contains:
        calls_count:
          description:
            - Number of times Counter was called.
          returned: always
          type: number
          sample: null
        kb_transferred:
          description:
            - Data Transferred in KiloBytes.
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
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMQuotaByCounterKeys(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            service_name=dict(
                type='str',
                updatable=False,
                disposition='serviceName',
                required=true
            ),
            quota_counter_key=dict(
                type='str',
                updatable=False,
                disposition='quotaCounterKey',
                required=true
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.quota_counter_key = None
        self.value = None
        self.count = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMQuotaByCounterKeys, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/quotas' +
                    '/{{ quota_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ quota_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("QuotaByCounterKey instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('QuotaByCounterKey instance already exists')

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
            self.log('Need to Create / Update the QuotaByCounterKey instance')

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
            self.log('QuotaByCounterKey instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('QuotaByCounterKey instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["value"] = response["value"]
           self.results["count"] = response["count"]
           self.results["next_link"] = response["next_link"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the QuotaByCounterKey instance {0}'.format(self.))

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
            self.log('Error attempting to create the QuotaByCounterKey instance.')
            self.fail('Error creating the QuotaByCounterKey instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the QuotaByCounterKey instance {0}'.format(self.))
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
            self.log('Error attempting to delete the QuotaByCounterKey instance.')
            self.fail('Error deleting the QuotaByCounterKey instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the QuotaByCounterKey instance {0} is present'.format(self.))
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
            # self.log("QuotaByCounterKey instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the QuotaByCounterKey instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMQuotaByCounterKeys()


if __name__ == '__main__':
    main()
