# Delete a gallery image.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
IMAGE_NAME="myimage"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/images/$IMAGE_NAME?api-version=2019-03-01