# NameSpaceCheckNameAvailability

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.ServiceBus/CheckNameAvailability?api-version=2017-04-01 --body '
{
  "name": "sdk-Namespace-2924"
}
'