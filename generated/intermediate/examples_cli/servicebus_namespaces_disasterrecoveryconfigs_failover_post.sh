# SBAliasFailOver
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
DISASTER_RECOVERY_CONFIG_NAME="mydisasterrecoveryconfig"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/disasterRecoveryConfigs/$DISASTER_RECOVERY_CONFIG_NAME/failover?api-version=2017-04-01 --body '
{}
'