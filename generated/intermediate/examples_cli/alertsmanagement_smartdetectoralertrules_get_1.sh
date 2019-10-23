# List alert rules
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/microsoft.alertsManagement/smartDetectorAlertRules?api-version=2019-06-01