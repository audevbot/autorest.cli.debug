# FrontendEndpoints_EnableHttps
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/frontendEndpoints/$FRONTEND_ENDPOINT_NAME/enableHttps?api-version=2019-04-01 --body '
{
  "certificateSource": "AzureKeyVault",
  "protocolType": "ServerNameIndication",
  "keyVaultCertificateSourceParameters": {
    "vault": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.KeyVault/vaults/" + VAULT_NAME + ""
    },
    "secretName": "secret1",
    "secretVersion": "00000000-0000-0000-0000-000000000000"
  }
}
'