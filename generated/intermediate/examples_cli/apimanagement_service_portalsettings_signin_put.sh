# ApiManagementPortalSettingsUpdateSignIn
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/portalsettings/signin --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "enabled": True
  }
}
'