# Get information about a snapshot.
RESOURCE_GROUP="myresourcegroup"
SNAPSHOT_NAME="mysnapshot"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/snapshots/$SNAPSHOT_NAME?api-version=2018-09-30