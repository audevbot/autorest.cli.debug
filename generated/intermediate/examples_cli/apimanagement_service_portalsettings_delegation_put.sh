# ApiManagementPortalSettingsUpdateDelegation
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/portalsettings/delegation?api-version=2019-01-01 --body '
{
  "properties": {
    "url": "http://contoso.com/delegation",
    "validationKey": "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==",
    "subscriptions": {
      "enabled": True
    },
    "userRegistration": {
      "enabled": True
    }
  }
}
'