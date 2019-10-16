# EventSubscriptions_UpdateForSubscription
EVENT_SUBSCRIPTION_NAME="myeventsubscription"

az rest --method patch --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME?api-version=2019-01-01