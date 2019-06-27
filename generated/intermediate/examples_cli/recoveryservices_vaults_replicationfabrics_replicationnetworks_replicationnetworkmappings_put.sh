# Creates network mapping.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_NETWORK_NAME="myreplicationnetwork"
REPLICATION_NETWORK_MAPPING_NAME="myreplicationnetworkmapping"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationNetworks/$REPLICATION_NETWORK_NAME/replicationNetworkMappings/$REPLICATION_NETWORK_MAPPING_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "recoveryFabricName": "Microsoft Azure",
    "recoveryNetworkId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "",
    "fabricSpecificDetails": {
      "instanceType": "VmmToAzure"
    }
  }
}
'