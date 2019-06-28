# Put ExtendedInfo of Resource
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
EXTENDED_INFORMATION_NAME="myextendedinformation"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/extendedInformation/$EXTENDED_INFORMATION_NAME --api-version 2016-06-01 --is-full-object --properties '
{
  "properties": {
    "integrityKey": "J99wzS27fmJ+Wjot7xO5wA==",
    "algorithm": "None"
  }
}
'