# ApiManagementDeleteProductApi
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PRODUCT_NAME="myproduct"
API_NAME="myapi"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/products/$PRODUCT_NAME/apis/$API_NAME?api-version=2019-01-01