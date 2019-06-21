# CreateCertificate - Minimal Pfx
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
CERTIFICATE_NAME="mycertificate"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/certificates/$CERTIFICATE_NAME --api-version 2018-12-01 --is-full-object --properties '
{
  "properties": {
    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
    "password": "KG0UY40e..."
  }
}
'