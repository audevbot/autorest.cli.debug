# Gets a recovery point for a migration item.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_PROTECTION_CONTAINER_NAME="myreplicationprotectioncontainer"
REPLICATION_MIGRATION_ITEM_NAME="myreplicationmigrationitem"
MIGRATION_RECOVERY_POINT_NAME="mymigrationrecoverypoint"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationProtectionContainers/$REPLICATION_PROTECTION_CONTAINER_NAME/replicationMigrationItems/$REPLICATION_MIGRATION_ITEM_NAME/migrationRecoveryPoints/$MIGRATION_RECOVERY_POINT_NAME --api-version 2018-07-10