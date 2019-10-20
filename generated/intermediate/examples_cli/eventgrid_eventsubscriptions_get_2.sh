# EventSubscriptions_GetForResource
EVENT_SUBSCRIPTION_NAME="myeventsubscription"

az rest --method get --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME?api-version=2019-01-01