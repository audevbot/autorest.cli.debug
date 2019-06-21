# Get Azure Firewall
RESOURCE_GROUP="myresourcegroup"
AZURE_FIREWALL_NAME="myazurefirewall"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/azureFirewalls/$AZURE_FIREWALL_NAME --api-version 2018-11-01