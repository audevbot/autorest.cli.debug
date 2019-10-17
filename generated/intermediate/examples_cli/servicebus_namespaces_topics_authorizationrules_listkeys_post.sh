# TopicAuthorizationRuleListKey
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
TOPIC_NAME="mytopic"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/topics/$TOPIC_NAME/authorizationRules/$AUTHORIZATION_RULE_NAME/ListKeys?api-version=2015-08-01 --body '
{}
'