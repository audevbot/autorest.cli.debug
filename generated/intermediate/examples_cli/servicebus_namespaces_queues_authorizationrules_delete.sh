# QueueAuthorizationRuleDelete
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
QUEUE_NAME="myqueue"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/queues/$QUEUE_NAME/authorizationRules/$AUTHORIZATION_RULE_NAME?api-version=2015-08-01