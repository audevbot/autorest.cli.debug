# ApiManagementCreateApiNewVersionUsingExistingApi
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
API_VERSION_SET_NAME="myapiversionset"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "Echo API2",
    "description": "Create Echo API into a new Version using Existing Version Set and Copy all Operations.",
    "subscriptionRequired": True,
    "serviceUrl": "http://echoapi.cloudapp.net/api",
    "path": "echo2",
    "protocols": [
      "http",
      "https"
    ],
    "isCurrent": True,
    "apiVersion": "v4",
    "sourceApiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
    "apiVersionSetId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apiVersionSets/" + API_VERSION_SET_NAME + ""
  }
}
'