# Get Backend Pool
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
BACKEND_POOL_NAME="mybackendpool"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/backendPools/$BACKEND_POOL_NAME?api-version=2019-04-01