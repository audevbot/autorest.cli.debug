# ApiManagementTenantAccessRegenerateKey
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
TENANT_NAME="mytenant"
GIT_NAME="mygit"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/tenant/$TENANT_NAME/git/$GIT_NAME?api-version=2019-01-01 --body '
{}
'