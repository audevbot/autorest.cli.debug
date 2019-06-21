# ApiManagementCreateApiIssueComment
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
ISSUE_NAME="myissue"
COMMENT_NAME="mycomment"
USER_NAME="myuser"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/issues/$ISSUE_NAME/comments/$COMMENT_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "text": "Issue comment.",
    "createdDate": "2018-02-01T22:21:20.467Z",
    "userId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""
  }
}
'