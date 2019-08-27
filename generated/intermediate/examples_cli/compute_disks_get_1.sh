# List all managed disks in a resource group.
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks --api-version 2018-09-30