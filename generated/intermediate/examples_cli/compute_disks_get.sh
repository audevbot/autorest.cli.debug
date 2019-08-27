# Get information about a managed disk.
RESOURCE_GROUP="myresourcegroup"
DISK_NAME="mydisk"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/disks/$DISK_NAME --api-version 2018-09-30