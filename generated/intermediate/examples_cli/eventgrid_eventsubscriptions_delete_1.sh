# EventSubscriptions_DeleteForResourceGroup
EVENT_SUBSCRIPTION_NAME="myeventsubscription"

az rest --method delete --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME?api-version=2019-01-01