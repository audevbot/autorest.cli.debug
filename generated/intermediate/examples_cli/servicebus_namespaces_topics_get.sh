# TopicGet
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/topics?api-version=2017-04-01