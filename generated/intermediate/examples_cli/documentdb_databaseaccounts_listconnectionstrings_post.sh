# CosmosDBDatabaseAccountListConnectionStrings
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/listConnectionStrings?api-version=2015-04-08 --body '
{}
'