# Topics_Get
RESOURCE_GROUP="myresourcegroup"
TOPIC_NAME="mytopic"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/topics/$TOPIC_NAME --api-version 2019-01-01