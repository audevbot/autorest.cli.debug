# ApiManagementCreateGroupExternal
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
GROUP_NAME="mygroup"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/groups/$GROUP_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "NewGroup (samiraad.onmicrosoft.com)",
    "description": "new group to test",
    "type": "external",
    "externalId": "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"
  }
}
'