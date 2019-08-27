# Create a snapshot from an existing snapshot in the same or a different subscription.
RESOURCE_GROUP="myresourcegroup"
SNAPSHOT_NAME="mysnapshot"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/snapshots/$SNAPSHOT_NAME --api-version 2018-09-30 --is-full-object --properties '
{
  "name": "mySnapshot2",
  "location": "West US",
  "properties": {
    "creationData": {
      "createOption": "Copy",
      "sourceResourceId": "subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot1"
    }
  }
}
'