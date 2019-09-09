# Delete Routing Rule
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
ROUTING_RULE_NAME="myroutingrule"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/routingRules/$ROUTING_RULE_NAME?api-version=2019-04-01