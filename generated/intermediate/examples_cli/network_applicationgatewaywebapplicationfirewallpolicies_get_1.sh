# Lists all WAF policies in a subscription

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies?api-version=2019-06-01