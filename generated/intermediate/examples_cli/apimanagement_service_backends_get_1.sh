# ApiManagementGetBackend
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
BACKEND_NAME="mybackend"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/backends/$BACKEND_NAME --api-version 2019-01-01