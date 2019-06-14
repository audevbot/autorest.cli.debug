# ApiManagementGetEmailTemplate
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
TEMPLATE_NAME="mytemplate"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/templates/$TEMPLATE_NAME --api-version 2019-01-01