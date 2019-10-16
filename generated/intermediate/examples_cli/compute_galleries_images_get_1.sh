# List gallery images in a gallery.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/images?api-version=2019-03-01