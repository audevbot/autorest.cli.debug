# List LoadBalancingSettings in a Front Door
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/loadBalancingSettings --api-version 2019-04-01