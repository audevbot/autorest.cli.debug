# Topics_Update
RESOURCE_GROUP="myresourcegroup"
TOPIC_NAME="mytopic"

az rest --method patch --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/topics/$TOPIC_NAME?api-version=2019-01-01