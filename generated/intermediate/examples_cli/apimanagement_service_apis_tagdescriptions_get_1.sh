# ApiManagementGetApiTagDescription
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
APIS_NAME="myapis"
TAG_DESCRIPTION_NAME="mytagdescription"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/apis/$APIS_NAME/tagDescriptions/$TAG_DESCRIPTION_NAME --api-version 2019-01-01