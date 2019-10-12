# Create a managed disk from a platform image.
RESOURCE_GROUP="myresourcegroup"
DISK_NAME="mydisk"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks/$DISK_NAME?api-version=2018-09-30 --body '
{
  "name": "myDisk",
  "location": "West US",
  "properties": {
    "osType": "Windows",
    "creationData": {
      "createOption": "FromImage",
      "imageReference": {
        "id": "/Subscriptions/{subscriptionId}/Providers/Microsoft.Compute/Locations/uswest/Publishers/Microsoft/ArtifactTypes/VMImage/Offers/{offer}"
      }
    }
  }
}
'