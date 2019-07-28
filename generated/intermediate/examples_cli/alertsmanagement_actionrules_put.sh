# PutActionRule
RESOURCE_GROUP="myresourcegroup"
ACTION_RULE_NAME="myactionrule"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.AlertsManagement/actionRules/$ACTION_RULE_NAME --api-version 2019-05-05-preview --is-full-object --properties '
{
  "location": "Global",
  "tags": {},
  "properties": {
    "scope": {
      "scopeType": "ResourceGroup",
      "values": [
        "/subscriptions/1e3ff1c0-771a-4119-a03b-be82a51e232d/resourceGroups/alertscorrelationrg"
      ]
    },
    "conditions": {
      "severity": {
        "operator": "Equals",
        "values": [
          "Sev0",
          "Sev2"
        ]
      },
      "monitorService": {
        "operator": "Equals",
        "values": [
          "Platform",
          "Application Insights"
        ]
      },
      "monitorCondition": {
        "operator": "Equals",
        "values": [
          "Fired"
        ]
      },
      "targetResourceType": {
        "operator": "NotEquals",
        "values": [
          "Microsoft.Compute/VirtualMachines"
        ]
      }
    },
    "type": "Suppression",
    "suppressionConfig": {
      "recurrenceType": "Daily",
      "schedule": {
        "startDate": "12/09/2018",
        "endDate": "12/18/2018",
        "startTime": "06:00:00",
        "endTime": "14:00:00"
      }
    },
    "description": "Action rule on resource group for daily suppression",
    "status": "Enabled"
  }
}
'