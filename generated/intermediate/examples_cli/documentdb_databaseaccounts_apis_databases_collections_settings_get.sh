# CosmosDBMongoDBCollectionThroughputGet
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
APIS_NAME="myapis"
DATABASE_NAME="mydatabase"
COLLECTION_NAME="mycollection"
SETTING_NAME="mysetting"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$APIS_NAME/databases/$DATABASE_NAME/collections/$COLLECTION_NAME/settings/$SETTING_NAME --api-version 2015-04-08