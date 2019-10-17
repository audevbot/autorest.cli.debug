# FrontendEndpoints_DisableHttps
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/frontendEndpoints/$FRONTEND_ENDPOINT_NAME/disableHttps?api-version=2019-04-01 --body '
{}
'