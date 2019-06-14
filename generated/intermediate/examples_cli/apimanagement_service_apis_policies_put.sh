# ApiManagementCreateApiPolicy
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
POLICY_NAME="mypolicy"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/policies/$POLICY_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "format": "xml",
    "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
  }
}
'