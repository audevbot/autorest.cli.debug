# Create a managed disk from a platform image.
RESOURCE_GROUP="myresourcegroup"
DISK_NAME="mydisk"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks/$DISK_NAME --api-version 2018-09-30 --is-full-object --properties '
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