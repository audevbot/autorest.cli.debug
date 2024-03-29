# Get software update configuration by name
RESOURCE_GROUP="myresourcegroup"
AUTOMATION_ACCOUNT_NAME="myautomationaccount"
SOFTWARE_UPDATE_CONFIGURATION_NAME="mysoftwareupdateconfiguration"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Automation/automationAccounts/$AUTOMATION_ACCOUNT_NAME/softwareUpdateConfigurations/$SOFTWARE_UPDATE_CONFIGURATION_NAME --api-version 2017-05-15-preview