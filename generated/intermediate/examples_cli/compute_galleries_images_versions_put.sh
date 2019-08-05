# Create or update a simple Gallery Image Version.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
IMAGE_NAME="myimage"
VERSION_NAME="myversion"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/images/$IMAGE_NAME/versions/$VERSION_NAME --api-version 2019-03-01 --is-full-object --properties '
{
  "location": "West US",
  "properties": {
    "publishingProfile": {
      "targetRegions": [
        {
          "name": "West US",
          "regionalReplicaCount": "1"
        },
        {
          "name": "East US",
          "regionalReplicaCount": "2",
          "storageAccountType": "Standard_ZRS"
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