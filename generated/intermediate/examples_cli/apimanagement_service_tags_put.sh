# ApiManagementCreateTag
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
TAG_NAME="mytag"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/tags/$TAG_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "displayName": "tag1"
  }
}
'