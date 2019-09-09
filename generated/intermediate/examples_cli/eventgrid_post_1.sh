# EventSubscriptions_GetFullUrlForResourceGroup
{SCOPE}_NAME="myscope"
MICROSOFT.EVENT_GRID_NAME="mymicrosofteventgrid"
{EVENT_SUBSCRIPTION_NAME}_NAME="myeventsubscription"

az rest --method post --uri /{scope}/${SCOPE}_NAME/Microsoft.EventGrid/$MICROSOFT.EVENT_GRID_NAME/{eventSubscriptionName}/${EVENT_SUBSCRIPTION_NAME}_NAME?api-version=2019-01-01 --body '
{}
'