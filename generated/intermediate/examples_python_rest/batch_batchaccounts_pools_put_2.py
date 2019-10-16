# CreatePool - Full Example
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
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"
SUBNET_NAME = "mysubnet"
APPLICATION_NAME = "myapplication"
CERTIFICATE_NAME = "mycertificate"

BODY = {
  "properties": {
    "displayName": "my-pool-name",
    "vmSize": "STANDARD_D4",
    "interNodeCommunication": "Enabled",
    "maxTasksPerNode": "13",
    "taskSchedulingPolicy": {
      "nodeFillType": "Pack"
    },
    "deploymentConfiguration": {
      "cloudServiceConfiguration": {
        "osFamily": "4",
        "osVersion": "WA-GUEST-OS-4.45_201708-01"
      }
    },
    "networkConfiguration": {
      "subnetId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
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
      "fixedScale": {
        "targetDedicatedNodes": "6",
        "targetLowPriorityNodes": "28",
        "resizeTimeout": "PT8M",
        "nodeDeallocationOption": "TaskCompletion"
      }
    },
    "metadata": [
      {
        "name": "metadata-1",
        "value": "value-1"
      },
      {
        "name": "metadata-2",
        "value": "value-2"
      }
    ],
    "startTask": {
      "commandLine": "cmd /c SET",
      "resourceFiles": [
        {
          "httpUrl": "https://testaccount.blob.core.windows.net/example-blob-file",
          "filePath": "c:\\temp\\gohere",
          "fileMode": "777"
        }
      ],
      "environmentSettings": [
        {
          "name": "MYSET",
          "value": "1234"
        }
      ],
      "userIdentity": {
        "autoUser": {
          "scope": "Pool",
          "elevationLevel": "Admin"
        }
      },
      "maxTaskRetryCount": "6",
      "waitForSuccess": True
    },
    "userAccounts": [
      {
        "name": "username1",
        "password": "examplepassword",
        "elevationLevel": "Admin",
        "linuxUserConfiguration": {
          "sshPrivateKey": "sshprivatekeyvalue",
          "uid": "1234",
          "gid": "4567"
        }
      }
    ],
    "applicationPackages": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/applications/" + APPLICATION_NAME + "",
        "version": "asdf"
      }
    ],
    "certificates": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/certificates/" + CERTIFICATE_NAME + "",
        "storeLocation": "LocalMachine",
        "storeName": "MY",
        "visibility": [
          "RemoteUser"
        ]
      }
    ],
    "applicationLicenses": [
      "app-license0",
      "app-license1"
    ]
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