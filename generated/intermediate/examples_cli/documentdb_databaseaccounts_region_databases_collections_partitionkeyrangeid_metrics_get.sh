# CosmosDBDatabaseAccountRegionGetMetrics
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
REGION_NAME="myregion"
DATABASE_NAME="mydatabase"
COLLECTION_NAME="mycollection"
PARTITION_KEY_RANGE_ID_NAME="mypartitionkeyrangeid"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/region/$REGION_NAME/databases/$DATABASE_NAME/collections/$COLLECTION_NAME/partitionKeyRangeId/$PARTITION_KEY_RANGE_ID_NAME/metrics --api-version 2015-04-08