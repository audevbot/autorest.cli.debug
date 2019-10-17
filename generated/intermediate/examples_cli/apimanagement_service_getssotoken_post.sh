# ApiManagementServiceGetSsoToken
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/getssotoken?api-version=2019-01-01 --body '
{}
'