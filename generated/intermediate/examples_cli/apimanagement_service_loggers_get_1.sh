# ApiManagementGetLogger
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
LOGGER_NAME="mylogger"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/loggers/$LOGGER_NAME --api-version 2019-01-01