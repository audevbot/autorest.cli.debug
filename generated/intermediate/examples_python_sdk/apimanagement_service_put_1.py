# ApiManagementCreateMultiRegionServiceWithCustomHostname
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
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"
SUBNET_NAME = "mysubnet"

BODY = {
  "location": "Central US",
  "sku": {
    "name": "Premium",
    "capacity": "1"
  },
  "properties": {
    "publisher_email": "admin@live.com",
    "publisher_name": "contoso",
    "additional_locations": [
      {
        "location": "North Europe",
        "sku": {
          "name": "Premium",
          "capacity": "1"
        },
        "virtual_network_configuration": {
          "subnet_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        }
      }
    ],
    "hostname_configurations": [
      {
        "type": "Proxy",
        "host_name": "proxyhostname1.contoso.com",
        "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificate_password": "**************Password of the Certificate************************************************"
      },
      {
        "type": "Proxy",
        "host_name": "proxyhostname2.contoso.com",
        "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificate_password": "**************Password of the Certificate************************************************",
        "negotiate_client_certificate": True
      },
      {
        "type": "Portal",
        "host_name": "portalhostname1.contoso.com",
        "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificate_password": "**************Password of the Certificate************************************************"
      }
    ],
    "virtual_network_configuration": {
      "subnet_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
    },
    "virtual_network_type": "External"
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
    response = mgmt_client.api_management_service.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()