# EventSubscriptions_UpdateForResourceGroup
{SCOPE}_NAME="myscope"
MICROSOFT.EVENT_GRID_NAME="mymicrosofteventgrid"
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
EVENTHUB_NAME="myeventhub"

az rest --method patch --uri /{scope}/${SCOPE}_NAME/Microsoft.EventGrid/$MICROSOFT.EVENT_GRID_NAME/{eventSubscriptionName}?api-version=2019-01-01