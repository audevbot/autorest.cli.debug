# ApiManagementCreateProductPolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PRODUCT_NAME="myproduct"
POLICY_NAME="mypolicy"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/products/$PRODUCT_NAME/policies/$POLICY_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "format": "xml",
    "value": "<policies>\r\n  <inbound>\r\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\r\n    <log-to-eventhub logger-id=\"16\">\r\n                      @( string.Join(\",\", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) \r\n                  </log-to-eventhub>\r\n    <quota-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(context.Request.Method == &quot;POST&quot; ? 1:2)\" />\r\n    <base />\r\n  </inbound>\r\n  <backend>\r\n    <base />\r\n  </backend>\r\n  <outbound>\r\n    <base />\r\n  </outbound>\r\n</policies>"
  }
}
'