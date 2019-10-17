# ApiManagementUpdateAuthorizationServer
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
AUTHORIZATION_SERVER_NAME="myauthorizationserver"

az rest --method patch --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/authorizationServers/$AUTHORIZATION_SERVER_NAME?api-version=2019-01-01