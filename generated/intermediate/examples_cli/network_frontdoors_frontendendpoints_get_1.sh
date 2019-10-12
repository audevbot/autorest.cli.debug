# Get Frontend Endpoint
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/frontendEndpoints/$FRONTEND_ENDPOINT_NAME?api-version=2019-04-01