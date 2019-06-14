# Create or update specific Forwarding Routing Rule
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
ROUTING_RULE_NAME="myroutingrule"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"
BACKEND_POOL_NAME="mybackendpool"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/routingRules/$ROUTING_RULE_NAME --api-version 2019-04-01 --is-full-object --properties '
{
  "name": "routingRule1",
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
      "Http"
    ],
    "patternsToMatch": [
      "/*"
    ],
    "routeConfiguration": {
      "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",
      "backendPool": {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""
      }
    },
    "enabledState": "Enabled"
  }
}
'