# ApiManagementGetApiDiagnostic
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
DIAGNOSTIC_NAME="mydiagnostic"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/diagnostics/$DIAGNOSTIC_NAME --api-version 2019-01-01