# Gets the details of a recovery services provider.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_RECOVERY_SERVICES_PROVIDER_NAME="myreplicationrecoveryservicesprovider"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationRecoveryServicesProviders/$REPLICATION_RECOVERY_SERVICES_PROVIDER_NAME --api-version 2018-07-10