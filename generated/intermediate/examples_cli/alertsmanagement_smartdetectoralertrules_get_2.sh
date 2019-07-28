# Get a Smart Detector alert rule
RESOURCE_GROUP="myresourcegroup"
SMART_DETECTOR_ALERT_RULE_NAME="mysmartdetectoralertrule"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/microsoft.alertsManagement/smartDetectorAlertRules/$SMART_DETECTOR_ALERT_RULE_NAME --api-version 2019-06-01