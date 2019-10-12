# ApiManagementCreateApiWithOpenIdConnect
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "Swagger Petstore",
    "description": "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.",
    "serviceUrl": "http://petstore.swagger.io/v2",
    "path": "petstore",
    "protocols": [
      "https"
    ],
    "authenticationSettings": {
      "openid": {
        "openidProviderId": "testopenid",
        "bearerTokenSendingMethods": [
          "authorizationHeader"
        ]
      }
    },
    "subscriptionKeyParameterNames": {
      "header": "Ocp-Apim-Subscription-Key",
      "query": "subscription-key"
    }
  }
}
'