# ApiManagementListNotificationRecipientEmails
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
NOTIFICATION_NAME="mynotification"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/notifications/$NOTIFICATION_NAME/recipientEmails --api-version 2019-01-01