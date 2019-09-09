# GetPrivateCloud
LOCATION_NAME="mylocation"
PRIVATE_CLOUD_NAME="myprivatecloud"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/privateClouds/$PRIVATE_CLOUD_NAME?api-version=2019-04-01