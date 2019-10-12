# List software update configurations
RESOURCE_GROUP="myresourcegroup"
AUTOMATION_ACCOUNT_NAME="myautomationaccount"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Automation/automationAccounts/$AUTOMATION_ACCOUNT_NAME/softwareUpdateConfigurations?api-version=2017-05-15-preview