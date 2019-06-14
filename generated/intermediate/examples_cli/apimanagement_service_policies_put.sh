# ApiManagementCreatePolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
POLICY_NAME="mypolicy"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/policies/$POLICY_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "format": "xml",
    "value": "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
  }
}
'