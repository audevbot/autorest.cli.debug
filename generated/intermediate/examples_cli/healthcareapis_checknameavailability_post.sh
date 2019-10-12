# Check name availability

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.HealthcareApis/checkNameAvailability?api-version=2019-09-16 --body '
{
  "type": "Microsoft.HealthcareApis/services",
  "name": "serviceName"
}
'