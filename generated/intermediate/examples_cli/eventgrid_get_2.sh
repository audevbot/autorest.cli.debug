# EventSubscriptions_GetForResource
{SCOPE}_NAME="myscope"
MICROSOFT.EVENT_GRID_NAME="mymicrosofteventgrid"

az rest --method get --uri /{scope}/${SCOPE}_NAME/Microsoft.EventGrid/$MICROSOFT.EVENT_GRID_NAME/{eventSubscriptionName}?api-version=2019-01-01