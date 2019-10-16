# DisasterRecoveryConfigsAuthorizationRuleGet
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
DISASTER_RECOVERY_CONFIG_NAME="mydisasterrecoveryconfig"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/disasterRecoveryConfigs/$DISASTER_RECOVERY_CONFIG_NAME/AuthorizationRules/$AUTHORIZATION_RULE_NAME?api-version=2017-04-01