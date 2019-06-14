# ApiManagementCreateApiRevisionFromExistingApi
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "path": "echo",
    "serviceUrl": "http://echoapi.cloudapp.net/apiv3",
    "sourceApiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + APIS_NAME + "",
    "apiRevisionDescription": "Creating a Revision of an existing API"
  }
}
'