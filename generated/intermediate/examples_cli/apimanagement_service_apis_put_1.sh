# ApiManagementCreateApiUsingSwaggerImport
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "format": "swagger-link-json",
    "value": "http://petstore.swagger.io/v2/swagger.json",
    "path": "petstore"
  }
}
'