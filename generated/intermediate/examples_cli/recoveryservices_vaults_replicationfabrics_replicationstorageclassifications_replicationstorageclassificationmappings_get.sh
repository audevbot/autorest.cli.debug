# Gets the list of storage classification mappings objects under a storage.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_STORAGE_CLASSIFICATION_NAME="myreplicationstorageclassification"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationStorageClassifications/$REPLICATION_STORAGE_CLASSIFICATION_NAME/replicationStorageClassificationMappings --api-version 2018-07-10