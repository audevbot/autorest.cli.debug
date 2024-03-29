# ApiManagementCreateApiUsingImportOverrideServiceUrl
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "format": "swagger-link",
    "value": "http://apimpimportviaurl.azurewebsites.net/api/apidocs/",
    "path": "petstoreapi123",
    "serviceUrl": "http://petstore.swagger.wordnik.com/api"
  }
}
'