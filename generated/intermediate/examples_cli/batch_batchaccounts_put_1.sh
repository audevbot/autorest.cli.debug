# BatchAccountCreate_BYOS
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
STORAGE_ACCOUNT_NAME="mystorageaccount"
VAULT_NAME="myvault"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME --api-version 2018-12-01 --is-full-object --properties '
{
  "location": "japaneast",
  "properties": {
    "autoStorage": {
      "storageAccountId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
    },
    "poolAllocationMode": "UserSubscription",
    "keyVaultReference": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.KeyVault/vaults/" + VAULT_NAME + "",
      "url": "http://sample.vault.azure.net/"
    }
  }
}
'