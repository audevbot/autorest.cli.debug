# ApiManagementCreateAuthorizationServer
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
AUTHORIZATION_SERVER_NAME="myauthorizationserver"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/authorizationServers/$AUTHORIZATION_SERVER_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "test2",
    "description": "test server",
    "clientRegistrationEndpoint": "https://www.contoso.com/apps",
    "authorizationEndpoint": "https://www.contoso.com/oauth2/auth",
    "authorizationMethods": [
      "GET"
    ],
    "tokenEndpoint": "https://www.contoso.com/oauth2/token",
    "supportState": True,
    "defaultScope": "read write",
    "grantTypes": [
      "authorizationCode",
      "implicit"
    ],
    "bearerTokenSendingMethods": [
      "authorizationHeader"
    ],
    "clientId": "1",
    "clientSecret": "2",
    "resourceOwnerUsername": "un",
    "resourceOwnerPassword": "pwd"
  }
}
'