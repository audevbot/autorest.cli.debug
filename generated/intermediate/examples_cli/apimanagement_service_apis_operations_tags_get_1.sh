# ApiManagementGetApiOperationTag
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
OPERATION_NAME="myoperation"
TAG_NAME="mytag"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/operations/$OPERATION_NAME/tags/$TAG_NAME --api-version 2019-01-01