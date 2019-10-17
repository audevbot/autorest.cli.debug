# Create or update a simple Gallery Image Version.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
IMAGE_NAME="myimage"
VERSION_NAME="myversion"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/images/$IMAGE_NAME/versions/$VERSION_NAME?api-version=2019-03-01 --body '
{
  "location": "West US",
  "properties": {
    "publishingProfile": {
      "targetRegions": [
        {
          "name": "West US",
          "regional_replica_count": "1"
        },
        {
          "name": "East US",
          "regional_replica_count": "2",
          "storage_account_type": "Standard_ZRS"
        }
      ],
      "source": {
        "managedImage": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/images/" + IMAGE_NAME + ""
        }
      }
    }
  }
}
'