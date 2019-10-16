# MigrationConfigurationsRevert
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
MIGRATION_CONFIGURATION_NAME="mymigrationconfiguration"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/migrationConfigurations/$MIGRATION_CONFIGURATION_NAME/revert?api-version=2017-04-01 --body '
{}
'