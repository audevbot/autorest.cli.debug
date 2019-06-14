# ApiManagementCreateProductTag
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PRODUCT_NAME="myproduct"
TAG_NAME="mytag"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/products/$PRODUCT_NAME/tags/$TAG_NAME --api-version 2019-01-01 --is-full-object --properties '
{}
'