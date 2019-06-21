# CreatePool - Minimal VirtualMachineConfiguration
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
          "publisher": "Canonical",
          "offer": "UbuntuServer",
          "sku": "14.04.5-LTS",
          "version": "latest"
        },
        "nodeAgentSkuId": "batch.node.ubuntu 14.04"
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