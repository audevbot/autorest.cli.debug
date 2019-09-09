# GetActionRulesResourceGroupWide
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.AlertsManagement/actionRules?api-version=2019-05-05-preview