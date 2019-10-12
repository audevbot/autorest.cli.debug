# NameSpaceListByResourceGroup
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces?api-version=2017-04-01