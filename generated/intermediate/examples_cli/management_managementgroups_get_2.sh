# GetManagementGroupWithExpand
MANAGEMENT_GROUP_NAME="mymanagementgroup"

az rest --method get --uri /providers/Microsoft.Management/managementGroups/$MANAGEMENT_GROUP_NAME?api-version=2018-03-01-preview