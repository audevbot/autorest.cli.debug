# ApiManagementCreateApiTagDescription
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
TAG_DESCRIPTION_NAME="mytagdescription"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/tagDescriptions/$TAG_DESCRIPTION_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "description": "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API",
    "externalDocsUrl": "http://some.url/additionaldoc",
    "externalDocsDescription": "Description of the external docs resource"
  }
}
'