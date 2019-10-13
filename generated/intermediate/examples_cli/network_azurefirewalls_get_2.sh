# List all Azure Firewalls for a given subscription

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Network/azureFirewalls?api-version=2018-11-01