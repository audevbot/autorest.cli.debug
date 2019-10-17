# ApiManagementBackendReconnect
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
BACKEND_NAME="mybackend"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/backends/$BACKEND_NAME/reconnect?api-version=2019-01-01 --body '
{
  "properties": {
    "after": "PT3S"
  }
}
'