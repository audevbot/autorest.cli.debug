# Gets a logical network with specified server id and logical network name.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_LOGICAL_NETWORK_NAME="myreplicationlogicalnetwork"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationLogicalNetworks/$REPLICATION_LOGICAL_NETWORK_NAME --api-version 2018-07-10