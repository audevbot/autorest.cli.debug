# CreatePool - Full VirtualMachineConfiguration
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
POOL_NAME="mypool"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/pools/$POOL_NAME?api-version=2018-12-01 --body '
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
            "disk_size_gb": "30",
            "storage_account_type": "Premium_LRS"
          },
          {
            "lun": "1",
            "caching": "None",
            "disk_size_gb": "200",
            "storage_account_type": "Standard_LRS"
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
            "backend_port": "12001",
            "frontend_port_range_start": "15000",
            "frontend_port_range_end": "15100",
            "network_security_group_rules": [
              {
                "access": "Allow",
                "source_address_prefix": "192.100.12.45",
                "priority": "150"
              },
              {
                "access": "Deny",
                "source_address_prefix": "*",
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