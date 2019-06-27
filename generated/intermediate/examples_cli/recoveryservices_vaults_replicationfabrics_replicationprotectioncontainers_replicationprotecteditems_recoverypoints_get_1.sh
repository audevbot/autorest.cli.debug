# Get a recovery point.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_PROTECTION_CONTAINER_NAME="myreplicationprotectioncontainer"
REPLICATION_PROTECTED_ITEM_NAME="myreplicationprotecteditem"
RECOVERY_POINT_NAME="myrecoverypoint"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationProtectionContainers/$REPLICATION_PROTECTION_CONTAINER_NAME/replicationProtectedItems/$REPLICATION_PROTECTED_ITEM_NAME/recoveryPoints/$RECOVERY_POINT_NAME --api-version 2018-07-10