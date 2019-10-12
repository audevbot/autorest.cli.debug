# ApiManagementPortalSettingsUpdateSignUp
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/portalsettings/signup?api-version=2019-01-01 --body '
{
  "properties": {
    "enabled": True,
    "termsOfService": {
      "enabled": True,
      "text": "Terms of service text.",
      "consentRequired": True
    }
  }
}
'