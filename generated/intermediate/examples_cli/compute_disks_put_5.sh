# Create a managed disk by copying a snapshot.
RESOURCE_GROUP="myresourcegroup"
DISK_NAME="mydisk"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks/$DISK_NAME --api-version 2018-09-30 --is-full-object --properties '
{
  "name": "myDisk",
  "location": "West US",
  "properties": {
    "creationData": {
      "createOption": "Copy",
      "sourceResourceId": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot"
    }
  }
}
'