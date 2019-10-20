# Create or update a simple gallery.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME?api-version=2019-03-01 --body '
{
  "location": "West US",
  "properties": {
    "description": "This is the gallery description."
  }
}
'