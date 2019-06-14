# ApiManagementCreateApiRelease
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
RELEASE_NAME="myrelease"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/releases/$RELEASE_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "apiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + APIS_NAME + "",
    "notes": "yahooagain"
  }
}
'