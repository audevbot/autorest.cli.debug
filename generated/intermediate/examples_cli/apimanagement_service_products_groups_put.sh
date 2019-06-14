# ApiManagementCreateProductGroup
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PRODUCT_NAME="myproduct"
GROUP_NAME="mygroup"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/products/$PRODUCT_NAME/groups/$GROUP_NAME --api-version 2019-01-01 --is-full-object --properties '
{}
'