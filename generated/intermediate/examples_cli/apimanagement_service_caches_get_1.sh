# ApiManagementGetCache
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
CACHE_NAME="mycache"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/caches/$CACHE_NAME?api-version=2019-01-01