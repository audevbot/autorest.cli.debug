# ApiManagementGetPolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
POLICY_NAME="mypolicy"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/policies/$POLICY_NAME --api-version 2019-01-01