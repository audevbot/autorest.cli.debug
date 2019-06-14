# Create or update a simple gallery.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME --api-version 2019-03-01 --is-full-object --properties '
{
  "location": "West US",
  "properties": {
    "description": "This is the gallery description."
  }
}
'