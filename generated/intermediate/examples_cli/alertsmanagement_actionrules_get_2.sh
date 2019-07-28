# GetActionRuleById
RESOURCE_GROUP="myresourcegroup"
ACTION_RULE_NAME="myactionrule"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.AlertsManagement/actionRules/$ACTION_RULE_NAME --api-version 2019-05-05-preview