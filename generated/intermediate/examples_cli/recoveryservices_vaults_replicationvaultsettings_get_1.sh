# Gets the vault setting.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_VAULT_SETTING_NAME="myreplicationvaultsetting"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationVaultSettings/$REPLICATION_VAULT_SETTING_NAME --api-version 2018-07-10