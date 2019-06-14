# CreatePool - Full Example
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
POOL_NAME="mypool"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"
APPLICATION_NAME="myapplication"
CERTIFICATE_NAME="mycertificate"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/pools/$POOL_NAME --api-version 2018-12-01 --is-full-object --properties '
{
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
'