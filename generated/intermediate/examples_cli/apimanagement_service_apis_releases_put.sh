# ApiManagementCreateApiRelease
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
RELEASE_NAME="myrelease"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/releases/$RELEASE_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "apiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
    "notes": "yahooagain"
  }
}
'