# CosmosDBDatabaseAccountCreateMax
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME?api-version=2015-04-08 --body '
{
  "location": "westus",
  "tags": {},
  "kind": "GlobalDocumentDB",
  "properties": {
    "databaseAccountOfferType": "Standard",
    "ipRangeFilter": "10.10.10.10",
    "isVirtualNetworkFilterEnabled": True,
    "virtualNetworkRules": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
        "ignore_missing_vnet_service_endpoint": False
      }
    ],
    "locations": [
      {
        "failover_priority": "0",
        "location_name": "southcentralus",
        "is_zone_redundant": False
      },
      {
        "failover_priority": "1",
        "location_name": "eastus",
        "is_zone_redundant": False
      }
    ],
    "consistencyPolicy": {
      "defaultConsistencyLevel": "BoundedStaleness",
      "maxIntervalInSeconds": "10",
      "maxStalenessPrefix": "200"
    }
  }
}
'