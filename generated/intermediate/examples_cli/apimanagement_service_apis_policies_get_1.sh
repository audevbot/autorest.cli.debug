# ApiManagementGetApiPolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
POLICY_NAME="mypolicy"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/policies/$POLICY_NAME?api-version=2019-01-01