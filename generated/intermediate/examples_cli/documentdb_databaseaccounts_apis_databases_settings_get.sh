# CosmosDBSqlDatabaseThroughputGet
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
DATABASE_NAME="mydatabase"
SETTING_NAME="mysetting"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/databases/$DATABASE_NAME/settings/$SETTING_NAME --api-version 2015-04-08