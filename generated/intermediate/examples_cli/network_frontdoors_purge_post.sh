# Purge content from Front Door
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/purge?api-version=2019-04-01 --body '
{
  "contentPaths": [
    "/pictures.aspx",
    "/pictures/*"
  ]
}
'