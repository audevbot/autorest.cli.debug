# List all Azure Firewalls for a given resource group
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/azureFirewalls --api-version 2018-11-01