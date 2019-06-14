# ApiManagementCreateApiIssueAttachment
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
ISSUE_NAME="myissue"
ATTACHMENT_NAME="myattachment"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/issues/$ISSUE_NAME/attachments/$ATTACHMENT_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "title": "Issue attachment.",
    "contentFormat": "image/jpeg",
    "content": "IEJhc2U2NA=="
  }
}
'