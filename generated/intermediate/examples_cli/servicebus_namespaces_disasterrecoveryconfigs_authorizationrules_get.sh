# NameSpaceAuthorizationRuleListAll
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
DISASTER_RECOVERY_CONFIG_NAME="mydisasterrecoveryconfig"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/disasterRecoveryConfigs/$DISASTER_RECOVERY_CONFIG_NAME/AuthorizationRules --api-version 2017-04-01