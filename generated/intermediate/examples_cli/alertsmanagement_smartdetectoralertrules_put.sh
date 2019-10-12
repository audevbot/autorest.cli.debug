# Create or update a Smart Detector alert rule
RESOURCE_GROUP="myresourcegroup"
SMART_DETECTOR_ALERT_RULE_NAME="mysmartdetectoralertrule"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/microsoft.alertsManagement/smartDetectorAlertRules/$SMART_DETECTOR_ALERT_RULE_NAME?api-version=2019-06-01 --body '
{
  "properties": {
    "description": "Sample smart detector alert rule description",
    "state": "Enabled",
    "severity": "Sev3",
    "frequency": "PT5M",
    "detector": {
      "id": "VMMemoryLeak"
    },
    "scope": [
      "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1"
    ],
    "actionGroups": {
      "customEmailSubject": "My custom email subject",
      "customWebhookPayload": "{\"AlertRuleName\":\"#alertrulename\"}",
      "groupIds": [
        "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourcegroups/actionGroups/providers/microsoft.insights/actiongroups/MyActionGroup"
      ]
    },
    "throttling": {
      "duration": "PT20M"
    }
  }
}
'