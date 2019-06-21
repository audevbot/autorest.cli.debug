# BatchAccountCreate_Default
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
STORAGE_ACCOUNT_NAME="mystorageaccount"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME --api-version 2018-12-01 --is-full-object --properties '
{
  "location": "japaneast",
  "properties": {
    "autoStorage": {
      "storageAccountId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
    }
  }
}
'