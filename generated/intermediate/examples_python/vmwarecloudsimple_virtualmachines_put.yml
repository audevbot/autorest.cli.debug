# CreateVirtualMachine
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
VIRTUAL_MACHINE_NAME = "myvirtualmachine"
LOCATION_NAME = "mylocation"
PRIVATE_CLOUD_NAME = "myprivatecloud"
VIRTUAL_MACHINE_TEMPLATE_NAME = "myvirtualmachinetemplate"
RESOURCE_POOL_NAME = "myresourcepool"
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"

BODY = {
  "location": "westus2",
  "properties": {
    "privateCloudId": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "",
    "templateId": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualMachineTemplates/" + VIRTUAL_MACHINE_TEMPLATE_NAME + "",
    "numberOfCores": "2",
    "amountOfRam": "4096",
    "disks": [
      {
        "controllerId": "1000",
        "independenceMode": "persistent",
        "totalSize": "10485760",
        "virtualDiskId": "2000"
      }
    ],
    "resourcePool": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/resourcePools/" + RESOURCE_POOL_NAME + ""
    },
    "guestOS": "Other (32-bit)",
    "guestOSType": "other",
    "nics": [
      {
        "network": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualNetworks/" + VIRTUAL_NETWORK_NAME + ""
        },
        "nicType": "E1000",
        "powerOnBoot": True,
        "virtualNicId": "4000"
      }
    ]
  }
}

API_VERSION = '2019-04-01'

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
    request = service_client.put("/subscriptions/" + SUBSCRIPTION + "/resourceGroups/" + RESOURCE_GR + "/providers/Microsoft.VMwareCloudSimple/virtualMachines/" + VIRTUAL_MACHINE_N, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()