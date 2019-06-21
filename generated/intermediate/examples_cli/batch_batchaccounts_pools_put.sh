# CreatePool - Minimal CloudServiceConfiguration
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
POOL_NAME="mypool"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/pools/$POOL_NAME --api-version 2018-12-01 --is-full-object --properties '
{
  "properties": {
    "vmSize": "STANDARD_D4",
    "deploymentConfiguration": {
      "cloudServiceConfiguration": {
        "osFamily": "5"
      }
    },
    "scaleSettings": {
      "fixedScale": {
        "targetDedicatedNodes": "3"
      }
    }
  }
}
'