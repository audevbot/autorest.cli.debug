# ApiManagementCreateApiIssueAttachment
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
ISSUE_NAME="myissue"
ATTACHMENT_NAME="myattachment"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/issues/$ISSUE_NAME/attachments/$ATTACHMENT_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "title": "Issue attachment.",
    "contentFormat": "image/jpeg",
    "content": "IEJhc2U2NA=="
  }
}
'