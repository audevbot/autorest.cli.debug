# CreatePool - Full VirtualMachineConfiguration
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
BATCH_ACCOUNT_NAME = "mybatchaccount"
POOL_NAME = "mypool"

BODY = {
  "properties": {
    "vmSize": "STANDARD_D4",
    "deploymentConfiguration": {
      "virtualMachineConfiguration": {
        "imageReference": {
          "publisher": "MicrosoftWindowsServer",
          "offer": "WindowsServer",
          "sku": "2016-Datacenter-SmallDisk",
          "version": "latest"
        },
        "nodeAgentSkuId": "batch.node.windows amd64",
        "windowsConfiguration": {
          "enableAutomaticUpdates": False
        },
        "licenseType": "Windows_Server",
        "dataDisks": [
          {
            "lun": "0",
            "caching": "ReadWrite",
            "diskSizeGB": "30",
            "storageAccountType": "Premium_LRS"
          },
          {
            "lun": "1",
            "caching": "None",
            "diskSizeGB": "200",
            "storageAccountType": "Standard_LRS"
          }
        ]
      }
    },
    "networkConfiguration": {
      "endpointConfiguration": {
        "inboundNatPools": [
          {
            "name": "testnat",
            "protocol": "TCP",
            "backendPort": "12001",
            "frontendPortRangeStart": "15000",
            "frontendPortRangeEnd": "15100",
            "networkSecurityGroupRules": [
              {
                "access": "Allow",
                "sourceAddressPrefix": "192.100.12.45",
                "priority": "150"
              },
              {
                "access": "Deny",
                "sourceAddressPrefix": "*",
                "priority": "3500"
              }
            ]
          }
        ]
      }
    },
    "scaleSettings": {
      "autoScale": {
        "formula": "$TargetDedicatedNodes=1",
        "evaluationInterval": "PT5M"
      }
    }
  }
}

API_VERSION = '2018-12-01'

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
    request = service_client.put("/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()