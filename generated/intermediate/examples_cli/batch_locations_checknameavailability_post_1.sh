# LocationCheckNameAvailability_AlreadyExists
LOCATION_NAME="mylocation"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Batch/locations/$LOCATION_NAME/checkNameAvailability?api-version=2018-12-01 --body '
{
  "name": "existingaccountname",
  "type": "Microsoft.Batch/batchAccounts"
}
'