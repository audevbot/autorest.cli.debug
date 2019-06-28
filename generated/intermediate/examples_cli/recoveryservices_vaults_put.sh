# Create of Update Recovery Services vault
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME --api-version 2016-06-01 --is-full-object --properties '
{
  "properties": {},
  "sku": {
    "name": "Standard"
  },
  "location": "West US"
}
'