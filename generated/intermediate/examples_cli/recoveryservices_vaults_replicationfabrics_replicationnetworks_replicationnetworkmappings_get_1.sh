# Gets network mapping by name.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_NETWORK_NAME="myreplicationnetwork"
REPLICATION_NETWORK_MAPPING_NAME="myreplicationnetworkmapping"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationNetworks/$REPLICATION_NETWORK_NAME/replicationNetworkMappings/$REPLICATION_NETWORK_MAPPING_NAME --api-version 2018-07-10