# Deletes a WAF policy within a resource group
RESOURCE_GROUP="myresourcegroup"
APPLICATION_GATEWAY_WEB_APPLICATION_FIREWALL_POLICY_NAME="myapplicationgatewaywebapplicationfirewallpolicy"

az rest --method delete --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies/$APPLICATION_GATEWAY_WEB_APPLICATION_FIREWALL_POLICY_NAME?api-version=2019-06-01