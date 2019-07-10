# List gallery Application Versions in a gallery Application Definition.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
APPLICATION_NAME="myapplication"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/applications/$APPLICATION_NAME/versions --api-version 2019-03-01