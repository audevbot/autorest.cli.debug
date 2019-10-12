# ApiManagementUpdateApiOperation
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
from azure.mgmt.apimanagement import ApiManagementClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
SERVICE_NAME = "myservice"
API_NAME = "myapi"
OPERATION_NAME = "myoperation"

BODY = {
  "properties": {
    "display_name": "Retrieve resource",
    "method": "GET",
    "url_template": "/resource",
    "template_parameters": [],
    "request": {
      "query_parameters": [
        {
          "name": "param1",
          "description": "A sample parameter that is required and has a default value of \"sample\".",
          "type": "string",
          "default_value": "sample",
          "required": True,
          "values": [
            "sample"
          ]
        }
      ]
    },
    "responses": [
      {
        "status_code": "200",
        "description": "Returned in all cases.",
        "representations": [],
        "headers": []
      },
      {
        "status_code": "500",
        "description": "Server Error.",
        "representations": [],
        "headers": []
      }
    ]
  }
}

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()
    mgmt_client = ApiManagementClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.api_operation.update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()