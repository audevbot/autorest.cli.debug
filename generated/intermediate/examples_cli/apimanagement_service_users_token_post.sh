# ApiManagementUserToken
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
USER_NAME="myuser"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/users/$USER_NAME/token?api-version=2019-01-01 --body '
{
  "properties": {
    "keyType": "primary",
    "expiry": "2019-04-21T00:44:24.2845269Z"
  }
}
'