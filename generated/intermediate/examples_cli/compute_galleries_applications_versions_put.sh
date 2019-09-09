# Create or update a simple gallery Application Version.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
APPLICATION_NAME="myapplication"
VERSION_NAME="myversion"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/applications/$APPLICATION_NAME/versions/$VERSION_NAME?api-version=2019-03-01 --body '
{
  "location": "West US",
  "properties": {
    "publishingProfile": {
      "source": {
        "fileName": "package.zip",
        "mediaLink": "https://mystorageaccount.blob.core.windows.net/mycontainer/package.zip?{sasKey}"
      },
      "targetRegions": [
        {
          "name": "West US",
          "regionalReplicaCount": "1",
          "storageAccountType": "Standard_LRS"
        }
      ],
      "replicaCount": "1",
      "endOfLifeDate": "2019-07-01T07:00:00Z",
      "storageAccountType": "Standard_LRS"
    }
  }
}
'