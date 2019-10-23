# Create job
RESOURCE_GROUP="myresourcegroup"
AUTOMATION_ACCOUNT_NAME="myautomationaccount"
JOB_NAME="myjob"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Automation/automationAccounts/$AUTOMATION_ACCOUNT_NAME/jobs/$JOB_NAME?api-version=2017-05-15-preview --body '
{
  "properties": {
    "runbook": {
      "name": "TestRunbook"
    },
    "parameters": {
      "key01": "value01",
      "key02": "value02"
    },
    "runOn": ""
  }
}
'