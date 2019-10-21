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
from azure.mgmt.vmwarecloudsimple import VMwareCloudSimple
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
    "private_cloud_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "",
    "template_id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualMachineTemplates/" + VIRTUAL_MACHINE_TEMPLATE_NAME + "",
    "number_of_cores": "2",
    "amount_of_ram": "4096",
    "disks": [
      {
        "controller_id": "1000",
        "independence_mode": "persistent",
        "total_size": "10485760",
        "virtual_disk_id": "2000"
      }
    ],
    "resource_pool": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/resourcePools/" + RESOURCE_POOL_NAME + ""
    },
    "nics": [
      {
        "network": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualNetworks/" + VIRTUAL_NETWORK_NAME + ""
        },
        "nic_type": "E1000",
        "power_on_boot": True,
        "virtual_nic_id": "4000"
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
    mgmt_client = VMwareCloudSimple(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.virtual_machines.create_or_update(RESOURCE_GROUP, VIRTUAL_MACHINE_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()