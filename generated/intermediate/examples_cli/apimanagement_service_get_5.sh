# ApiManagementListSubscriptions
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/subscriptions/$SUBSCRIPTION_ID --api-version 2019-01-01