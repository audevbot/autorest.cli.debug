# ApiManagementCreateApiIssue
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
ISSUE_NAME="myissue"
USER_NAME="myuser"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/issues/$ISSUE_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "title": "New API issue",
    "description": "New API issue description",
    "createdDate": "2018-02-01T22:21:20.467Z",
    "state": "open",
    "userId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""
  }
}
'