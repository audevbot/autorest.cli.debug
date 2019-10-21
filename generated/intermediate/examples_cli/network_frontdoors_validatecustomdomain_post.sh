# FrontDoor_ValidateCustomDomain
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/validateCustomDomain?api-version=2019-04-01 --body '
{
  "hostName": "www.someDomain.com"
}
'