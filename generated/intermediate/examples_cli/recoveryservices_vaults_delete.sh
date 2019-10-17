# Delete Recovery Services Vault
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME?api-version=2016-06-01