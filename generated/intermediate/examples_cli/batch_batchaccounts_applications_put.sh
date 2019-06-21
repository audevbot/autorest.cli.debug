# ApplicationCreate
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
APPLICATION_NAME="myapplication"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/applications/$APPLICATION_NAME --api-version 2018-12-01 --is-full-object --properties '
{
  "properties": {
    "allowUpdates": False,
    "displayName": "myAppName"
  }
}
'