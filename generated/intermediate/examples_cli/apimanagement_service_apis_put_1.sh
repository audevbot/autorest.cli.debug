# ApiManagementCreateApiUsingSwaggerImport
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "format": "swagger-link-json",
    "value": "http://petstore.swagger.io/v2/swagger.json",
    "path": "petstore"
  }
}
'