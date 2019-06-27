# Returns the list of available operations.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/operations --api-version 2018-07-10