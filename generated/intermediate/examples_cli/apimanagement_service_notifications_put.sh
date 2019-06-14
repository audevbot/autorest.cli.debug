# ApiManagementCreateNotification
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
NOTIFICATION_NAME="mynotification"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/notifications/$NOTIFICATION_NAME --api-version 2019-01-01 --is-full-object --properties '
{}
'