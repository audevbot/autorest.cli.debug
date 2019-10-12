# Create or Update a service with all parameters
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
from azure.mgmt.healthcareapis import HealthCareApis
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
SERVICE_NAME = "myservice"

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

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()
    mgmt_client = HealthCareApis(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.services.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()