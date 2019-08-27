# List all snapshots in a resource group.
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/snapshots --api-version 2018-09-30