# ApiManagementGetGroup
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
GROUP_NAME="mygroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/groups/$GROUP_NAME --api-version 2019-01-01