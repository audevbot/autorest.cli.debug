# ApiManagementCreateEmailTemplate
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
TEMPLATE_NAME="mytemplate"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/templates/$TEMPLATE_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "subject": "Your request for $IssueName was successfully received."
  }
}
'