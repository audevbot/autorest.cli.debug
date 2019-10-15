# EventSubscriptions_UpdateForResourceGroup
EVENT_SUBSCRIPTION_NAME="myeventsubscription"
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
EVENTHUB_NAME="myeventhub"

az rest --method patch --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME?api-version=2019-01-01