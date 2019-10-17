# ApiManagementDeleteApiVersionSet
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_VERSION_SET_NAME="myapiversionset"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apiVersionSets/$API_VERSION_SET_NAME?api-version=2019-01-01