# ApiManagementListUserIdentities
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
USER_NAME="myuser"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/users/$USER_NAME/identities --api-version 2019-01-01