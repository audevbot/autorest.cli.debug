# Lists all WAF policies in a resource group
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies?api-version=2019-06-01