# SBAliasCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
DISASTER_RECOVERY_CONFIG_NAME="mydisasterrecoveryconfig"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/disasterRecoveryConfigs/$DISASTER_RECOVERY_CONFIG_NAME --api-version 2017-04-01 --is-full-object --properties '
{
  "properties": {
    "partnerNamespace": "sdk-Namespace-37",
    "alternateName": "alternameforAlias-Namespace-8860"
  }
}
'