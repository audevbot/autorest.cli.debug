# changestate
SMART_GROUP_NAME="mysmartgroup"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.AlertsManagement/smartGroups/$SMART_GROUP_NAME/changeState?api-version=2019-05-05-preview --body '
{
  "comments": "Acknowledging smart group"
}
'