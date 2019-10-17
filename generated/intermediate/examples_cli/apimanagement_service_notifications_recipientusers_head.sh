# ApiManagementHeadNotificationRecipientUser
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
NOTIFICATION_NAME="mynotification"
RECIPIENT_USER_NAME="myrecipientuser"

az rest --method head --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/notifications/$NOTIFICATION_NAME/recipientUsers/$RECIPIENT_USER_NAME?api-version=2019-01-01