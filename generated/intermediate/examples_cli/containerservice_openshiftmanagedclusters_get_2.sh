# Get OpenShift Managed Cluster
RESOURCE_GROUP="myresourcegroup"
OPEN_SHIFT_MANAGED_CLUSTER_NAME="myopenshiftmanagedcluster"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ContainerService/openShiftManagedClusters/$OPEN_SHIFT_MANAGED_CLUSTER_NAME?api-version=2019-04-30