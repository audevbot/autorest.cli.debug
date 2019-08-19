# Get Managed Clusters by Resource Group
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ContainerService/openShiftManagedClusters --api-version 2018-09-30-preview