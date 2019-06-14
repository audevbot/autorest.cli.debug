# CosmosDBDatabaseAccountCreateMax
RESOURCE_GROUP="myresourcegroup"
DATABASE_ACCOUNT_NAME="mydatabaseaccount"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.DocumentDB/databaseAccounts/$DATABASE_ACCOUNT_NAME --api-version 2015-04-08 --is-full-object --properties '
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
        "ignoreMissingVNetServiceEndpoint": False
      }
    ],
    "locations": [
      {
        "failoverPriority": "0",
        "locationName": "southcentralus"
      },
      {
        "failoverPriority": "1",
        "locationName": "eastus"
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