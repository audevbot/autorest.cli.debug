# EventSubscriptions_ListRegionalByResourceGroup
RESOURCE_GROUP="myresourcegroup"
LOCATION_NAME="mylocation"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/locations/$LOCATION_NAME/eventSubscriptions?api-version=2019-01-01