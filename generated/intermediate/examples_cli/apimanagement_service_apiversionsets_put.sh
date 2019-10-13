# ApiManagementCreateApiVersionSet
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_VERSION_SET_NAME="myapiversionset"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apiVersionSets/$API_VERSION_SET_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "api set 1",
    "versioningScheme": "Segment",
    "description": "Version configuration"
  }
}
'