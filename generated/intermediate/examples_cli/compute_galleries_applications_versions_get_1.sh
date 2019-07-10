# Get a gallery Application Version with replication status.
RESOURCE_GROUP="myresourcegroup"
GALLERY_NAME="mygallery"
APPLICATION_NAME="myapplication"
VERSION_NAME="myversion"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/galleries/$GALLERY_NAME/applications/$APPLICATION_NAME/versions/$VERSION_NAME --api-version 2019-03-01