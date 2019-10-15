# ApiManagementServiceGetNetworkStatusByLocation
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
LOCATION_NAME="mylocation"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/locations/$LOCATION_NAME/networkstatus?api-version=2019-01-01