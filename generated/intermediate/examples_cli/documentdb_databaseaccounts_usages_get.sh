# CosmosDBDatabaseAccountGetUsages
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/usages --api-version 2015-04-08