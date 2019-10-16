# ApiManagementCreateApiOperationPolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
OPERATION_NAME="myoperation"
POLICY_NAME="mypolicy"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/operations/$OPERATION_NAME/policies/$POLICY_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "format": "xml",
    "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
  }
}
'