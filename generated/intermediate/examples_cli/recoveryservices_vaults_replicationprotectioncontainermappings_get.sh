# Gets the list of all protection container mappings in a vault.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationProtectionContainerMappings --api-version 2018-07-10