# Get Recovery Services Resource
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME --api-version 2016-06-01