# ApiManagementHeadIdentityProvider
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
IDENTITY_PROVIDER_NAME="myidentityprovider"

az rest --method head --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/identityProviders/$IDENTITY_PROVIDER_NAME?api-version=2019-01-01