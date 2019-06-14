# ApplicationPackageGet
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
APPLICATION_NAME="myapplication"
VERSION_NAME="myversion"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/applications/$APPLICATION_NAME/versions/$VERSION_NAME --api-version 2018-12-01