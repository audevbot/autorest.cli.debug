# ApiManagementUserConfirmationPasswordSend
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
USER_NAME="myuser"
CONFIRMATION_NAME="myconfirmation"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/users/$USER_NAME/confirmations/$CONFIRMATION_NAME/send?api-version=2019-01-01 --body '
{}
'