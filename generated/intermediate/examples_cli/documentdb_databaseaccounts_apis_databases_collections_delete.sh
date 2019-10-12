# CosmosDBMongoDBCollectionDelete
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
DATABASE_NAME="mydatabase"
COLLECTION_NAME="mycollection"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/databases/$DATABASE_NAME/collections/$COLLECTION_NAME?api-version=2015-04-08