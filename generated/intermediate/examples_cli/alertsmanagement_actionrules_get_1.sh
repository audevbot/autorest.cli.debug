# GetActionRulesResourceGroupWide
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.AlertsManagement/actionRules --api-version 2019-05-05-preview