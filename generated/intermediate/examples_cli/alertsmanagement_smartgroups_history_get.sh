# Resolve
SMART_GROUP_NAME="mysmartgroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.AlertsManagement/smartGroups/$SMART_GROUP_NAME/history --api-version 2019-05-05-preview