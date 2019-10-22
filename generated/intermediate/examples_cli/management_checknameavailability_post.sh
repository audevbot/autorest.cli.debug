# CheckManagementGroupNameAvailability

az rest --method post --uri /providers/Microsoft.Management/checkNameAvailability?api-version=2018-03-01-preview --body '
{
  "name": "nameTocheck",
  "type": "/providers/Microsoft.Management/managementGroups"
}
'