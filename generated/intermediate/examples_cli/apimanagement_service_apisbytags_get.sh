# ApiManagementListApisByTags
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apisByTags?api-version=2019-01-01