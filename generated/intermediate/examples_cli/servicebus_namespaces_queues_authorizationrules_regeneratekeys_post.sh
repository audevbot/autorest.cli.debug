# QueueAuthorizationRuleRegenerateKey
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
QUEUE_NAME="myqueue"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/queues/$QUEUE_NAME/authorizationRules/$AUTHORIZATION_RULE_NAME/regenerateKeys?api-version=2015-08-01 --body '
{
  "keyType": "PrimaryKey"
}
'