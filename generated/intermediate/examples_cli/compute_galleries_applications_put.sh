# Create or update a simple gallery Application.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
APPLICATION_NAME="myapplication"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/applications/$APPLICATION_NAME --api-version 2019-03-01 --is-full-object --properties '
{
  "location": "West US",
  "properties": {
    "description": "This is the gallery application description.",
    "eula": "This is the gallery application EULA.",
    "privacyStatementUri": "myPrivacyStatementUri}",
    "releaseNoteUri": "myReleaseNoteUri",
    "supportedOSType": "Windows"
  }
}
'