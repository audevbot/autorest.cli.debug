# ApiManagementListProductSubscriptions
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PRODUCT_NAME="myproduct"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/products/$PRODUCT_NAME/subscriptions/$SUBSCRIPTION_ID?api-version=2019-01-01