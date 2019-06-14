# ApiManagementCreateApiTagDescription
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
TAG_DESCRIPTION_NAME="mytagdescription"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/tagDescriptions/$TAG_DESCRIPTION_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "description": "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API",
    "externalDocsUrl": "http://some.url/additionaldoc",
    "externalDocsDescription": "Description of the external docs resource"
  }
}
'