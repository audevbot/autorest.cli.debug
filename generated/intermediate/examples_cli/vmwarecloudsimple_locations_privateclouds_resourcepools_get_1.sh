# GetResourcePool
LOCATION_NAME="mylocation"
PRIVATE_CLOUD_NAME="myprivatecloud"
RESOURCE_POOL_NAME="myresourcepool"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/privateClouds/$PRIVATE_CLOUD_NAME/resourcePools/$RESOURCE_POOL_NAME?api-version=2019-04-01