# Gets the list of storage classification objects under a fabric.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationStorageClassifications --api-version 2018-07-10