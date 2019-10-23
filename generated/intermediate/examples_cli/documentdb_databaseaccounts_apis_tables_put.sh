# CosmosDBTableReplace
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
API_NAME="myapi"
TABLE_NAME="mytable"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$API_NAME/tables/$TABLE_NAME?api-version=2015-04-08 --body '
{
  "properties": {
    "resource": {
      "id": "tableName"
    },
    "options": {}
  }
}
'