# TopicAuthorizationRuleListAll
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
TOPIC_NAME="mytopic"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/topics/$TOPIC_NAME/authorizationRules?api-version=2017-04-01