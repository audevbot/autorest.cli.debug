# Get Azure Firewall
RESOURCE_GROUP="myresourcegroup"
AZURE_FIREWALL_NAME="myazurefirewall"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/azureFirewalls/$AZURE_FIREWALL_NAME?api-version=2018-11-01