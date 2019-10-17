# ApiManagementCreateApi
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME?api-version=2019-01-01 --body '
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