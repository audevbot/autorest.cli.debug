# ListPrivateCloudInLocation
LOCATION_NAME="mylocation"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/privateClouds?api-version=2019-04-01