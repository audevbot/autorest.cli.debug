# CosmosDBCassandraTableList
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
KEYSPACE_NAME="mykeyspace"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/keyspaces/$KEYSPACE_NAME/tables --api-version 2015-04-08