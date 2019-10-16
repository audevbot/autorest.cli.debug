# CosmosDBDatabaseAccountRegionGetMetrics
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
SOURCE_REGION_NAME="mysourceregion"
TARGET_REGION_NAME="mytargetregion"
PERCENTILE_NAME="mypercentile"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/sourceRegion/$SOURCE_REGION_NAME/targetRegion/$TARGET_REGION_NAME/percentile/$PERCENTILE_NAME?api-version=2015-04-08