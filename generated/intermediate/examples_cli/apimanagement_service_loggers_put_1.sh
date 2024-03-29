# ApiManagementCreateAILogger
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
LOGGER_NAME="mylogger"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/loggers/$LOGGER_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "loggerType": "applicationInsights",
    "description": "adding a new logger",
    "credentials": {
      "instrumentationKey": "11................a1"
    }
  }
}
'