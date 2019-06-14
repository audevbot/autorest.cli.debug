# MigrationConfigurationsStartMigration
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
MIGRATION_CONFIGURATION_NAME="mymigrationconfiguration"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/migrationConfigurations/$MIGRATION_CONFIGURATION_NAME --api-version 2017-04-01 --is-full-object --properties '
{
  "properties": {
    "targetNamespace": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ServiceBus/namespaces/" + NAMESPACE_NAME + "",
    "postMigrationName": "sdk-PostMigration-5919"
  }
}
'