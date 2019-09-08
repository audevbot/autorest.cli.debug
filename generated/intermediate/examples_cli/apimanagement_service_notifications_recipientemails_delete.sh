# ApiManagementDeleteNotificationRecipientEmail
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
NOTIFICATION_NAME="mynotification"
RECIPIENT_EMAIL_NAME="myrecipientemail"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/notifications/$NOTIFICATION_NAME/recipientEmails/$RECIPIENT_EMAIL_NAME?api-version=2019-01-01