# ApiManagementCreateProduct
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PRODUCT_NAME="myproduct"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/products/$PRODUCT_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "displayName": "Test Template ProductName 4"
  }
}
'