# NameSpaceAuthorizationRuleGet
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/AuthorizationRules/$AUTHORIZATION_RULE_NAME --api-version 2017-04-01