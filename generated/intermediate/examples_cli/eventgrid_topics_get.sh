# Topics_Get
RESOURCE_GROUP="myresourcegroup"
TOPIC_NAME="mytopic"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/topics/$TOPIC_NAME?api-version=2019-01-01