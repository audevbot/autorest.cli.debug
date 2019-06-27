# Enables migration.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_PROTECTION_CONTAINER_NAME="myreplicationprotectioncontainer"
REPLICATION_MIGRATION_ITEM_NAME="myreplicationmigrationitem"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationProtectionContainers/$REPLICATION_PROTECTION_CONTAINER_NAME/replicationMigrationItems/$REPLICATION_MIGRATION_ITEM_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "policyId": "/Subscriptions/cb53d0c3-bd59-4721-89bc-06916a9147ef/resourceGroups/resourcegroup1/providers/Microsoft.RecoveryServices/vaults/migrationvault/replicationPolicies/vmwarepolicy1",
    "providerSpecificDetails": {
      "instanceType": "VMwareCbt"
    }
  }
}
'