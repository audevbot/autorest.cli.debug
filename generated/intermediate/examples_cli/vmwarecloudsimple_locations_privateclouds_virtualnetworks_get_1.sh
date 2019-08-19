# GetVirtualNetwork
LOCATION_NAME="mylocation"
PRIVATE_CLOUD_NAME="myprivatecloud"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/privateClouds/$PRIVATE_CLOUD_NAME/virtualNetworks/$VIRTUAL_NETWORK_NAME --api-version 2019-04-01