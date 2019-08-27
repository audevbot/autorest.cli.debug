# Create a snapshot by importing an unmanaged blob from a different subscription.
RESOURCE_GROUP="myresourcegroup"
SNAPSHOT_NAME="mysnapshot"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/snapshots/$SNAPSHOT_NAME --api-version 2018-09-30 --is-full-object --properties '
{
  "name": "mySnapshot1",
  "location": "West US",
  "properties": {
    "creationData": {
      "createOption": "Import",
      "storageAccountId": "subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount",
      "sourceUri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"
    }
  }
}
'