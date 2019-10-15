# List gallery Application Versions in a gallery Application Definition.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
APPLICATION_NAME="myapplication"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/applications/$APPLICATION_NAME/versions?api-version=2019-03-01