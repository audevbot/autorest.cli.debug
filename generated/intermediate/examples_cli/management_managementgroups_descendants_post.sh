# GetDescendants
MANAGEMENT_GROUP_NAME="mymanagementgroup"

az rest --method post --uri /providers/Microsoft.Management/managementGroups/$MANAGEMENT_GROUP_NAME/descendants?api-version=2018-03-01-preview --body '
{}
'