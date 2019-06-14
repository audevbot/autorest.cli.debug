# ApiManagementCreateApi
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "description": "apidescription5200",
    "authenticationSettings": {
      "oAuth2": {
        "authorizationServerId": "authorizationServerId2283",
        "scope": "oauth2scope2580"
      }
    },
    "subscriptionKeyParameterNames": {
      "header": "header4520",
      "query": "query3037"
    },
    "displayName": "apiname1463",
    "serviceUrl": "http://newechoapi.cloudapp.net/api",
    "path": "newapiPath",
    "protocols": [
      "https",
      "http"
    ]
  }
}
'