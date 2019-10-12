# ApiManagementUpdateBackend
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
BACKEND_NAME="mybackend"

az rest --method patch --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/backends/$BACKEND_NAME?api-version=2019-01-01