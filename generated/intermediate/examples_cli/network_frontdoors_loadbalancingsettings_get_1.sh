# Get LoadBalancingSettings
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
LOAD_BALANCING_SETTING_NAME="myloadbalancingsetting"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/loadBalancingSettings/$LOAD_BALANCING_SETTING_NAME --api-version 2019-04-01