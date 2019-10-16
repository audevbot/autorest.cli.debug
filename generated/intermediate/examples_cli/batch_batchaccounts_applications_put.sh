# ApplicationCreate
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
APPLICATION_NAME="myapplication"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/applications/$APPLICATION_NAME?api-version=2018-12-01 --body '
{
  "properties": {
    "allowUpdates": False,
    "displayName": "myAppName"
  }
}
'