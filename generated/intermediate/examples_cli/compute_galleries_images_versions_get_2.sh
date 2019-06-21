# List gallery Image Versions in a gallery Image Definition.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
IMAGE_NAME="myimage"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/images/$IMAGE_NAME/versions --api-version 2019-03-01