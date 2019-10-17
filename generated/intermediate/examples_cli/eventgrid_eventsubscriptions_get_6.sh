# EventSubscriptions_ListByResource
RESOURCE_GROUP="myresourcegroup"
{RESOURCE_TYPE_NAME}_NAME="myresourcetype"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/{providerNamespace}/{resourceTypeName}/${RESOURCE_TYPE_NAME}_NAME/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01