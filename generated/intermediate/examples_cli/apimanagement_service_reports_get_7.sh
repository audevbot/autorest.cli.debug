# ApiManagementGetReportsByRequest
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
REPORT_NAME="myreport"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/reports/$REPORT_NAME --api-version 2019-01-01