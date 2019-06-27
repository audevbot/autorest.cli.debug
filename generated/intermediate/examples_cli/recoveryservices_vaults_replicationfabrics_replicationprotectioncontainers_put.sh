# Create a protection container.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_PROTECTION_CONTAINER_NAME="myreplicationprotectioncontainer"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationProtectionContainers/$REPLICATION_PROTECTION_CONTAINER_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "providerSpecificInput": [
      {
        "instanceType": "ReplicationProviderSpecificContainerCreationInput"
      }
    ]
  }
}
'