# CreateCertificate - Minimal Cer
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
CERTIFICATE_NAME="mycertificate"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/certificates/$CERTIFICATE_NAME?api-version=2018-12-01 --body '
{
  "properties": {
    "data": "MIICrjCCAZagAwI...",
    "format": "Cer"
  }
}
'