# Suspend job
RESOURCE_GROUP="myresourcegroup"
AUTOMATION_ACCOUNT_NAME="myautomationaccount"
JOB_NAME="myjob"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Automation/automationAccounts/$AUTOMATION_ACCOUNT_NAME/jobs/$JOB_NAME/suspend?api-version=2017-05-15-preview --body '
{}
'