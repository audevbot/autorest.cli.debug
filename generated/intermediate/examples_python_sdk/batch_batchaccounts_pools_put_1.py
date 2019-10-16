# CreatePool - Minimal VirtualMachineConfiguration
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
from azure.mgmt.batch import BatchManagement
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
BATCH_ACCOUNT_NAME = "mybatchaccount"
POOL_NAME = "mypool"

BODY = {
  "properties": {
    "vm_size": "STANDARD_D4",
    "deployment_configuration": {
      "virtual_machine_configuration": {
        "image_reference": {
          "publisher": "Canonical",
          "offer": "UbuntuServer",
          "sku": "14.04.5-LTS",
          "version": "latest"
        },
        "node_agent_sku_id": "batch.node.ubuntu 14.04"
      }
    },
    "scale_settings": {
      "auto_scale": {
        "formula": "$TargetDedicatedNodes=1",
        "evaluation_interval": "PT5M"
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
    mgmt_client = BatchManagement(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()