# Get ExtendedInfo of Resource
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
EXTENDED_INFORMATION_NAME="myextendedinformation"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/extendedInformation/$EXTENDED_INFORMATION_NAME?api-version=2016-06-01