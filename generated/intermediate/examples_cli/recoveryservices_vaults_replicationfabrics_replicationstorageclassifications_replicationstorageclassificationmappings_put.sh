# Create storage classification mapping.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_STORAGE_CLASSIFICATION_NAME="myreplicationstorageclassification"
REPLICATION_STORAGE_CLASSIFICATION_MAPPING_NAME="myreplicationstorageclassificationmapping"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationStorageClassifications/$REPLICATION_STORAGE_CLASSIFICATION_NAME/replicationStorageClassificationMappings/$REPLICATION_STORAGE_CLASSIFICATION_MAPPING_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "targetStorageClassificationId": "/Subscriptions/9112a37f-0f3e-46ec-9c00-060c6edca071/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/2a48e3770ac08aa2be8bfbd94fcfb1cbf2dcc487b78fb9d3bd778304441b06a0/replicationStorageClassifications/8891569e-aaef-4a46-a4a0-78c14f2d7b09"
  }
}
'