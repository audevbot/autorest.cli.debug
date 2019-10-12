# Resolve
ALERT_NAME="myalert"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.AlertsManagement/alerts/$ALERT_NAME/changestate?api-version=2019-05-05-preview --body '
{
  "comments": "Acknowledging alert"
}
'