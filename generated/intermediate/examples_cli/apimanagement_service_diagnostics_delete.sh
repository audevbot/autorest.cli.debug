# ApiManagementDeleteDiagnostic
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
DIAGNOSTIC_NAME="mydiagnostic"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/diagnostics/$DIAGNOSTIC_NAME?api-version=2019-01-01