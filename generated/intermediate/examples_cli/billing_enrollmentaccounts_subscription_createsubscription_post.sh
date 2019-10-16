# createSubscription
ENROLLMENT_ACCOUNT_NAME="myenrollmentaccount"

az rest --method post --uri /providers/Microsoft.Billing/enrollmentAccounts/$ENROLLMENT_ACCOUNT_NAME/providers/Microsoft.Subscription/createSubscription?api-version=2018-03-01-preview --body '
{
  "offerType": "MS-AZR-0017P",
  "displayName": "Test Ea Azure Sub",
  "owners": [
    {
      "object_id": "973034ff-acb7-409c-b731-e789672c7b31"
    },
    {
      "object_id": "67439a9e-8519-4016-a630-f5f805eba567"
    }
  ],
  "additionalParameters": {
    "customData": {
      "key1": "value1",
      "key2": True
    }
  }
}
'