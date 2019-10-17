# ApiManagementTenantAccessSyncState
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
TENANT_NAME="mytenant"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/tenant/$TENANT_NAME/syncState?api-version=2019-01-01