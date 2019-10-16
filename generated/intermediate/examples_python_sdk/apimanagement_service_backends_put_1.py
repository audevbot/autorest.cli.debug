# ApiManagementCreateBackendProxyBackend
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
BACKEND_NAME = "mybackend"

BODY = {
  "properties": {
    "description": "description5308",
    "url": "https://backendname2644/",
    "protocol": "http",
    "tls": {
      "validate_certificate_chain": True,
      "validate_certificate_name": True
    },
    "proxy": {
      "url": "http://192.168.1.1:8080",
      "username": "Contoso\\admin",
      "password": "opensesame"
    },
    "credentials": {
      "query": {
        "sv": [
          "xx",
          "bb",
          "cc"
        ]
      },
      "header": {
        "x-my-1": [
          "val1",
          "val2"
        ]
      },
      "authorization": {
        "scheme": "Basic",
        "parameter": "opensesma"
      }
    }
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
    response = mgmt_client.backend.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()