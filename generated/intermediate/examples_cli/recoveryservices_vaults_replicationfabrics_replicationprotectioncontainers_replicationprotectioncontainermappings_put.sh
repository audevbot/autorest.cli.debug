# Create protection container mapping.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_PROTECTION_CONTAINER_NAME="myreplicationprotectioncontainer"
REPLICATION_PROTECTION_CONTAINER_MAPPING_NAME="myreplicationprotectioncontainermapping"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationProtectionContainers/$REPLICATION_PROTECTION_CONTAINER_NAME/replicationProtectionContainerMappings/$REPLICATION_PROTECTION_CONTAINER_MAPPING_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "targetProtectionContainerId": "Microsoft Azure",
    "policyId": "/Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationPolicies/protectionprofile1",
    "providerSpecificInput": {}
  }
}
'