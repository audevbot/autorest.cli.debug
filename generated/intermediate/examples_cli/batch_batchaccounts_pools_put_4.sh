# CreatePool - Full VirtualMachineConfiguration
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
POOL_NAME="mypool"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/pools/$POOL_NAME --api-version 2018-12-01 --is-full-object --properties '
{
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
'