# AddSubscriptionToManagementGroup
MANAGEMENT_GROUP_NAME="mymanagementgroup"

az rest --method put --uri /providers/Microsoft.Management/managementGroups/$MANAGEMENT_GROUP_NAME/subscriptions/$SUBSCRIPTION_ID?api-version=2018-03-01-preview --body '
{}
'