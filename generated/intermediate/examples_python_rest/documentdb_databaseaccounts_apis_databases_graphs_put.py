# CosmosDBGremlinGraphCreateUpdate
#
# This script expects that the following environment vars are set:
#
# AZURE_TENANT: your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
# AZURE_SECRET: your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: your Azure Subscription Id

import os
import traceback
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_configuration import AzureConfiguration
from msrest.service_client import ServiceClient
from msrest.polling import LROPoller
from msrestazure.polling.arm_polling import ARMPolling
from msrest.pipeline import ClientRawResponse
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
DATABASE_ACCOUNT_NAME = "mydatabaseaccount"
API_NAME = "myapi"
DATABASE_NAME = "mydatabase"
GRAPH_NAME = "mygraph"

BODY = {
  "properties": {
    "resource": {
      "id": "graphName",
      "indexingPolicy": {
        "indexingMode": "Consistent",
        "automatic": True,
        "includedPaths": [
          {
            "path": "/*",
            "indexes": [
              {
                "kind": "Range",
                "dataType": "String",
                "precision": "-1"
              },
              {
                "kind": "Range",
                "dataType": "Number",
                "precision": "-1"
              }
            ]
          }
        ],
        "excludedPaths": []
      },
      "partitionKey": {
        "paths": [
          "/AccountNumber"
        ],
        "kind": "Hash"
      },
      "defaultTtl": "100",
      "uniqueKeyPolicy": {
        "uniqueKeys": [
          {
            "paths": [
              "/testPath"
            ]
          }
        ]
      },
      "conflictResolutionPolicy": {
        "mode": "LastWriterWins",
        "conflictResolutionPath": "/path"
      }
    },
    "options": {}
  }
}

API_VERSION = '2015-04-08'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()

    config = AzureConfiguration('https://management.azure.com')
    service_client = ServiceClient(credentials, config)

    query_parameters = {}
    query_parameters['api-version'] = API_VERSION

    header_parameters = {}
    header_parameters['Content-Type'] = 'application/json; charset=utf-8'

    operation_config = {}
    request = service_client.put("/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.DocumentDB/databaseAccounts/" + DATABASE_ACCOUNT_NAME + "/apis/" + API_NAME + "/databases/" + DATABASE_NAME + "/graphs/" + GRAPH_NAME, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()