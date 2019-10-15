# CosmosDBDatabaseAccountCreateMin
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME?api-version=2015-04-08 --body '
{
  "location": "westus",
  "properties": {
    "databaseAccountOfferType": "Standard",
    "locations": [
      {
        "failover_priority": "0",
        "location_name": "southcentralus",
        "is_zone_redundant": False
      }
    ]
  }
}
'