# CosmosDBGremlinGraphThroughputUpdate
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
DATABASE_NAME="mydatabase"
GRAPH_NAME="mygraph"
SETTING_NAME="mysetting"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/databases/$DATABASE_NAME/graphs/$GRAPH_NAME/settings/$SETTING_NAME?api-version=2015-04-08 --body '
{
  "properties": {
    "resource": {
      "throughput": "400"
    }
  }
}
'