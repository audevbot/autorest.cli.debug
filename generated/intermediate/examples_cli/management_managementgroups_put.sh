# PutManagementGroup
MANAGEMENT_GROUP_NAME="mymanagementgroup"

az resource create --id /providers/Microsoft.Management/managementGroups/$MANAGEMENT_GROUP_NAME --api-version 2018-03-01-preview --is-full-object --properties '
{
  "id": "/providers/Microsoft.Management/managementGroups/ChildGroup",
  "type": "/providers/Microsoft.Management/managementGroups",
  "name": "ChildGroup",
  "properties": {
    "tenantId": "20000000-0000-0000-0000-000000000000",
    "displayName": "ChildGroup",
    "details": {
      "parent": {
        "id": "/providers/Microsoft.Management/managementGroups/RootGroup"
      }
    }
  }
}
'