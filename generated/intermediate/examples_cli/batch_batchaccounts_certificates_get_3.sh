# Get Certificate with Deletion Error
RESOURCE_GROUP="myresourcegroup"
BATCH_ACCOUNT_NAME="mybatchaccount"
CERTIFICATE_NAME="mycertificate"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Batch/batchAccounts/$BATCH_ACCOUNT_NAME/certificates/$CERTIFICATE_NAME?api-version=2018-12-01