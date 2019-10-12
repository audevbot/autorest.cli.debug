# CosmosDBGremlinDatabaseCreateUpdate
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
DATABASE_NAME="mydatabase"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/databases/$DATABASE_NAME?api-version=2015-04-08 --body '
{
  "properties": {
    "resource": {
      "id": "databaseName"
    },
    "options": {}
  }
}
'