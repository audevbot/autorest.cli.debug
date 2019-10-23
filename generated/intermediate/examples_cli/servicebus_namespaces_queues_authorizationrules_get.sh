# QueueAuthorizationRuleListAll
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
QUEUE_NAME="myqueue"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/queues/$QUEUE_NAME/authorizationRules?api-version=2017-04-01