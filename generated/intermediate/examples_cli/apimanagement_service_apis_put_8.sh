# ApiManagementCreateApiClone
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "displayName": "Echo API2",
    "description": "Copy of Existing Echo Api including Operations.",
    "subscriptionRequired": True,
    "serviceUrl": "http://echoapi.cloudapp.net/api",
    "path": "echo2",
    "protocols": [
      "http",
      "https"
    ],
    "isCurrent": True,
    "sourceApiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + APIS_NAME + ""
  }
}
'