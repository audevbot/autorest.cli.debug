# ApiManagementHeadOpenIdConnectProvider
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
OPENID_CONNECT_PROVIDER_NAME="myopenidconnectprovider"

az rest --method head --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/openidConnectProviders/$OPENID_CONNECT_PROVIDER_NAME?api-version=2019-01-01