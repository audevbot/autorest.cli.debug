# CosmosDBDatabaseAccountListByResourceGroup
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts?api-version=2015-04-08