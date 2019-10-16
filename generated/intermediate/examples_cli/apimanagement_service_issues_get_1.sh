# ApiManagementGetIssue
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
ISSUE_NAME="myissue"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/issues/$ISSUE_NAME?api-version=2019-01-01