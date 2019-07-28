# List alert rules
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/microsoft.alertsManagement/smartDetectorAlertRules --api-version 2019-06-01