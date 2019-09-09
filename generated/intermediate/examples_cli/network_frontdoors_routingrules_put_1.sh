# Create or update specific Redirect Routing Rule
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
ROUTING_RULE_NAME="myroutingrule"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/routingRules/$ROUTING_RULE_NAME?api-version=2019-04-01 --body '
{
  "name": "redirectRoutingRule1",
  "properties": {
    "frontendEndpoints": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
      },
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
      }
    ],
    "acceptedProtocols": [
      "Https"
    ],
    "patternsToMatch": [
      "/*"
    ],
    "routeConfiguration": {
      "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorRedirectConfiguration",
      "redirectType": "Moved",
      "redirectProtocol": "HttpsOnly",
      "customHost": "www.bing.com",
      "customPath": "/api",
      "customFragment": "fragment",
      "customQueryString": "a=b"
    },
    "enabledState": "Enabled"
  }
}
'