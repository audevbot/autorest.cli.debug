# ApiManagementGetApiIssueComment
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
ISSUE_NAME="myissue"
COMMENT_NAME="mycomment"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/issues/$ISSUE_NAME/comments/$COMMENT_NAME --api-version 2019-01-01