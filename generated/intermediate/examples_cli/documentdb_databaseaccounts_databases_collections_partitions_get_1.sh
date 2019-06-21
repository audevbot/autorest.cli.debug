# CosmosDBCollectionGetUsages
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
DATABASE_NAME="mydatabase"
COLLECTION_NAME="mycollection"
PARTITION_NAME="mypartition"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/databases/$DATABASE_NAME/collections/$COLLECTION_NAME/partitions/$PARTITION_NAME --api-version 2015-04-08