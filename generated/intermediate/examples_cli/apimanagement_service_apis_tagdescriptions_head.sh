# ApiManagementHeadApiTagDescription
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
API_NAME="myapi"
TAG_DESCRIPTION_NAME="mytagdescription"

az rest --method head --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$API_NAME/tagDescriptions/$TAG_DESCRIPTION_NAME?api-version=2019-01-01