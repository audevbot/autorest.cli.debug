# ApiManagementCreateApiUsingWadlImport
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "format": "wadl-link-json",
    "value": "https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl",
    "path": "collector"
  }
}
'