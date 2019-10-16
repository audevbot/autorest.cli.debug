# Create a managed disk by importing an unmanaged blob from a different subscription.
RESOURCE_GROUP="myresourcegroup"
DISK_NAME="mydisk"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks/$DISK_NAME?api-version=2018-09-30 --body '
{
  "name": "myDisk",
  "location": "West US",
  "properties": {
    "creationData": {
      "createOption": "Import",
      "storageAccountId": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount",
      "sourceUri": "https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd"
    }
  }
}
'