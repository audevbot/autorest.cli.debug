# ApiManagementCreatePolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
POLICY_NAME="mypolicy"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/policies/$POLICY_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "format": "xml",
    "value": "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
  }
}
'