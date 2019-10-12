# ApiManagementDeleteProperty
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PROPERTY_NAME="myproperty"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/properties/$PROPERTY_NAME?api-version=2019-01-01