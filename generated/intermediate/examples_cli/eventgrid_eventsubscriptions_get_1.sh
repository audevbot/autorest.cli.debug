# EventSubscriptions_ListGlobalByResourceGroup
RESOURCE_GROUP="myresourcegroup"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/eventSubscriptions --api-version 2019-01-01