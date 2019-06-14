# CosmosDBTableReplace
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
APIS_NAME="myapis"
TABLE_NAME="mytable"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME/apis/$APIS_NAME/tables/$TABLE_NAME --api-version 2015-04-08 --is-full-object --properties '
{
  "properties": {
    "resource": {
      "id": "tableName"
    },
    "options": {}
  }
}
'