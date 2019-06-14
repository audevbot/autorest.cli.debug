# Get job stream
RESOURCE_GROUP="myresourcegroup"
AUTOMATION_ACCOUNT_NAME="myautomationaccount"
JOB_NAME="myjob"
STREAM_NAME="mystream"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Automation/automationAccounts/$AUTOMATION_ACCOUNT_NAME/jobs/$JOB_NAME/streams/$STREAM_NAME --api-version 2017-05-15-preview