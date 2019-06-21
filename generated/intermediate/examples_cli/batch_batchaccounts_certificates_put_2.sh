# CreateCertificate - Full
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
CERTIFICATE_NAME="mycertificate"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/certificates/$CERTIFICATE_NAME --api-version 2018-12-01 --is-full-object --properties '
{
  "properties": {
    "thumbprintAlgorithm": "SHA1",
    "thumbprint": "0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E",
    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
    "password": "KG0UY40e...",
    "format": "Pfx"
  }
}
'