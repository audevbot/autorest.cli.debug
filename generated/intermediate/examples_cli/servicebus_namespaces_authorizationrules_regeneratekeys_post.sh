# NameSpaceAuthorizationRuleRegenerateKey
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/AuthorizationRules/$AUTHORIZATION_RULE_NAME/regenerateKeys?api-version=2017-04-01 --body '
{
  "keyType": "PrimaryKey"
}
'