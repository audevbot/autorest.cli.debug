# Resolve
ALERT_NAME="myalert"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.AlertsManagement/alerts/$ALERT_NAME/history?api-version=2019-05-05-preview