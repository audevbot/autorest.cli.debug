# ApiManagementServiceCheckNameAvailability

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.ApiManagement/checkNameAvailability?api-version=2019-01-01 --body '
{
  "name": "apimService1"
}
'