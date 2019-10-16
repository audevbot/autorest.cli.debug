# Create a managed disk from an existing managed disk in the same or different subscription.
RESOURCE_GROUP="myresourcegroup"
DISK_NAME="mydisk"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks/$DISK_NAME?api-version=2018-09-30 --body '
{
  "name": "myDisk2",
  "location": "West US",
  "properties": {
    "creationData": {
      "createOption": "Copy",
      "sourceResourceId": "subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myDisk1"
    }
  }
}
'