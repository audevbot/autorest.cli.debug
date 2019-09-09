# CreatePool - Custom Image
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
POOL_NAME="mypool"
IMAGE_NAME="myimage"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/pools/$POOL_NAME?api-version=2018-12-01 --body '
{
  "properties": {
    "vmSize": "STANDARD_D4",
    "deploymentConfiguration": {
      "virtualMachineConfiguration": {
        "imageReference": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/images/" + IMAGE_NAME + ""
        },
        "nodeAgentSkuId": "batch.node.ubuntu 14.04"
      }
    }
  }
}
'