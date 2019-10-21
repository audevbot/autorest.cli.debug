# BatchAccountCreate_Default
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
STORAGE_ACCOUNT_NAME="mystorageaccount"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME?api-version=2018-12-01 --body '
{
  "location": "japaneast",
  "properties": {
    "autoStorage": {
      "storageAccountId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
    }
  }
}
'