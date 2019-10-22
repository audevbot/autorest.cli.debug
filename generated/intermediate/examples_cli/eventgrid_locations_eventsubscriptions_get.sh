# EventSubscriptions_ListRegionalBySubscription
LOCATION_NAME="mylocation"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.EventGrid/locations/$LOCATION_NAME/eventSubscriptions?api-version=2019-01-01