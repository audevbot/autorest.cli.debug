# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

BODY = {}
        output = mgmt_client.services.get(RESOURCE_GROUP, SERVICE_NAME, BODY)
BODY = {
  "location": "westus2",
  "kind": "fhir-R4",
  "properties": {
    "access_policies": [
      {
        "object_id": "c487e7d1-3210-41a3-8ccc-e9372b78da47"
      },
      {
        "object_id": "5b307da8-43d4-492b-8b66-b0294ade872f"
      }
    ],
    "cosmos_db_configuration": {
      "offer_throughput": "1000"
    },
    "authentication_configuration": {
      "authority": "https://login.microsoftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc",
      "audience": "https://azurehealthcareapis.com",
      "smart_proxy_enabled": True
    },
    "cors_configuration": {
      "origins": [
        "*"
      ],
      "headers": [
        "*"
      ],
      "methods": [
        "DELETE",
        "GET",
        "OPTIONS",
        "PATCH",
        "POST",
        "PUT"
      ],
      "max_age": "1440",
      "allow_credentials": False
    }
  }
}
        output = mgmt_client.services.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
BODY = {
  "location": "westus2",
  "kind": "fhir-R4",
  "properties": {
    "access_policies": [
      {
        "object_id": "c487e7d1-3210-41a3-8ccc-e9372b78da47"
      }
    ]
  }
}
        output = mgmt_client.services.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
BODY = {
  "tags": {
    "tag1": "value1",
    "tag2": "value2"
  }
}
        output = mgmt_client.services.update(RESOURCE_GROUP, SERVICE_NAME, BODY)
BODY = {}
        output = mgmt_client.services.delete(RESOURCE_GROUP, SERVICE_NAME, BODY)
BODY = {}
        output = mgmt_client.services.list(, BODY)
BODY = {}
        output = mgmt_client.services.list_by_resource_group(RESOURCE_GROUP, , BODY)
BODY = {
  "type": "Microsoft.HealthcareApis/services",
  "name": "serviceName"
}
        output = mgmt_client.services.check_name_availability(, BODY)
BODY = {}
        output = mgmt_client.operations.list(, BODY)
BODY = {}
        output = mgmt_client.operation_results.get(LOCATION_NAME, OPERATIONRESULT_NAME, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()