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
module: azure_rm_batchcertificate_info
version_added: '2.9'
short_description: Get Certificate info.
description:
  - Get info of Certificate.
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
    type: str
  account_name:
    description:
      - The name of the Batch account.
    required: true
    type: str
  maxresults:
    description:
      - The maximum number of items to return in the response.
    type: number
  name:
    description:
      - >-
        The identifier for the certificate. This must be made up of algorithm
        and thumbprint separated by a dash, and must match the certificate data
        in the request. For example SHA1-a3d1c5.
    type: str
  id:
    description:
      - The ID of the resource.
    type: str
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
    type: str
  thumbprint_algorithm:
    description:
      - >-
        This must match the first portion of the certificate name. Currently
        required to be 'SHA1'.
    type: str
  thumbprint:
    description:
      - This must match the thumbprint from the name.
    type: str
  format:
    description:
      - >-
        The format of the certificate - either Pfx or Cer. If omitted, the
        default is Pfx.
    type: str
  provisioning_state_transition_time:
    description:
      - undefined
    type: datetime
  previous_provisioning_state:
    description:
      - The previous provisioned state of the resource
    type: str
  previous_provisioning_state_transition_time:
    description:
      - undefined
    type: datetime
  public_data:
    description:
      - The public key of the certificate.
    type: str
  delete_certificate_error:
    description:
      - >-
        This is only returned when the certificate provisioningState is
        'Failed'.
    type: dict
    suboptions:
      code:
        description:
          - >-
            An identifier for the error. Codes are invariant and are intended to
            be consumed programmatically.
        required: true
        type: str
      message:
        description:
          - >-
            A message describing the error, intended to be suitable for display
            in a user interface.
        required: true
        type: str
      target:
        description:
          - >-
            The target of the particular error. For example, the name of the
            property in error.
        type: str
      details:
        description:
          - A list of additional details about the error.
        type: list
        suboptions:
          code:
            description:
              - >-
                An identifier for the error. Codes are invariant and are
                intended to be consumed programmatically.
            required: true
            type: str
          message:
            description:
              - >-
                A message describing the error, intended to be suitable for
                display in a user interface.
            required: true
            type: str
          target:
            description:
              - >-
                The target of the particular error. For example, the name of the
                property in error.
            type: str
          details:
            description:
              - A list of additional details about the error.
            type: list
            suboptions:
              code:
                description:
                  - >-
                    An identifier for the error. Codes are invariant and are
                    intended to be consumed programmatically.
                required: true
                type: str
              message:
                description:
                  - >-
                    A message describing the error, intended to be suitable for
                    display in a user interface.
                required: true
                type: str
              target:
                description:
                  - >-
                    The target of the particular error. For example, the name of
                    the property in error.
                type: str
              details:
                description:
                  - A list of additional details about the error.
                type: list
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListCertificates
  azure_rm_batchcertificate_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
- name: ListCertificates - Filter and Select
  azure_rm_batchcertificate_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
- name: Get Certificate
  azure_rm_batchcertificate_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate
- name: Get Certificate with Deletion Error
  azure_rm_batchcertificate_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myCertificate

'''

RETURN = '''
certificate:
  description: >-
    A list of dict results where the key is the name of the Certificate and the
    values are the facts for that Certificate.
  returned: always
  type: complex
  contains:
    certificate_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - The ID of the resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - 'The ETag of the resource, used for concurrency statements.'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The properties associated with the certificate.
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
    from azure.mgmt.batch import BatchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCertificateInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            account_name=dict(
                type='str',
                required=true
            ),
            maxresults=dict(
                type='number'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.account_name = None
        self.maxresults = None
        self.name = None
        self.id = None
        self.etag = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCertificateInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.name is not None):
            self.results['certificate'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['certificate'] = self.format_item(self.listbybatchaccount())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.certificate.get(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        certificate_name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def listbybatchaccount(self):
        response = None

        try:
            response = self.mgmt_client.certificate.list_by_batch_account(resource_group_name=self.resource_group,
                                                                          account_name=self.account_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response.as_dict()

    def format_item(item):
        return item


def main():
    AzureRMCertificateInfo()


if __name__ == '__main__':
    main()
